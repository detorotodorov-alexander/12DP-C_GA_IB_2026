# Project status

Live document, updated at least twice a week (task 7.1, Isaac) and reviewed in the retrospective on 22 October. Planned dates come from [`report/project_plan.md`](../report/project_plan.md); the Gantt is in [`gantt/`](../gantt/).

Status: Pending · In progress · Completed · Incident · Backlog · Canceled. When something changes, write why in Notes.

**Updated up to 26/10/2026**

> **Schedule incident (detected 24/10):** Gantt v1 placed the end of the project on 28/10, but the official deadline is **Monday 26/10 at 22:00** (Disease Project Overview). Tasks 6.4–6.6 and 7.4 have been re-planned inside 24/10–26/10, and the WP8 (oral defence) dates remain to be confirmed. The re-planning is reflected in the live Gantt and will be analysed in task 7.4.

| Task | Description | Resp. | Plan. start | Plan. finish | Real start | Real finish | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Create the repo and folders | Alexander | 28/09 | 28/09 | 14/09 | 14/09 | Completed | Repo created before the plan existed (first commit 14/09). |
| 1.2 | Read the brief and the rubric | All | 28/09 | 29/09 | 14/09 | 17/09 | Completed | Course instructions uploaded to `files/instructions/` between 14/09 and 17/09. |
| 1.3 | Write the README and repo rules | Arseniy | 29/09 | 30/09 | 17/09 | 09/10 | Completed | First version 17/09, finished once the disease and roles were known (08–09/10). |
| 1.4 | Agree on scope, objectives and roles | All | 05/10 | 05/10 | 05/10 | 08/10 | Completed | Roles added one by one by each member (05/10–08/10). |
| 1.5 | Draft the Gantt and risk analysis | Alexander | 30/09 | 02/10 | 28/09 | 09/10 | Completed | Gantt draft from 28/09; risk analysis added 05/10 (Biel) and rewritten 09/10. |
| 1.6 | Set up the status document | Isaac | 01/10 | 02/10 | 09/10 | 09/10 | Completed | Late: planned 01–02/10, created 09/10. |
| 1.7 | Review and submit Gantt v1 | Alexander, Biel | 09/10 | 09/10 | 09/10 | 09/10 | Completed | Submitted on time. Teacher feedback received (see "Feedback" below). |
| 2.1 | Get the gene and protein records | Isaac | 30/09 | 05/10 | 19/10 | 19/10 | Completed | Late. Human records and database IDs in `files/data/gsn_records_summary.md`; stayed on branch usr/dg-isc until 25/10 (merge delayed). |
| 2.2 | Collect evidence on pathogenic variants | Isaac | 06/10 | 08/10 | 24/10 |  | In progress | Late (Incident 2.x). Focus reduced to the assigned variant D187N and the closely related D187Y. |
| 2.3 | Confirm the assigned variant and the numbering | All | 09/10 | 09/10 | 19/10 | 24/10 | Completed | Variant c.640G>A, p.Asp214Asn = D187N. Conversion table in `files/data/residue_numbering.md` (mitigation of R2). |
| 2.4 | Describe how normal gelsolin works | Isaac | 13/10 | 14/10 | 24/10 | 25/10 | Completed | Late. Written as part of the report Background. |
| 3.1 | Choose the reference PDB structure | Alexander | 13/10 | 13/10 |  |  | Real dates to be confirmed by owner | Structural analysis (human WT, mutant and horse) provided by the teaching team; record date received. |
| 3.2 | Show the variants on the structure | Alexander | 14/10 | 14/10 |  |  | Real dates to be confirmed by owner | Figure of WT D187 vs mutant N187 taken from the teaching-team report. |
| 3.3 | Look for structures of the variants | Biel | 09/10 | 09/10 |  |  | Real dates to be confirmed by owner |  |
| 3.4 | Compare normal vs variant around residue 187 | Alexander, Biel | 15/10 | 19/10 | 25/10 | 25/10 | Completed | Written by Biel in Results (structural comparison) with Figure 1. Effect of D187N is chemical rather than structural. |
| 3.4b | Backup: build the variants in PyMOL | Alexander | 13/10 | 14/10 |  |  | Canceled | Contingency for R1 not needed: mutant structure provided by the teaching team. |
| 4.1 | Disease background | Biel | 30/09 | 06/10 | 25/10 | 25/10 | Completed | Reassigned to Isaac (agreed with Biel): clinical picture and epidemiology in the report Background. |
| 4.2 | How the disease develops | Biel | 07/10 | 14/10 | 25/10 | 25/10 | Completed | Reassigned to Isaac (agreed with Biel): disease mechanism in the report Background. |
| 4.3 | Link the variant to the symptoms | Biel, Isaac | 20/10 | 21/10 | 24/10 |  | In progress | Late. |
| 5.1 | Choose the species | Arseniy | 06/10 | 07/10 | 15/10 | 15/10 | Completed | Done by Biel: horse (mandatory), mouse and fly; rationale in `files/data/homologs_table.md`. |
| 5.2 | Get the horse and second-species sequences | Arseniy | 08/10 | 09/10 | 15/10 | 15/10 | Completed | Done by Biel. Curated RefSeq entries; horse record lacks the N-terminal region (R5 partly materialised). |
| 5.3 | Align the sequences | Arseniy | 13/10 | 14/10 | 19/10 | 25/10 | Completed | Pairwise CDS and protein alignments (WT vs mutant, human vs horse, human vs mouse) in `files/data/`. |
| 5.4 | Check how conserved D187 is | Arseniy, Alexander | 15/10 | 16/10 | 25/10 | 26/10 | Completed | D187 conserved in horse (D163) and mouse (D212). Written by Arseniy in Results; corrections by Isaac (26/10). |
| 6.1 | Report skeleton (BMC format) | Biel | 05/10 | 05/10 | 17/09 | 25/10 | Completed | First skeleton by Biel (17/09); restructured to BMC format with section owners by Isaac (25/10). |
| 6.2 | Bibliography | Isaac | 09/10 | 14/10 | 24/10 | 25/10 | Completed | Late. 9 sources selected and annotated in `references/README.md` (reviews vs original papers vs databases). |
| 6.3 | First drafts of Background, Methods and Results | Each WP lead | 16/10 | 20/10 | 24/10 | 26/10 | Completed | All first drafts merged into main on 26/10 (PRs #17 Biel, #22 Arseniy, #24 Isaac). Missing: human–horse structural results and structural Methods. |
| 6.4 | Final Results, Discussion, Abstract and Conclusions | All | 22/10 | 23/10 | 26/10 |  | In progress | Re-planned to 26/10. Discussion and Conclusions pending; Abstract by Isaac at the end. |
| 6.5 | Fix references and Declarations | Isaac | 26/10 | 26/10 | 26/10 |  | Pending | Re-planned: must be finished before 18:00 on 26/10. |
| 6.6 | Final review (buffer day) | All | 27/10 | 27/10 | 26/10 |  | Pending | Re-planned from 27/10 to 26/10 (18:00–21:30): original date was after the deadline. |
| 7.1 | Keep the status document updated | Isaac | 01/10 | 28/10 | 09/10 |  | Incident | Not updated between 09/10 and 24/10. Updated again from 24/10. |
| 7.2 | Keep the live Gantt updated | Alexander | 13/10 | 28/10 |  |  | Incident | Live Gantt not updated since 09/10. |
| 7.3 | Save every source in references/ | All | 28/09 | 28/10 | 24/10 |  | In progress | 9 sources stored by Isaac (25/10). Full text of 3 papers not available via UPC/CSUC: abstracts stored. Add any new source used in the report. |
| 7.4 | Final Gantt and comparison with v1 | Alexander | 28/10 | 28/10 | 26/10 |  | Pending | Re-planned from 28/10 to 26/10. |
| 8.1 | Slides | All | 29/10 | 30/10 |  |  | Backlog | Dates to confirm when the defence date is known. |
| 8.2 | First rehearsal | All | 03/11 | 03/11 |  |  | Backlog |  |
| 8.3 | Second rehearsal | All | 04/11 | 04/11 |  |  | Backlog |  |

## Risks

Scores and contingency plans are in [section 4 of the plan](../report/project_plan.md#4-risk-analysis).

| Risk | Score | Status | Notes |
|---|---|---|---|
| R1 | 6 | Closed | Mutant structure provided by the teaching team; 3.4b canceled. |
| R2 | 6 | Materialised, mitigated | The teaching-team report itself mixes numbering (position 214 vs D187). Conversion table added; all numbers to be checked in 6.6. |
| R3 | 6 | Open | Structural interpretation still in progress. |
| R4 | 6 | Open | |
| R5 | 4 | Materialised, mitigated | Horse record lacks residues 1–53 (signal peptide region); does not affect domain G2 or D187. |
| R6 | 4 | Open | To check in 6.6 (≤ 5000 words, ≤ 5 figures/tables). |
| R7 | 3 | Open | |
| R8 (new) | 6 | Materialised | Deadline mismatch in Gantt v1 (28/10 vs 26/10). Mitigation: re-planning of 6.4–7.4 into 24–26/10. |
| R9 (new) | 6 | Open | Unbalanced contributions (teacher feedback 09/10). Mitigation: each member commits their own report section from their own account. |

## Feedback from the teaching team (Gantt v1)

| Comment | Action | Owner | Status |
|---|---|---|---|
| Rewrite the General Objective as a formal infinitive statement | Rewrite in `project_plan.md` and report Background | To assign | Pending |
| Define "WP" before using it | Fix first mention in `project_plan.md` | To assign | Pending |
| Workload imbalance between members | See R9 | All | In progress |
