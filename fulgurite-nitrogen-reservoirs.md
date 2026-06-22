# Nitrogen Reservoirs in Fulgurites: A Provenance Protocol and the Case Against Structural Si–N in Lightning Glass

> **CONTRACT — Falsifiable research program.** Everything in this file is meant to be attacked with instruments, controls, and detection limits. Claims wear status bins. Nothing here depends on, or lends support to, anything in `/method`, `/theory`, or `/fiction`. If you cite this file, cite it as geochemistry. The metaphors that generated these questions live in the other folders and stay there.

**Document type:** Perspective + analytical protocol (research-program skeleton)
**One-line claim:** In fulgurites, the question "is there nitrogen?" is meaningless until provenance is resolved; structural Si–N in ordinary lightning glass is not expected on first principles, and the useful contribution is a reservoir-deconvolution protocol plus the targeted replication of two known archive signals.

> **Honest framing up front.** This program does **not** report a coupled carbon–nitrogen–silicon system, a new mineral, or storm-made silicon oxynitride. Its contribution is (1) a quantitative, mechanistic argument for why structural Si–N should be *absent* in ordinary fulgurite glass, (2) a reusable protocol for attributing any detected nitrogen to the correct reservoir, and (3) two scoped replication-and-extension studies of archive signals that already exist in the literature, with explicit statements of what is new. The central structural-nitrogen result is an *expected confirmation*, not a discovery, and is presented as such.

---

## 1. Abstract

Fulgurites are amorphous silica glasses (dominantly lechatelierite) formed when lightning fuses silica-rich substrate. They are repeatedly invoked as recorders of event chemistry, but reports of "nitrogen in fulgurite" routinely conflate three distinct things: nitrogen bonded into the glass network, nitrogen physically trapped as gas, and nitrogen adsorbed or organic on surfaces and in residues. This document does two things. First, it argues from silicate-melt nitrogen systematics that structural (Si–N) nitrogen should be effectively absent in glass quenched from an oxidizing, ~1-second lightning melt, making "no structural Si–N" a *mechanistic prediction* rather than an open question. Second, it provides a provenance protocol that separates four nitrogen reservoirs — lattice-bound, occluded molecular gas, surface/weathering, and organic-residue — and specifies which analytical methods can and cannot discriminate them, including the hard limit that the only direct bonding test (EELS N-K ELNES) is informative only when nitrogen is above detection, i.e., in the case the prediction says will not occur. Within that protocol, two known archive signals are re-examined with stated novelty deltas: occluded vesicle gas (oxidized N, CO/CO₂, isotopes) as a multi-specimen reproducibility test, and carbon-correlated reduced phases (reduced phosphorus, iron silicides) as a quantified spatial-correlation test. Post-strike bioreceptivity is included only as a scoped pilot, because the general phenomenon of silicate-glass bioalteration is already established and the strike-specific question is sample-limited. The expected outcome is an upper bound on structural nitrogen, provenance-resolved accounting of any nitrogen that is present, replicated or falsified archive signals, and a bioreceptivity result that must survive a full substrate-control suite to count.

---

## 2. Background and the Actual Gap

Fulgurites are well characterized as a material. The dominant silica phase in tube fulgurites is lechatelierite, an amorphous fused silica, classified as a mineraloid; many specimens are partly protocrystalline, and a standard five-type morphological classification (sand, clay, caliche, rock, droplet) is in wide use. Two archive signals are already published:

- **Vesicle gas archive.** Trapped CO₂, CO, and NO in glassy bubbles of a Late Pleistocene Libyan Desert fulgurite were used, with δ¹³C and a C/N ratio, to reconstruct paleo-vegetation and paleoclimate (Navarro-González et al., 2007). Oxidized nitrogen in sealed vesicles is therefore a demonstrated, not hypothetical, reservoir.
- **Carbon-driven reduced chemistry.** Lightning-induced reduction of phosphorus oxidation state, and the occurrence of iron silicides in fulgurites, are established in the fulgurite literature (Pasek and co-workers; iron-silicide-in-fulgurite reports).

