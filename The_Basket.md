# The Basket

**Institutional custody and accountability**

Andrew Dube · Pattern Monkey · 16 October 2026 · Revision 3

Public records establish a relationship between ICE and Palantir and a sequence of Medicaid-data transfers, incomplete deletion accounts, corrective searches, and disputed limits on use. They also establish two statements by Todd Blanche that require reconciliation: a June 2025 certification marking no section 208 waiver and a July 2026 answer acknowledging an earlier section 208(b)(1) determination. Those are specific, reviewable questions about public authority. They do not require a theory connecting every person, institution, historical comparison, or symbol discussed in the wider project.

This revision puts the records and the questions they can settle first. Historical comparisons explain possible mechanisms. Symbolic readings and pattern tests appear in appendices and supply no evidence for the factual findings. Unsupported continuity hypotheses have been retired.

**Evidence cutoff:** records inspected on 16 October 2026. The latest court order inspected is ECF 196, filed 8 September 2026. This is not a complete docket audit through the cutoff. Agency representations, judicial findings, institutional assessments, and this document's interpretations remain separately identified.

## How claims are tested

Every consequential claim identifies an actor or institution, an act, a date or period, the record supporting it, counterevidence, and the limit of the conclusion. An available document that has not been read remains retrieval work.

### Record quality and verification status

| Grade | Record type | Permitted use |
| --- | --- | --- |
| A | Primary filing, order, contemporaneous statement, contract record, or official instrument | Establishes what that instrument records, orders, admits, or represents. A party's declaration does not become an independent audit or a judicial finding. |
| B | Established journalism or an institutional account or assessment | Supports the attributed account, with its method, period, and limitations. |
| C | Later first-person recollection | Establishes the person's stated account; the underlying event needs its own assessment. |
| D | Aggregator, secondary compilation, or unauthenticated transcription | A retrieval lead or corroboration. It cannot independently carry a finding. |
| X | No checkable supporting record obtained | Logged without a factual finding. |

Grade, verification status, and inference are different fields. A primary photograph can establish co-attendance while supplying no evidence of collaboration. An SEC filing can establish that proponents made a claim without independently establishing their contract arithmetic. An official statement can establish an agency's position without proving that every underlying act happened as described.

The analytical lanes are observation, structure, comparison, symbolism, and speculation. A sentence that crosses lanes must name the additional evidence required. Relabeling an unsupported allegation as symbolism does not preserve it in the factual argument.

Co-attendance does not establish collaboration. Sponsorship does not establish payment to every attendee. Praise does not establish partnership. Adjacency does not establish direction. Family relationships do not transfer another person's contacts, acts, knowledge, or responsibility.

### The threshold for a capture assessment

The project defines capture as a transition from an optional intermediary to a gatekeeper whose decisions become difficult to bypass, review, correct, or reverse. That gradient is a diagnostic prompt, not a finding that every institution is captured.

**The ordinary case:** an institution may keep records, interpret rules, exercise expertise, coordinate an emergency, or use an incumbent supplier while remaining auditable, appealable, replaceable, and subject to effective renewal or termination.

A capture assessment must identify an actual restriction on alternatives or correction, its practical consequence, and why the strongest ordinary explanation does not adequately account for it. Missing information alone does not meet that threshold. Procurement dependence, deficient verification, unlawful action, coordination, and capture are separate propositions.

Use the ten variables from *The Coup in the Verbs* as a case profile: replaceability, bypass cost, review interval, reversal cost, executive gravity, legislative relevance, access concentration, correction velocity, institutional inertia, and institutional metabolism. Record reasons and counterevidence for each; do not manufacture a composite score. The manuscript's separate Palace-drift test requires evidence of material influence before formal review, resistance to disclosure or challenge, and an additional supported criterion. Proximity and amplification do not satisfy it. [C01]

## The documented spine

### Medicaid data and the limits of the custody record

Case: *State of California v. U.S. Department of Health and Human Services*, No. 3:25-cv-05536-VC, Northern District of California. The principal dataset here is the CMS file received by ICE on 7 January 2026. Later retransmission is recorded separately.

The stages are **sharing or access, engineering ingestion, import into an operational application, generated lead, and enforcement action**. Databricks processing is already reported in a sworn declaration. The open import question concerns ELITE or another application used operationally, rather than ingestion into any computer system.

#### Judicial context

The 12 August 2025 order, ECF 98, granted preliminary relief concerning the agencies' change in Medicaid-data policy. It addressed reasoned decision-making under the Administrative Procedure Act, declined the requested notice-and-comment relief at that stage, and treated the Spending Clause request as moot in light of the APA relief. It predates the January 2026 file and makes no finding about that file's later handling by Palantir. [S01]

The later declarations refer to a 29 December 2025 injunction. Its complete text was not separately inspected in this revision. The 8 September 2026 clarification order, ECF 196, was inspected directly. It orders further work on categories of people whose information may be shared; distinguishes individualized criminal investigation from sharing en masse; addresses covered health-program data beyond Medicaid; and leaves prior restrictions in place pending approval of clarifying language. It does not adjudicate a Palantir purge or establish a person-level enforcement consequence. [S08]

The September order required a proposed stipulation within 28 days. Later stipulations, orders, or appellate developments must be checked before describing the operative scope as of 16 October. The September order is the latest order inspected here, not a claim that nothing later exists.

#### The records in sequence

