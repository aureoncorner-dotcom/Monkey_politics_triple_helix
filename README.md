# WOBBLE working-class evidence: reproducible calculation

Expanded run: October 19, 2026. User weights: food/nutrition 37%, housing/utilities 31%, health 23%, livelihoods 7%, financial resilience 2%.

Run `python reproduce.py` with Python, pandas, numpy and openpyxl installed. The script reads the preserved official public-use ZIP without extracting personal records to additional files, joins adult person weights to 80 replicate weights by SCRAMID, validates seven published totals within rounding tolerance, and writes microdata_results.csv and calculation_summary.json. SHA256SUMS.json identifies the source bytes used. No external access is required to rerun.

## Results and interpretation

The frozen exploratory basket uses rates [8,23,26,7.6,12] with weights [.37,.31,.23,.07,.02], giving 16.842 arithmetic points. It combines different populations, reference periods and concepts. It is not a calibrated severity scale, a percentage of people harmed, or an October estimate. Replacing only the food input with July HTOPS food insufficiency gives 16.6108347. This source variant changes survey and recall period and cannot establish improvement. Other concepts remain unchanged; student measures do not receive extra weight on top of the five domains.

July HTOPS finds 12.7465% of valid adult responses reporting a household reduction in necessities such as food or medicine to pay an energy bill in the preceding two months. The 90% sampling interval is 10.8103–14.6827%. Among adults reporting 2025 household income under $35,000 the estimate is 23.7528% (19.3260–28.1795%). This is a direct self-reported household budget tradeoff. It is not evidence that commercial real estate losses caused banks to restrict credit.

Rates use PWEIGHT: percentages of adults reporting household conditions, not percentages of households. Each denominator excludes nonanswers; missing_pct is the weighted nonanswer share within the applicable population. Rent and mortgage estimates are conditional on the applicable tenure and a valid answer; missing tenure is outside that conditional population. Income subgroups exclude unreported income. Neither exclusion means no hardship. The underlying public-use file contains 12,755 records.

Variance = 4/80 times the sum of squared differences between each replicate ratio and the full-weight ratio. 90% intervals = estimate +/- 1.645 standard errors. The overall unweighted response rate was 9.4%, weighted 10.4%. Intervals do not capture systematic nonresponse bias. This cross-sectional survey cannot demonstrate individual transitions or identify causation. The health checkbox must be recoded to reproduce the published insured, uninsured and unknown categories; the script documents that recode. Uninsured status is not equivalent to forgone necessary care.

## Census provenance

Measurement: July 15–August 3, 2026. Publication: September 24, 2026. Downloaded for the October 19 run. Recall periods appear in the output. Income refers to calendar 2025. Table workbooks and the public-use ZIP are unmodified.

- Release and table links: https://www.census.gov/data/tables/2026/demo/hhp/2607.html
- Table source base: https://www2.census.gov/programs-surveys/demo/tables/hhp/2026/2607/ (append each preserved XLSX filename).
- Public-use data landing: https://www.census.gov/data/datasets/time-series/demo/hhp/2026.html
- Public-use ZIP: https://www2.census.gov/programs-surveys/demo/datasets/hhp/2026/topical/HTOPS_HPS_2607_CSV.zip
- Methods: https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/HTOPS_2607_Source_and_Accuracy.pdf
- User notes: https://www2.census.gov/programs-surveys/demo/technical-documentation/hhp/2607_HTOPS_Household_Pulse_User_Notes_09102026.pdf

computed_rates.json records workbook cells and count-based ratios, including transportation (not included in the replicate analysis). microdata_results.csv contains national and income-under-$35,000 ratios and sampling intervals, plus current rent/mortgage arrears and reported household employment-income loss. Current arrears are not comparable to SHED arrears at any point during a prior year.

## Other inputs retained in the assessment

- SHED 2025: October 17–28, 2025 interviews; published May 19, 2026; chapter updated May 26. The four input rates are 8% food insufficiency, 23% renter arrears over a year, 26% cost-related skipped medical expenses, and 12% unable to meet a $400 emergency by any means. https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm
- September 2026 U-6 7.6%, released October 2: https://www.bls.gov/news.release/archives/empsit_10022026.htm
- September prices, released October 14: https://www.bls.gov/news.release/archives/cpi_10142026.htm
- September real earnings, released October 14: https://www.bls.gov/news.release/archives/realer_10142026.htm
- Student debt, Q2 2026, August 11 release: https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/pdf/hhdc_2026q2.pdf
- Trellis student basic needs: Fall 2025 fieldwork, report April 2026. Voluntary institutional sample; results not nationally representative. https://www.trellisstrategies.org/wp-content/uploads/2026/04/SFWS-Aggregate-Report_FALL2025_FINAL.pdf

## Gate result and missing observations

The October 17 WOBBLE-GATE-v2.3-r1 baseline is retained: Scenario 8 Gates 1/2 cleared, Gate 3 unearned; Phase II / PRE-WATCH. The household evidence does not establish CRE losses -> restrictive bank decisions -> reduced credit availability or household income. Continued lending growth remains counterevidence. Aggregate balances alone mix supply, demand, repayments, writeoffs and reporting changes.

Remaining evidence needs: matched bank/borrower records linking dated CRE losses and capital effects to tighter approval criteria, rejected or reduced credit for comparable applicants and subsequent activity/income; comparable current student basic-needs observations; nutritional adequacy, displacement, nationwide utility shutoffs and interrupted care; matched-person employment transitions. Future releases are not pre-scored. No thresholds, within-domain weights or automatic phase rules were added.
