"""Reproduce adult person-weighted HTOPS July 2026 estimates.
Run: python reproduce.py (requires pandas, numpy, openpyxl).
Raw sources and dictionary are preserved unchanged alongside this script.
No survey indicator is assigned a new WOBBLE threshold or severity label.
"""
from pathlib import Path
import zipfile, json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
with zipfile.ZipFile(ROOT / 'HTOPS_HPS_2607_CSV.zip') as z:
    d = pd.read_csv(z.open('HTOPS_HPS_2607_PUF.csv'))
    r = pd.read_csv(z.open('HTOPS_HPS_2607_REPWGT_PUF.csv'))
assert d.SCRAMID.is_unique and r.SCRAMID.is_unique
d = d.merge(r, on='SCRAMID', validate='one_to_one')
assert np.allclose(d.PWEIGHT, d.PWEIGHT0)
# Reconstruct the published health table: an unselected 'none' checkbox is
# insufficient to establish insurance coverage. Other-only coverage is unknown;
# IHS-only respondents without other coverage are included as uninsured.
insured = d[['HLTHINS_EMP','HLTHINS_MEDICARE','HLTHINS_MEDICAID','HLTHINS_PURCH','HLTHINS_VA','HLTHINS_TRICARE']].eq(1).any(axis=1)
uninsured = d.HLTHINS_NO.eq(1) | (d.HLTHINS_IHS.eq(1) & ~insured & ~d.HLTHINS_OTH.eq(1))
d['INSURANCE_TABLE_STATUS'] = np.where(insured,2,np.where(uninsured,1,-99))
w = d.PWEIGHT.to_numpy()
rw = d[[f'PWEIGHT{i}' for i in range(1, 81)]].to_numpy()

# indicator, variable, adverse codes, valid codes, recall, applicable population
specs = [
 ('food_insufficiency','FD_SUFF',[3,4],[1,2,3,4],'last 7 days','all adults'),
 ('cut_necessities_for_energy','ENERGY',[1],[1,2],'last 2 months','all adults'),
 ('unsafe_home_temperature','HSE_TEMP',[1],[1,2],'last 2 months','all adults'),
 ('unable_pay_full_energy_bill','ENERGY_BILL',[1],[1,2],'last 2 months','all adults'),
 ('expenses_somewhat_very_difficult','EXPENSE_DIFFICULT',[3,4],[1,2,3,4],'last 2 months','all adults'),
 ('uninsured','INSURANCE_TABLE_STATUS',[1],[1,2],'current','all adults'),
 ('could_not_always_keep_home_cool','TEMP_SAFE',[2,3],[1,2,3],'this summer','all adults'),
 ('behind_rent_currently','RENTCUR',[2],[1,2],'current','adults in rented homes'),
 ('behind_mortgage_currently','MORTCUR',[2],[1,2],'current','adults in mortgaged homes'),
 ('household_employment_income_loss','WORKLOSS',[1],[1,2],'last 4 weeks','all adults'),
]
rows=[]
for group, subset in [('all',np.ones(len(d),dtype=bool)),('household_income_under_35000',d.RHHINCOME.isin([1,2]).to_numpy())]:
 for name,var,yes,valid,recall,pop in specs:
    applicable = subset & (d[var].to_numpy()!=-88)
    validmask = subset & d[var].isin(valid).to_numpy()
    yesmask = subset & d[var].isin(yes).to_numpy()
    p = 100*w[yesmask].sum()/w[validmask].sum()
    reps = 100*rw[yesmask].sum(axis=0)/rw[validmask].sum(axis=0)
    se = np.sqrt((4/80)*np.square(reps-p).sum())
    rows.append(dict(group=group,indicator=name,variable=var,recall=recall,population=pop,
      estimate_pct=float(p),se_pp=float(se),ci90_low=float(p-1.645*se),ci90_high=float(p+1.645*se),
      weighted_numerator=float(w[yesmask].sum()),weighted_valid_denominator=float(w[validmask].sum()),
      missing_pct=float(100*w[applicable & ~validmask].sum()/w[applicable].sum()),
      sample_valid=int(validmask.sum()),sample_adverse=int(yesmask.sum())))
out=pd.DataFrame(rows)
out.to_csv(ROOT/'microdata_results.csv',index=False)

# Match published counts to rounding tolerance before reporting ratios.
table_rates=json.loads((ROOT/'computed_rates.json').read_text())
mapping={'food_insufficient':'food_insufficiency','necessities_cut_for_energy':'cut_necessities_for_energy',
 'unsafe_temperature':'unsafe_home_temperature','energy_bill_not_full':'unable_pay_full_energy_bill',
 'expenses_somewhat_very_difficult':'expenses_somewhat_very_difficult','uninsured':'uninsured',
 'safe_temp_not_always':'could_not_always_keep_home_cool'}
for t in table_rates:
 if t['key'] in mapping:
    a=out.loc[(out.group=='all') & (out.indicator==mapping[t['key']])].iloc[0]
    assert abs(a.weighted_numerator-t['numerator'])<2, t['key']
    assert abs(a.weighted_valid_denominator-t['denominator'])<2, t['key']
print(out[['group','indicator','estimate_pct','ci90_low','ci90_high','missing_pct']].to_string(index=False))
weights=np.array([.37,.31,.23,.07,.02]); fixed=np.array([8,23,26,7.6,12])
benchmark=float(weights@fixed)
food=out.loc[(out.group=='all')&(out.indicator=='food_insufficiency'),'estimate_pct'].iloc[0]
variant=float(benchmark+.37*(food-8))
result={'weights':weights.tolist(),'fixed_inputs':fixed.tolist(),'fixed_benchmark':benchmark,
 'food_source_variant':variant,'variant_warning':'Changes survey and recall period; not a like-for-like change or current composite.',
 'field_dates':'2026-07-15/2026-08-03','publication_date':'2026-09-24',
 'variance':'4/80 * sum((replicate_ratio - full_ratio)^2); 90% interval = estimate +/- 1.645 SE',
 'missing':'Exclude invalid/nonanswer from each denominator; report item missing separately. Do not treat missing as no hardship.',
 'scope':'PWEIGHT adult person estimates, not household counts. Low-income grouping uses reported 2025 household income.',
 'limitations':'Cross-sectional reports do not identify CRE-bank-credit causation. Confidence intervals exclude systematic nonresponse bias.'}
(ROOT/'calculation_summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