| Event date | Record and narrow proposition | Limit |
| --- | --- | --- |
| 7 January 2026 and afterward | Briseno's 9 April declaration says ICE received CMS matches, loaded the data into Databricks, and began normalization. Paragraphs 10–12. [S02] | A sworn account of engineering processing. Raw receipt, ingestion, and transformation logs were not independently inspected. |
| About 20 February 2026 | The same declaration says ICE restricted access and quarantined the data following disagreement about the injunction's coverage. Paragraph 13. [S02] | The declaration states the agency's action and explanation; it does not independently establish all recipients' conduct. |
| 24 February 2026 | The Teams exhibit records a deletion and retention discussion. It is an instruction record, not a completed copy inventory. [S04] | An earlier suggestion about retaining a Palantir copy must be read with the subsequent clarification. No completed retention or deletion follows from the suggestion alone. |
| 27–30 March 2026 | The April declaration reports confirmation on 30 March that the file and Databricks data had been deleted, with no other sources or derivatives retained in ICE holdings. Paragraph 16. Later declarations identify 27 March deletion activity. [S02, S05] | This is evidence of a sworn comprehensive deletion representation. Later records qualify its accuracy and completeness. |
| 29 May–1 June 2026 | ECF 172-1 says ICE found a copy in the AWS S3 Production environment after the earlier deletion account. It attributes this to an overlooked bucket and reports deletion, SOC log checks, and confirmation that the storage location no longer contained the file. Paragraphs 11–16. [S05] | Agency verification is reported. The underlying logs were not independently inspected in this review. The label Production does not by itself establish operational use by officers. |
| 9 June 2026; disclosed 7 July | ECF 180 says HHS inadvertently shared a file of the previously transferred plaintiff-state data through a Box folder during a separate transfer. It reports remedial action and cites declarations denying operational ingestion and law-enforcement use. [S06] | A separate retransmission event. It must not be collapsed into an inference that every later copy survived the March or May deletion effort. The attached declarations to ECF 180 were not all separately inspected. |
| 17–22 June 2026; described 8 July | ECF 181-1 says logs showed six users had had a copy, with the file remaining in two users' storage and one recorded download. It describes Teams, OneDrive, recycle-bin, filename, and hash searches and further deletions. Paragraphs 14–22. [S07] | Six logged users is not a verified count of six newly discovered physical copies. One downloaded file was not located. Some filename variants could not be tied to plaintiff-state information. |
| As of 8 July 2026 | ECF 181-1 acknowledges that changed names or contents limit the ability to locate every possible version. It repeats the denial of operational ingestion and enforcement use. Paragraphs 23–24. [S07] | This is an express limitation on comprehensive assurance, alongside specific reported verification work. |
| Government response received 2 July; reproduced 16 July | Plaintiff counsel Anna Rich reproduces defendants' interrogatory response saying the January data were shared with the ELITE Team and Palantir through Teams and subsequently deleted from the chat. Paragraph 4. [S03] | A government response quoted in a plaintiff's declaration. Sharing with a team is not proof of import into its application, a particular contractor's download, or an enforcement outcome. |

The sequence supports a concrete accountability question: comprehensive assurances preceded discoveries of additional copies, and later search efforts acknowledged technical limits. It also contains evidence of corrective work. The remaining inquiry concerns identifiers, scope, lineage, retained exceptions, and the records behind those assurances.

It would be inaccurate to say that only the February discussion is in evidence, that no verification was performed, or that the July opposition is the only source for later copies. The sworn declarations themselves are evidence. They report agency verification; independent inspection of the underlying technical record remains a further step.

Neither the agency's denial nor the gaps are discarded. Operational use remains unresolved on the inspected record. Later ICE copies do not establish post-purge retention by Palantir. Each custodian and each transfer requires its own inventory and lineage.

### Procurement dependence across separate instruments

The earlier Basket merged different procurement documents. This revision separates them.

| Instrument | Purpose and timing | What was verified | What remains outside the finding |
| --- | --- | --- | --- |
| J&A-25-0092 | Prototype modification of task order 70CTD022FR0000170; published April 2025 | The primary PDF selects FAR 8.405-6(a)(1)(i)(A), urgent and compelling need. Its rationale also describes Palantir as the source able to meet the required timetable using the existing platform. PDF pages 2–3. [S09] | Selecting urgency does not mean the document lacks sole-source language. It supplies no 42-vendor review or 18–24-month estimate in the inspected material. Redacted amounts are not reconstructed. |
| J&A-25-0309, support modification identified by the notice as P000012 and by the attachment filename as P00012 | Continued licensing, hosting, operations, maintenance, and adaptive maintenance beyond 25 September 2025; award notice posted 10 October 2025 | SAM.gov and its primary attachment were inspected. The attachment selects FAR 8.405-6(a)(1)(i)(B), sole-capable-source authority. Section 6 says no market research was conducted for this support requirement. Sections 7–8 identify the prior P00009 work and prospective competition efforts. [S10] | This finding belongs to the support action. It does not establish that every Palantir acquisition lacked market research. The notice's spelling of its identifier is preserved rather than silently substituted for the task-order number. |
| J&A-25-0266, ICM and investigative-analytics modernization | A January 2026 posting, with an attachment filename referencing 8 January | An aggregator's transcription describes a distinct modernization procurement, market research, and an 18–24-month transition estimate. [L01] | The original signed attachment was not inspected here. Grade D for this pass. No primary-source finding is made from the transcription. |
| FY25-00257, DHS-wide Palantir blanket purchase agreement | A separate DHS-wide instrument; aggregator posting dated 14 May 2026 | An aggregator transcription attributes a 42-vendor evaluation to this instrument's adopted ICE market research. [L02] | The primary attachment was not inspected. Grade D. The count is excluded from the factual spine pending original-source inspection. |