The gap is not "do fulgurites record anything." It is that **nitrogen provenance is routinely under-determined**: a positive nitrogen signal is reported without establishing whether it is lattice, gas, surface, or organic. This protocol targets that gap directly. Everything in the document is organized around one rule: *resolve the reservoir before attributing the nitrogen.*

---

## 3. Why Structural Si–N Is Not Expected (the quantitative prior)

The prediction "no structural Si–N in ordinary fulgurite glass" is not a hedge. It follows from melt chemistry:

1. **Oxygen fugacity controls nitrogen speciation.** In silicate melts, nitrogen enters the network as structural N³⁻ only under strongly reducing conditions; under oxidizing conditions it is present overwhelmingly as physically dissolved molecular N₂. Nitrogen solubility and speciation in silicate melts are governed primarily by fO₂ and melt polymerization (experimental silicate-melt N-solubility systematics).
2. **Fulgurites form oxidizing and quench fast.** Ordinary sand/soil fulgurites form in air and solidify in roughly one second. This is the opposite of the conditions under which structural N enters a silica network.
3. **Oxynitride glass requires deliberate synthesis.** Si–O–N glasses are produced by reducing atmospheres, NH₃ treatment, or nitride starting materials — engineered conditions absent from a soil lightning strike.
4. **Terrestrial nitrides are vanishingly rare.** Natural silicon oxynitride (sinoite) is known essentially only from reduced meteoritic contexts; confirmed terrestrial nitride minerals (e.g., siderazot) are exceptional. The base rate for forming a nitride in struck soil is near zero.

**Consequence for the framework:** the structural-nitrogen test is included to place a defensible *upper bound* and to close the question quantitatively, not because a positive is plausible. Reporting the expected negative is low-information on its own; its value is that it is paired with provenance-resolved accounting of the nitrogen that *is* present (Sections 4–6).

---

## 4. The Four-Reservoir Provenance Model

Any nitrogen signal must be assigned to one of these before interpretation.

| Reservoir | Definition | Prior expectation | What confirms it |
|---|---|---|---|
| **R1 — Lattice / structural** | N bonded into the silica network (Si–N) | Expected absent (Section 3) | Spatially coherent N-K ELNES Si–N fingerprint in fresh interior glass, N above detection, not surface/gas/organic/artifact |
| **R2 — Occluded molecular gas** | N-bearing gas physically trapped in sealed vesicles (NO/NOₓ, possibly N₂ mixtures) | Plausible; primary archive target | Sealed-vesicle crush/stepped-heating release distinct from modern air/soil; isotopes inconsistent with infiltration |
| **R3 — Surface / weathering** | Nitrate/ammonium adsorbed on rinds, cracks, pores, handling-contaminated zones | Expected common; default contamination | Interior-vs-rind gradient; absence in fresh interior; presence on open surfaces |
| **R4 — Organic residue** | N in charred biomass, PAHs, microbial films, trapped carbonaceous particles | Mixed; must be separated | Co-location with carbon phases; CN-rich, organic ELNES/Raman signature; not in clean lechatelierite |

Physical entrapment (R2) is not bonding (R1). Organic nitrogen (R4) is neither lattice nor event gas. Surface nitrogen (R3) cannot be treated as event nitrogen without interior, blank, and gradient controls.

---

## 5. Analytical Decision Tree and Its Honest Limits

This is the load-bearing section, because the protocol's credibility depends on stating what the instruments *cannot* do.

### 5.1 What each method actually resolves

- **NanoSIMS (CN⁻, SiN⁻, NO⁻; interior maps).** Best available tool for sensitive nitrogen detection and spatial mapping. **Limit:** molecular secondary ions can form by atomic recombination in the sputter plume, so a SiN⁻ signal does **not** by itself prove a pre-existing Si–N bond, and CN⁻ — the standard sensitive N ion — cannot distinguish lattice N from organic or adsorbed N. NanoSIMS therefore *detects and localizes* nitrogen and supports reservoir assignment by spatial pattern, but cannot, alone, establish R1.
- **EELS N-K edge (ELNES).** The only direct bonding-environment test; can in principle distinguish Si–N from nitrate, organic N, and trapped gas. **Limit:** requires nitrogen above detection. In the predicted regime (R1 absent), there is no nitrogen to fingerprint, so the decisive tool is informative only in the non-default case. This is a structural feature of the problem, not a fixable gap.
- **Vacuum-crush + stepped heating + GC-MS + δ¹³C/δ¹⁵N.** Standard, appropriate, and decisive for **R2** (occluded gas vs infiltration). Strongest lane for event nitrogen.
- **XANES/EXAFS (P, Fe).** Strong for oxidation state in the redox arm (Section 7).
- **SEM-EDS, Raman, XRD.** Texture, phase context, crystalline reduced phases, carbon mapping, target selection. Not decisive for nitrogen speciation.