The support notice lists **$29,898,236 as Base and All Options Value**, not as verified payments or a verified incremental modification amount. Do not add that figure to prototype reporting as though the records establish two independent expenditures. [S10]

**Structural interpretation:** the primary instruments document dependence on the incumbent's configured software, technical rights, approvals, and implementation timetable for the requirements at issue. Continuity and time pressure are substantial ordinary explanations. This supports investigation of switching costs and the feasibility of an exit. It does not establish that anyone deliberately engineered the dependence, that requirements were improperly drawn, or that a source-selection decision violated procurement law.

The formal authority changes between the inspected prototype and support actions. The supporting rationale already discussed a sole available supplier under the prototype's timetable. A simple story that urgency later became exclusive capability would lose that distinction.

A procurement test can now be specific: obtain the requirement, the considered alternatives, the evaluation record, data and software rights, portability obligations, migration options, and any funded transition plan. A feasible alternative that was considered on equal requirements would count against an engineered-exclusion theory.

### Blanche and the two ethics records

The OGE certification was visually inspected, including the selected answer. Section 7(a) reads:

> I received a waiver pursuant to 18 U.S.C. § 208.

The **No** answer is selected. The certification is signed 5 June 2025. The sentence itself contains no limitation to a waiver expressly required by the ethics agreement. That observation does not determine the instrument's legal classification or prove intent. [S11]

In the July 2026 Senate response, Q16(b) asks whether Blanche received a written section 208(b)(1) determination before the 7 April 2025 cryptocurrency memorandum and requests it. He answers:

> Yes, but such determinations are not subject to disclosure.

Q16(f) separately maintains that the memorandum did not constitute a particular matter directly and predictably affecting his financial interests and says ethics officials cleared it. Preserve that explanation as counterevidence. Locator: combined PDF page 193, printed page 10 of the Hirono response set. [S12]

The public-availability rule, 5 C.F.R. §2640.304, provides for requested public access to agency waivers under section 208(b)(1) or (b)(3), subject to specified withholding limitations. A blanket statement about nondisclosure requires explanation if the referenced instrument is such a waiver. This review has not obtained that instrument or adjudicated an exemption. [S13]

The record supports a request for reconciliation: identify the instrument's date, issuing authority, legal basis, covered interests and matters, and whether it was classified as a waiver; explain the June answer in relation to it; and state the specific legal basis for withholding any portion. It does not establish deliberate falsehood, an unlawful financial benefit, or a connection to Palantir.

### Other institutional routes

These rows preserve separate acts. Their placement does not connect them to one another.

| Record | Specific act or attributed position | What it can support |
| --- | --- | --- |
| EO 14205, 7 February 2025 | Establishes the White House Faith Office within the Domestic Policy Council and specifies consultation, policy, and agency-coordination functions. [S14] | A formal policy route. A decision about a named applicant, grant, enforcement case, or contractor needs its own record. |
| EO 14202, 6 February 2025 | Establishes the DOJ task force, chaired by the Attorney General, with membership and functions stated in the order. [S15] | An interagency route. The order's political allegations are the administration's claims, not this document's independently adopted findings. |
| Strategic Bitcoin Reserve order, 6 March 2025 | Establishes reserve and stockpile arrangements and directs agency accounting and related work. [S21] | A public policy act. No personal payment, clemency bargain, or transaction-caused policy change follows from it. |
| Army announcement, 31 July 2025 | Announces an enterprise agreement with Palantir with a maximum potential value of $10 billion over up to ten years. [S22] | An announced contracting framework. The Army expressly distinguishes the ceiling from obligations and commitments. |
| McConnell's Senate-floor statement, 16 March 2016 | States the leadership's position on withholding consent and postponing consideration of the vacancy. [S23] | A documented public position on the nomination process. It does not establish a private instruction or bargain. |
| JCN announcement, 9 January 2017 | Announces an expected campaign expenditure of at least $10 million supporting the next Supreme Court nominee. [S24] | The organization's contemporaneous campaign plan. An announcement is not an independent audit of expenditure or proof of a quid pro quo. |

The earlier Money corridor's income, transaction, policy, and pardon bundle is discontinued as a combined inference. The Maven amount and other unverified quantitative claims are not carried into this spine. Residence and spouse-based routes are removed. Any proposed return requires one act per row, a supporting instrument, and a stated causal question.

## Structure and historical comparison

### The seven moves as questions

The manuscript's sequence is retained as a set of questions, not a validated prediction rule or seven interchangeable boxes: delegitimizing ordinary procedure; normalizing emergency authority; weakening effective checks through legal instruments; restricting autonomous institutions; constructing status-based internal enemies; expanding coercive capacity; and tilting competitive elections. [C01]

For each proposed application, identify the actual instrument, its effect, an ordinary explanation, a counterexample, and an observation that would weaken the diagnosis. Emergency rhetoric alone is insufficient. A court's existence alone does not establish effective restraint; an adverse order's actual implementation is relevant evidence.

The same rule applies to any leader. Examine appointments, legislation, court compliance, spending authority, enforcement choices, and access restrictions under a common test. The previous interpretive-apex discussion of Trump and Netanyahu has been removed. Neither is assigned an apocalyptic character or used to connect the other to an undocumented command structure.

### Cases and transfer limits

| Case | Mechanism considered | Transfer limit or discriminating observation |
| --- | --- | --- |
| Hungary under Orbán | Constitutional and institutional changes that can disadvantage competition while elections continue | Compare particular rules and effects. Continued elections neither settle the matter nor become irrelevant. The U.S. institutional setting differs. |
| Weimar Germany | Emergency decrees and transfer of legislative power | The comparison concerns that mechanism. This document identifies no U.S. equivalent of the Reichstag Fire Decree or Enabling Act. |
| Fascist Italy | Coercion converted into state authority through elite accommodation | The U.S. is not shown here to have the same party-state fusion or abolition of lawful opposition. |
| Late Roman Republic | Repeated exceptional commands and escalation that undermines succession | An ancient republic supplies a limited comparison; its franchise, military organization, and institutions differ substantially. |
| Norway, March–May 2020 | Temporary emergency legislation with an operative parliamentary check | Parliament reports stopping provisions in five of 32 regulations; the act ended on 27 May after one extension. An emergency existed and checks operated. [S18] |
| United States, steel seizure, 1952 | A presidential emergency argument checked by a court | Truman's 10 June message states that, after the 2 June Supreme Court decision, he immediately ordered government possession relinquished. This is his contemporaneous account of compliance. [S19] |

The first four are manuscript-based background comparisons, not newly replicated historical investigations. The latter two directly address selection on failed democracies. They show that emergency authority and strong executive action do not inevitably produce permanent concentration. They do not prove that contemporary U.S. checks will succeed.

A stronger later study should define its case-selection rule before collecting additional successes and failures, specify which powers actually expired or persisted, and compare implementation rather than rhetoric alone. Two negative cases improve discrimination; they do not validate the entire model.

### Independent assessments of U.S. democracy

| Publication | Observation period and reported result | Interpretation limit |
| --- | --- | --- |
| V-Dem, *Democracy Report 2026*, dataset v16 | Its U.S. section reports a 24% LDI decline during 2025 and a rank change from 20th to 51st. It separately reports 0.79 in 2023 and 0.57 in 2025. [S16] | The one-year percentage and the 2023–2025 endpoints are different comparisons. These are V-Dem's model-based assessments, with estimation and revision limits. |
| Freedom House, *Freedom in the World 2026*, U.S. report | Reports 81/100, compared with 84/100 the prior year, and retains the Free designation. [S17] | A distinct institutional assessment with different concepts and scales. It is not a replication of V-Dem or proof of identical classification. |

Both report deterioration in their own measures. Agreement in direction does not eliminate common reliance on public events, methodological disagreement, or uncertainty. This Basket makes no unqualified claim of unprecedented decline on its own authority and does not infer a particular actor's motive from an index.

## What the network register establishes

The original row numbers are preserved for traceability. Verification below describes this revision. A prior grade in the supplied register is not represented as a fresh source check.

| Original row | Disposition and supported proposition | Provenance and stop |
| --- | --- | --- |
| 1 | **Verified A, narrowed.** The 2025 primary justification concerns an ImmigrationOS prototype under the existing task order and specifies the timetable and requirements. | S09. Redacted monetary details are not filled from another action's notice. No dataset-specific outcome follows. |
| 2 | **Verified A.** The official support notice and J&A-25-0309 support the sole-capable-source wording and the selected authority for that later action. | S10. This is the newly closed lead. Neither authority nor market-research statements migrate to unrelated actions. |
| 3 | **Verified A for the filing and its claims.** The SEC filing identifies the filer and co-filers and advocates a human-rights due-diligence report. It states an over-$81-million ICE figure attributed to company disclosures. | S20. The filers are Presbyterian Life & Witness through the Presbyterian Church (U.S.A.), A Corporation; Portico Benefit Services; and Missionary Oblates of Mary Immaculate-US. The proposal concerns defense-related human-rights risks, with ICE discussed in its supporting material. No independent contract-total reconciliation or proposal outcome was performed. |
| 4 | **No new factual finding; excluded as a network bridge.** The supplied register grades the award-tribute account B. | Its journalism was not reopened. Even a verified speech and praise would need a further instrument to support funding, instruction, or operational control. |
| 5 | **X, unresolved.** The proposed interviews were not inspected. | Episode, date, and transcript required. An interview would establish a published conversation, not a contract or direction. |
| 6 | **Not reopened; excluded from the spine.** The supplied register reports a contributor appointment, later departure, and Epstein-file references. | No fresh finding is made about the appointment, counts, or chronology. References in records do not establish wrongdoing or another person's prior knowledge. |
| 7 | **Retired from this network argument.** Spouse-based attribution is removed. | No contact, responsibility, or knowledge is transferred between spouses. No new inquiry into family members is initiated. |
| 8 | **X; vague association removed.** Platforming or praise is not entered without a specific attributable act and relevance test. | No finding about the named speakers or their relationships follows. |
| 9 | **Verified A, limited to the order.** EO 14205 establishes the office and its location and functions. | S14. The personnel clause in the supplied register was not separately reverified and is not needed for this finding. |
| 10 | **Not reopened; retained only as a disputed lead.** The supplied register describes faith leaders' complaint and a White House response. | Retrieve the article, identify the exact access decision and response. No connection to Palantir follows from the allegation. |
| 11 | **D in the supplied register; no new finding.** The advocacy report was not inspected. | Neither the plural claim nor a tie to the policy office or contractor is established here. |
| 12 | **Status-only claim excluded from the argument.** No confirmation vote is relied on in this revision. | Holding office would identify authority, not responsibility for an unrelated act. |
| 13 | **Verified A for a narrower statement.** The Senate QFR records Blanche saying he met Epstein victims or counsel twice, including on 16 July 2026. | S12, combined PDF page 1. A self-reported meeting is supported; the vague claim that he was central to all file handling is not adopted. No Palantir link follows. |
| 14 | **Narrow negative evidence verified; funding inference not retained.** The MIT-commissioned report says its review found no Epstein donation to MIT supporting Wilczek and records his denial of support. | S25, PDF page 30, footnote 29. That finding is institution- and search-specific. It is not a universal clearance. The conference-attendance component was not newly verified. This path supplies no bridge to the conduct at issue and is retired here. |