### 5.2 Demoted or dangerous alone

- **XPS N 1s** — surface-biased; reads contamination unless on freshly fractured interior with depth profiling and strict blanks. Not a primary structural-N tool.
- **FTIR / Raman Si–N assignments** — Si–N and Si–O features overlap/are ambiguous in glass; not decisive.
- **Any surface-only nitrogen detection** — not event evidence without full reservoir deconvolution.

### 5.3 Honest default output

Because EELS is mute when R1 is absent and NanoSIMS cannot prove a bond alone, the **expected deliverable in the default case is an upper bound on structural nitrogen plus reservoir-resolved attribution of detected nitrogen to R2/R3/R4** — not a positive structural claim. Spatial homogeneity in clean lechatelierite is supporting evidence for/against R1 but is not sufficient by itself (finely disseminated organic residue can also appear homogeneous).

---

## 6. Sub-Study A — Vesicle Gas Archive (replication and extension)

**Known result being extended:** Navarro-González et al. (2007) — occluded CO₂/CO/NO with δ¹³C and C/N in one specimen.

**Novelty delta (what is actually new):**
- multi-specimen reproducibility rather than a single best case;
- quantitative sealed-vs-open vesicle comparison within and across specimens;
- explicit blank/modern-air/¹⁴C control framework;
- provenance-resolved nitrogen — separating occluded oxidized N gas (R2) from adsorbed (R3) and organic (R4) contributions via stepped-heating release structure.

**Methods:** vacuum crush; stepped heating; GC-MS; δ¹³C; δ¹⁵N; gas ratios.
**Controls:** procedural blanks; modern-air reference; open-vesicle comparison; weathered-rind comparison.

**Falsifies the gas-archive claim if:**
- crushed sealed-vesicle gas is compositionally and isotopically indistinguishable from modern air/soil;
- N₂/O₂/Ar ratios indicate infiltration rather than event preservation;
- carbon dates ¹⁴C-modern where ancient preservation is claimed;
- stepped-heating release does not separate occluded gas from adsorbed contamination.

> **δ¹⁵N caveat (do not overclaim).** Lightning-fixed nitrogen overlaps heavily in δ¹⁵N with atmospheric N₂ (≈0‰) and several soil sources; the fractionations are small. δ¹⁵N is supporting context, not a standalone discriminator of event nitrogen.

---

## 7. Sub-Study B — Carbon-Correlated Reduced Phases (replication and extension)

**Known result being extended:** lightning-induced phosphorus reduction and iron silicides in fulgurites (Pasek and co-workers; iron-silicide reports).

**Novelty delta:**
- quantified **spatial correlation** of reduced-phase abundance with carbon-rich vs carbon-poor zones across multiple samples, rather than single-specimen phase identification;
- P/Fe oxidation-state mapping by XANES/EXAFS tied to in-situ organics;
- explicit exclusion of conductor contamination and detrital reduced phases.

**Methods:** SEM-EDS phase mapping; Raman (carbon phases); XRD (crystalline reduced phases); XANES/EXAFS (P, Fe oxidation state); microprobe transects across carbon gradients.

**Falsifies the redox-archive claim if:**
- reduced phases show no spatial correlation with carbon-rich zones;
- reduced phases trace to conductor/contaminant sources rather than soil/organic starting material;
- reanalysis shows the reduced products are detrital contaminants.

**Explicit boundary:** carbon drives local reduction in P and Fe systems; it is **not** invoked to reduce nitrogen into the lattice. There is no claimed mechanism coupling this arm to nitrogen speciation.