The directly verified contracting relationship is supported by rows 1–2. Row 3 documents shareholder advocacy, not an independent technical confirmation of either contract. Other rows may concern real contact, public speech, or official status; none supplies the missing allocation, instruction, or causal record needed to connect those people to the Medicaid custody events.

## Records to seek and public work to complete

A missing record is not automatically a public disclosure entitlement. Identify whether a rule, an order, an existing-records request, or a voluntary explanation is the relevant route. Preserve asserted exemptions and search limitations. A refusal establishes the refusal and its stated basis, not the withheld act.

### Requests to record holders

| Question | Record holder and route | Closure test |
| --- | --- | --- |
| What was the pre-April 2025 section 208(b)(1) instrument, and how does it relate to the June certification? | DOJ ethics office; request the instrument and explanation under the applicable public-availability procedure, including §2640.304 where applicable. | Instrument date, issuer, authority, scope and classification; reconciliation of the certification; specific reasons and lawful redactions for withheld portions. |
| What did deletion verification actually cover? | ICE/DHS custodians of Databricks, S3, O365, Teams, OneDrive, Box, security searches and associated contractor records; request existing responsive records. | Identified objects and derivatives, systems and custodians searched, dates, methods, exceptions, known transformations, and support for the attestations. |
| Did sharing become import into an operational application? | ICE system and data owners; agency-controlled records of contractor work. | A dataset identifier or traceable derivative connected through lineage to a successful import into a named application. |
| Did the data produce an enforcement consequence? | ICE query, lead, review and case-record custodians. | A trace from that dataset or derivative to a generated lead, human decision and attempted or applied action. A contract's capabilities do not satisfy this test. |
| What can be said about contractor deletion? | ICE/DHS for records within agency control; Palantir for any voluntary public statement or attestation it chooses to provide. | Scope-specific inventories and attestations supported by retained records. FOIA is not presented as a direct command to a private company. |
| Is the supplier realistically replaceable? | ICE/DHS contracting and system owners. | Source selection, market research, software and data rights, migration requirements, actual alternatives, and a costed, usable transition path. |

The existing Medicaid brief contains an ICE records-request draft. This revision supplies newly read docket references and a narrower verification question; that separate draft has not been edited or submitted. No message, FOIA request, complaint, or fee commitment has been sent. [C03]

### Public retrieval and analysis

| Item | State at this revision | Next work |
| --- | --- | --- |
| ECF 172-1, 180 and 181-1 | **Retrieved and read.** | Incorporate these primary records into any later edition of the separate Medicaid evidence brief. |
| ECF 196, 8 September 2026 order | **Retrieved and read.** | Check subsequent stipulations, orders and appellate activity before stating current legal scope. |
| J&A-25-0309 / P00012 support attachment | **Retrieved and read from the official notice.** | Preserve the distinction between total options value, modification value and obligations. |
| January ICM and DHS-wide justifications | **Original attachments not inspected.** | Retrieve each original; confirm dates, selected authority and the location of every numerical estimate. Until then, L01–L02 stay D. |
| Original 2022 source-selection chain | **Not inspected.** | Obtain the original notice, evaluation and award-action history before attributing the origin of dependence. |
| Broader political corridors and unverified network rows | **Not findings in this revision.** | Reopen only for a specific act with material relevance and a named record. |
| Comparative diagnostic validation | **Not completed.** | Predefine case selection and decision criteria; add successes, failures and ambiguous cases. |

For each unresolved claim keep: record needed, custodian, identifier, date range, retrieval route, source grade, verification status, search coverage, counterevidence, closure test and as-of date. Record Supported, Provisionally Supported, Indeterminate, Rejected or Retired separately from confidence. A failed retrieval does not establish that a record does not exist.

## Countermeasures and tests of this argument

The practical safeguards are review dates that require fresh authorization; portable records; workable alternatives; defined data purposes; access and transformation logs; scoped deletion verification; independent review; timely appeal; and remedies that change conduct.

The argument weakens where records show effective review, compliance, correction, portability, or replacement. Verified non-use would resolve the dataset-specific use question without erasing an earlier custody failure. A lawful, scope-specific ethics instrument and a documented explanation could reconcile the two statements. A functioning competitive transition would count against exclusive dependence. These possibilities must stay available as outcomes.

The original predictions are preserved as hypotheses recorded in the prior Basket, rather than scored successes: that access would become documented while enforcement use remained unpinned; that resolution might come through settlement or a purge order; and that individual accountability might not follow. Their independent pre-outcome registration dates were not verified. To score future predictions, state a deadline and an observable event in advance, preserve the record, and record failures as explicitly as successes.

*No crown. No chains. Exit always valid.*