---

## 8. Pilot — Post-Strike Bioreceptivity (scoped, not a co-equal hypothesis)

**Why this is only a pilot.** Microbial and fungal colonization and dissolution of silicate glass is an established field, including the colonization sequence on glass surfaces and characteristic granular/tubular bioalteration textures analogous to fungal tunneling of silicates. The general phenomenon is not novel. The narrow open question is whether *strike-specific* chemistry produces a colonization or alteration response distinguishable from ordinary glass, nutrients, surface area, moisture, pH, and disturbance.

**Feasibility limits stated honestly:** fulgurites are rare and individually unique; a truly matched non-strike substrate is unattainable because the strike is itself the disturbance; biogenicity of glass-alteration textures is contested; and maturation can overprint or destroy candidate biosignatures.

**Required controls (must beat all to claim a strike-specific term):** experimental fulgurite generated under realistic discharge (a stronger control than kiln/thermal glass); sterilized fulgurite glass; thermal/kiln glass; protolith from the same site; disturbed non-strike soil; matched nearby non-strike substrate; time series; multi-strike/multi-site replication; blinded colonization scoring.

**Default explanation:** moisture, nutrients, surface area, disturbance, pH.
**Upgrade condition:** colonization or alteration tracks strike-altered redox/mineral/glass chemistry after the full control suite, including experimental-fulgurite controls.

**Stream separation:** biologically colonized specimens must never be used for clean structural-nitrogen (R1) measurement.

---

## 9. What Would Change the Picture (upgrade criteria)

The structural-nitrogen prediction is upgraded only by all of:

1. spatially coherent N-K ELNES **Si–N** fingerprint in fresh interior silica glass, nitrogen above detection, distinguished from nitrate, organic N, and trapped gas; **and**
2. confirmation that the signal is not surface contamination, beam-induced buildup, groundmass mixing, or SIMS recombination.

The archive program is strengthened (not the bonding claim) by:

3. reproducible sealed-vesicle C/N gas signatures distinct from modern infiltration across specimens;
4. carbon-correlated reduced-phosphorus or iron-silicide gradients across multiple samples;
5. a bioreceptivity signal surviving the full control suite of Section 8.

---

## 10. Mandatory Controls (consolidated)

**Analytical:** procedural blanks for all extraction/mounting; nitrogen-free fused-silica control through identical prep; protolith control from the same site; sealed-vs-open paired vesicle sampling; interior-vs-rind gradient; clean lechatelierite core vs mixed groundmass; curation/contaminant audit (consolidants, adhesives, acid treatment, handling residues, storage nitrate, animal/bird contamination, mounting media, beam-induced C/N buildup).

**Biology:** experimental fulgurite; sterilized glass; thermal glass; protolith; disturbed soil; matched non-strike soil; time series; multi-site replication; blinded scoring.

---

## 11. Safety Constraints

No DIY lightning, no high-voltage arc rigs outside institutional labs, no fulgurite collection during active storms, no sealed pressure vessels, no unknown-gas extraction outside a fume hood, no heating of mystery materials, no chemical-synthesis attempts, no mixing of unknown chemicals, and no use of biologically colonized specimens for clean structural-nitrogen measurement. All meaningful testing belongs in institutional laboratories with trained personnel, approved procedures, and appropriate instrumentation.

---

## 12. Limitations and Self-Assessment

- **No coupled-system claim.** Carbon, nitrogen, and silicon are treated as co-located, not mechanistically coupled. There is no "circuit," no planetary process, and no metaphysical framing.
- **The central negative is expected.** "No structural Si–N" is a mechanistic prediction; its standalone information content is low and it is reported as confirmation, paired with provenance-resolved accounting of the nitrogen that is present.
- **Two arms are replications.** The gas-archive and redox-archive results exist in the literature; this program's added value is reproducibility, quantification, control rigor, and nitrogen provenance — stated as such.
- **The decisive bonding test is conditional.** EELS is informative only when nitrogen is above detection, i.e., not in the predicted default case; the honest default output is an upper bound.
- **Statistical power is bounded** by fulgurite rarity and per-specimen uniqueness, most acutely for the bioreceptivity pilot.