## Appendix A Historical scholarship and control of interpretation

The historical essay concerns comparable functions: organizing service through calendars, authorizing knowledge through texts and revelation, and defining who may interpret an account. These are background and comparisons credited to the scholars and ancient sources cited in that essay. They are not new discoveries of this Basket or evidence of a continuous organization. [C02]

Its useful case is Epiphanius as a narrator with an interest in his own account. The revised essay distinguishes his reported encounters and intervention from proof that he witnessed every alleged rite. It also distinguishes the independent survival of *Pistis Sophia* from external verification of an accusation preserved inside its literary dialogue. Every witness's framing remains open to scrutiny. [C02]

Control of interpretation is ordinary when its exercise remains answerable to evidence, appeal and correction. The project term eethnic shield is retained only as an earlier name for a proposed protection from correction; it is not an ethnic category. The neutral description carries the analysis.

BT-01 through BT-09 remain credited historical background and research topics, with each source's limits. **BT-10 and BT-11 are retired as unsupported organizational-continuity hypotheses.** They are not an open bridge from ancient communities to contemporary people, finance or institutions. Their retirement remains visible in the revision record.

Babylonia is a historical geographic and chronological designation where the scholarship uses it. It is not a modern population, ancestry claim, or network label.

## Appendix B Symbolic reading

Revelation may be read as a vocabulary for imagining imperial power, authorized speech, participation and exclusion. This is literary interpretation. Its contribution is a question about how power represents itself, not additional evidence that a modern event occurred.

No modern person is cast as a Revelation character. Public leaders belong in conduct-based political analysis under the same evidentiary test. Religious affiliation, nationality, ancestry and family contact supply no substitute for an act.

The operation gate has two requirements: a documented allocation such as funding, access, exclusion or enforcement, and evidence that the allocation tracked the proposed symbolic framing rather than an ordinary explanation. No symbolic node in this Basket has been shown to meet both. Procurement is documented; symbolism-driven procurement is not established.

The pharmakeia comparison remains a separate lexical and literary topic in the historical essay. It carries no claim about a specific modern substance, procedure, organization or transaction. This appendix claims no novelty for the general idea that inherited narratives shape political language. A claim of intellectual priority would require a separate literature review.

## Appendix C Pattern tests and recorded nulls

The prior Basket reports that a proposed global excess-synchronization result was not shown, that a physical test was not run, and that two saved strict-episode tests returned p = 1.0. The underlying data, code and protocols were not independently rerun in this revision. These are carried-forward reports, not a new replication or a statistical credential for the political analysis. [C04]

The arithmetic corrections remain: 413 = 7 × 59; 22 = 2 × 11; 437 = 19 × 23. Adjacent dates alone do not establish deliberate coordination. No sky object, ritual timing node, or selected count contributes evidence to the documented spine.

The useful practice is preserving null results, correction dates and test limits. A method must also be assessed for selection, multiple comparisons, coverage and reproducibility before its reliability is claimed.

## Appendix D Revision decisions

| Adversarial issue | Action in revision 3 |
| --- | --- |
| Historical or religious naming implying a continuous hidden organization | Renamed the analytical function in neutral terms; retired BT-10 and BT-11; retained historical scholarship with its limits. |
| Modern leaders beside apocalyptic character imagery | Removed the interpretive-apex passage and all modern-person casting. |
| Merged procurement instruments | Separated four instruments and verified the support action's primary attachment. The 42-vendor count stays outside the spine pending original-source inspection. |
| Urgency treated as inconsistent with sole-source supporting language | Corrected. Selected authority and supporting rationale are recorded separately. |
| Deletion records treated as though only instructions were evidence | Corrected. Sworn representations and later reports of verification are retained; independent access to underlying logs remains distinct. |
| Later copies known only through plaintiffs' opposition | Closed part of the gap by reading ECF 172-1, 180 and 181-1 directly. Added the separate Box retransmission. |
| September order unreviewed | Retrieved ECF 196. Later docket developments remain retrieval work. |
| Blanche certification paraphrased | Quoted §7(a), visually checked No, and read Q16(b) and (f) with the public-availability rule. |
| Shareholder proponents unidentified | Identified the filers in the SEC document. Preserved the contract figure as their attributed claim. |
| MIT review treated as universally closing a person's history | Narrowed the finding to the report's donation search and recorded denial. Retired the proposed bridge. |
| Proximity-only rows called either proven networks or nonexistent contacts | Separated record quality, verification status and the inference each record permits. |
| Historical selection on failed regimes | Added Norway and the 1952 U.S. steel-seizure episode as negative cases, with a further validation requirement. |
| V-Dem alone carrying an unattributed superlative | Attributed its result and added Freedom House's different measure and retained Free classification. |
| Public homework blended with records held by institutions | Split retrieval work from requests to custodians; named the route and closure test. |
| Clock and ritual timing material weakening the factual argument | Moved null reports into a methodological appendix; removed ritual timing and sky nodes from the argument. |
| Personal byline substitution | Restored Andrew Dube as the research author reference. |
| Unchecked broader corridors | Preserved verified acts separately; removed bundled inferences and deferred unsupported numerical claims. |

## Sources

Primary court records below are hosted by court-record repositories or a state attorney general. Host location is identified where it matters. A primary filing remains a party's representation unless it is an order or is otherwise independently verified. All newly inspected sources were accessed on 16 October 2026.

### Court and dataset records

- **S01 — ECF 98, order, 12 August 2025.** Court PDF hosted by California DOJ; especially PDF pages 4–5. [Primary PDF](https://oag.ca.gov/system/files/attachments/press-docs/98%20Order%20Granting%20in%20Part%20and%20Denying%20in%20Part%20PI.pdf).
- **S02 — ECF 155-4, Briseno declaration, 9 April 2026.** PDF pages 2–3, paragraphs 10–16. [Primary filing](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.155.4.pdf).
- **S03 — ECF 182-1, Rich declaration, 16 July 2026.** Paragraph 4 reproduces the government's response; paragraphs 5–6 address deletion material and counsel's explanation. [Primary filing](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.182.1.pdf).
- **S04 — ECF 182-2, Teams exhibit DHS_PI0002.** One-page produced exhibit; chat dated 24 February 2026. Read with S03 for provenance. [Primary exhibit](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.182.2.pdf).
- **S05 — ECF 172-1, Briseno declaration, 4 June 2026.** Paragraphs 11–17 on the S3 copy, deletion and log checks. [Primary filing](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.172.1.pdf).
- **S06 — ECF 180, defendants' notice, 7 July 2026.** Box retransmission and cited remedial measures. Its attachments were not all independently inspected. [Primary filing](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.180.0.pdf).
- **S07 — ECF 181-1, fourth Briseno declaration, 8 July 2026.** PDF pages 4–5, paragraphs 14–24. [Primary filing](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.181.1.pdf).
- **S08 — ECF 196, clarification order, 8 September 2026.** Three pages. Retrieved through the Oregon DOJ tracker and read directly. [Primary order](https://storage.courtlistener.com/recap/gov.uscourts.cand.452203/gov.uscourts.cand.452203.196.0.pdf). [Tracker](https://www.doj.state.or.us/oregon-department-of-justice/federal-oversight/federal-litigation-tracker/). The full docket index was unavailable; this is not an exhaustive later-docket check.

### Procurement

- **S09 — ICE J&A-25-0092.** Primary agency PDF mirrored by the Immigration Policy Tracking Project; image pages visually inspected. Use PDF page order because printed page labels are inconsistent. [PDF](https://iptp-production.s3.amazonaws.com/media/documents/2025.04.17_ICE_Limited_Sources_Justification_for_70CTD022FR0000170.pdf). [Official notice](https://sam.gov/opp/f71acee6010c423db4902446a59a690c/view).
- **S10 — ICE J&A-25-0309 and support award notice.** Official SAM.gov notice inspected directly, including description, award-value label, attachment and posting date. Attachment: 5.1.1-P00012_LSJ_Exceeding_SAT_Redacted_V4.pdf, five pages; authority checkbox visually inspected on PDF page 2. [Official notice and attachment](https://sam.gov/opp/cb55c3c595e5491b94b0090f448ffd21/view#attachments-links).
- **L01 — J&A-25-0266 retrieval lead.** GovTribe transcription of a January 2026 ICM justification, with AI summary separately labelled by the site. Original attachment not inspected. [Transcription](https://govtribe.com/file/government-file/1-dot-5-dot-1-ice-lsj-icm-palantir-final-signed-redacted-1-dot-8-dot-26-dot-pdf). [Official notice identified through the corpus](https://sam.gov/opp/5477991867424397affe85e2fad8b5fc/view).
- **L02 — FY25-00257 retrieval lead.** GovTribe transcription of the DHS-wide LSJ; 42-vendor text appears in the reproduced market-research portion. Original not inspected. [Transcription](https://govtribe.com/file/government-file/lsj-fy25-00257-palantir-final-redacted-for-posting-5-dot-2026-dot-pdf). [Official notice](https://sam.gov/opp/5ec301a2417f4e68aed185d8fefe379e/view).
- **L03 — Original 2022 source-selection lead.** Identified in the manuscript, not inspected in this pass. [SAM.gov notice](https://sam.gov/opp/027b10d0cff3409c91d52d5cef37d576/view).

### Ethics and institutional routes

- **S11 — Blanche ethics-agreement compliance certification, signed 5 June 2025.** OGE primary PDF, page 3, §7(a); answer visually checked. [Certification](https://extapps2.oge.gov/201/Presiden.nsf/PAS%2BIndex/92E6C79E88537F4485258CA1002C2338/$FILE/Blanche%20EA%20Certification%201%20of%201.pdf).
- **S12 — Senate Judiciary Blanche QFR responses, July 2026.** Committee-hosted combined PDF; Hirono Q16 begins on PDF page 192; responses 16(b)–(f) on PDF page 193, printed page 10. The meeting statement used in network row 13 appears on PDF page 1. [Responses](https://www.judiciary.senate.gov/download/2026-07-15_qfr-responses_blanchepdf). [Committee hearing page](https://www.judiciary.senate.gov/committee-activity/hearings/the-nomination-of-the-honorable-todd-blanche-to-be-attorney-general-of-the-UNITED-STATES).
- **S13 — 5 C.F.R. §2640.304.** Public availability of agency waivers and withholding limitations; eCFR displayed current through 15 October 2026 at inspection. [Regulation](https://www.ecfr.gov/current/title-5/chapter-XVI/subchapter-B/part-2640/subpart-C/section-2640.304).
- **S14 — EO 14205, 7 February 2025.** Official GPO text, establishment and functions of the White House Faith Office. [Text](https://www.govinfo.gov/content/pkg/DCPD-202500240/html/DCPD-202500240.htm).
- **S15 — EO 14202, 6 February 2025.** Official Federal Register PDF, particularly section 2. [Order](https://www.govinfo.gov/content/pkg/FR-2025-02-12/pdf/2025-02611.pdf).
- **S21 — Strategic Bitcoin Reserve and Digital Asset Stockpile order, 6 March 2025.** Official presidential instrument, sections 2–4. [Order](https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/).
- **S22 — U.S. Army enterprise-agreement announcement, 31 July 2025.** Institutional account identifying the ceiling and denying that it represents specific obligations. [Announcement](https://www.army.mil/article-amp/287506/u_s_army_awards_enterprise_service_agreement_to_enhance_military_readiness_and_drive_operational_efficiency).
- **S23 — McConnell statement, 16 March 2016.** Contemporaneous Senate leadership statement; a primary statement of position. [Statement](https://www.republicanleader.senate.gov/newsroom/remarks/mcconnell-on-supreme-court-nomination/).
- **S24 — JCN campaign announcement, 9 January 2017.** Primary organizational announcement of an expected expenditure, not an independent spending audit. [Announcement](https://judicialnetwork.com/jcn-press-release/judicial-crisis-network-launches-10-million-campaign-preserve-justice-scalias-legacy-support-president-elect-trump-nominee/).

### Comparative measures and network records

- **S16 — V-Dem, Democracy Report 2026.** Dataset v16; U.S. section, printed pages 32–39, including the reported one-year change and separate longer-period endpoints. Primary report of the institute's own assessment. [Report](https://www.v-dem.net/documents/75/V-Dem_Institute_Democracy_Report_2026_lowres.pdf).
- **S17 — Freedom House, United States, Freedom in the World 2026.** Own institutional assessment: 81/100, prior 84/100, Free. [Country report](https://freedomhouse.org/country/united-states/freedom-world/2026).
- **S18 — Storting, Corona Act repealed.** Official parliamentary account, updated 3 June 2020; describes exercised minority checks and the act's termination. [Account](https://www.stortinget.no/en/in-english/about-the-storting/news-archive/front-page-news/2019-2020/corona-act-repealed/).
- **S19 — Truman, Special Message to Congress on the Steel Strike, 10 June 1952.** Contemporaneous presidential account preserved by the Truman Library; distinguish his account of compliance from a fresh independent reconstruction. [Message](https://www.trumanlibrary.gov/library/public-papers/161/special-message-congress-steel-strike).
- **S20 — SEC PX14A6G, accession 0001214659-26-005220.** Proponents' exempt-solicitation notice dated 28 April 2026; header and supporting material inspected. A filing is not an SEC endorsement of its assertions. [Filing](https://www.sec.gov/Archives/edgar/data/1321655/000121465926005220/o429261px14a6g.htm).
- **S25 — Goodwin Procter, MIT fact-finding report, January 2020, updated 17 January.** Institution-commissioned review; PDF page 30, printed page 29, footnote 29. [Report](https://web.mit.edu/fact2020/files/MIT-report.pdf?200117=). The scope-specific negative finding and the recorded denial are separately identified.

### Project sources and coverage

- **C01 — The Coup in the Verbs Unified Manuscript (6).** Current project copy read on 16 October 2026; its header gives an evidence cutoff of 17 August 2026. Used for the framework, ten-variable profile, comparison limits and Palace-drift gate. This Basket does not edit that manuscript or claim to reverify its entire bibliography.
- **C02 — Sacred Time Narrative Authority Revision, 16 October 2026.** Supplied 26-page PDF; especially pages 9–10, 14 and 26. Historical interpretation and source distinctions were inspected; its ancient-source investigation was not independently repeated.
- **C03 — Medicaid ICE Palantir Evidence Brief, 16 October 2026.** Supplied five-page PDF. Its request remains a draft. This Basket's newly retrieved filings extend the brief's stated retrieval coverage without silently updating that separate file.
- **C04 — The Basket, prior version.** Supplies the earlier pattern-test reports and predictions as historical project claims. No underlying statistical rerun or independent prediction-registration audit was performed.
- **C05 — Network source register and adversarial pass supplied in this conversation.** Used as the revision brief. Individual recommendations were tested against the retrieved records; the pass itself is not independent verification of its factual assertions.

For the central new receipts, SHA-256 identifies the downloaded bytes, not the truth or completeness of the record:

| Record | Bytes | SHA-256 |
| --- | ---: | --- |
| J&A-25-0309 support attachment | 934856 | d14d6982b4454ffb6ceb145cbad5aecc89666aa40b09d106d9f55a3f3d9229d8 |
| ECF 172-1 | 149891 | e73e772a92cdaf66ac6f8b4dd2d8adf2eadf1033279c3a614f2d2c11f7d89ae6 |
| ECF 180 | 133320 | 344c0c8a9eef9f459bb1042d8f567b3106ce26cb29c6e775286eecdfa97e3add |
| ECF 181-1 | 313389 | 5bb7ba6401f46e8867501621f1c4eb13c15e7ca51f15422a87ae67a1128ce395 |
| ECF 196 | 149614 | a5c5bf9d8b996738a8a808e3cd8c287fd7edeb0a2478dd0f448bff051b1d9a47 |
| OGE certification | 503715 | 22330df1d54f96821a27797372bb6d14a238f1bae9e8fe091530ab963c3c8988 |
| Senate QFR combined PDF | 4140308 | c43ed362ff9b50f3b85e290bbeceba28b2fb955157d9838237fb4a6b34377638 |