**Best honest description of the contribution:** a disciplined nitrogen-provenance protocol for fulgurite glass, a first-principles argument that closes the structural-Si–N question, and the controlled replication/extension of two known archive signals — *not* a new coupled C–N–Si phenomenon.

---

## 13. One-Page Brief

- **Question:** When nitrogen is detected in a fulgurite, which reservoir is it — lattice, occluded gas, surface, or organic — and is any of it event nitrogen?
- **Expected answers:** structural Si–N, no (mechanistically forced); occluded oxidized N gas, possibly yes in well-preserved sealed vesicles; surface nitrate/ammonium, likely contamination; organic-residue N, must be separated.
- **Most decisive methods:** vacuum-crush + stepped heating + GC-MS + isotopes (R2); NanoSIMS mapping + EELS ELNES (R1, conditional); XANES/EXAFS (redox arm).
- **Most dangerous false positive:** surface or recombination-derived nitrogen read as event/lattice nitrogen.
- **Rule:** resolve the reservoir before naming the nitrogen; no reservoir, no claim.

---

## References (verify all before submission)

The following are the key works this program rests on. **Author, year, and venue details should be confirmed against the primary sources before any submission**; several are paraphrased from memory of the literature and at least one attribution in earlier drafts may be incorrect.

- Navarro-González, R., Mahan, S. A., Singhvi, A. K., et al. (2007). *Paleoecology reconstruction from trapped gases in a fulgurite from the late Pleistocene of the Libyan Desert.* Geology, 35(2), 171–174. — Occluded CO₂/CO/NO, δ¹³C, C/N; paleoecology.
- Pasek, M. A., and co-workers — fulgurite phosphorus reduction (e.g., *lightning-induced reduction of phosphorus oxidation state*) and the standard five-type fulgurite morphological classification (Pasek et al., 2012). **Confirm exact citations; the phosphorus-reduction result is associated primarily with Pasek, and any attribution to other authors should be checked.**
- Iron-silicide-in-fulgurite reports (e.g., Feng et al.; and "occurrence of iron silicides in a fulgurite") — **confirm exact reference.**
- Silicate-melt nitrogen solubility/speciation systematics showing fO₂ control and N³⁻ incorporation only under reducing conditions (e.g., Libourel, Marty & Humbert, 2003, and subsequent fO₂-controlled N-solubility studies) — **confirm exact references; this is the load-bearing basis for the structural-Si–N prediction.**
- Microbial/fungal interactions with silicate glasses: review of bio-colonization steps and dissolution (npj Materials Degradation, 2021); volcanic/basaltic glass bioalteration textures and associated communities (e.g., Cockell et al., Geobiology, 2009; basaltic-glass bioalteration literature). — Establishes that glass bioalteration is a mature field.
- Natural silicon oxynitride (sinoite) in enstatite chondrites (Andersen et al., 1964) and confirmation of a rare terrestrial nitride, siderazot (Bette et al., 2021) — boundary markers for nitride rarity.
- Experimental fulgurite generation under realistic discharge, and experimental-vs-natural fulgurite comparisons — basis for the experimental-fulgurite control in the bioreceptivity pilot.

---

## Appendix — Provenance Checklist (use before any positive nitrogen claim)

1. Which reservoir is being read: lattice (R1), occluded gas (R2), surface/weathering (R3), or organic residue (R4)?
2. Was the surface removed or avoided; was the analysis on fresh interior lechatelierite or mixed groundmass?
3. Were procedural blanks and a nitrogen-free fused-silica control run through identical prep?
4. Was protolith from the same site measured?
5. Were sealed and open vesicles compared, and interior-vs-rind gradients measured?
6. For SIMS: is the SiN⁻/CN⁻ signal distinguishable from recombination and from organic/adsorbed nitrogen, or only consistent with detection?
7. For EELS: is nitrogen above detection, and does ELNES distinguish Si–N from nitrate/organic/gas?
8. Were curation contaminants and beam-induced C/N buildup audited?
9. Were biological and clean-chemistry sample streams kept physically separate?
10. Is the conclusion stated as an upper bound where the bonding test was mute?
