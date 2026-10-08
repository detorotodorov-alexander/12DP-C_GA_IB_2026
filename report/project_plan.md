# Molecular basis of Gelsolin Amyloidosis: a structural and comparative analysis of pathogenic GSN variants

**Group:** 12DP-C · Introduction to Bioinformatics · UPC/UB/UAB · 2026–2027

---

## 1. Project Overview & Team

### General Objective
To explain how pathogenic variants in the *GSN* gene alter the sequence, structure and function of gelsolin to cause Gelsolin Amyloidosis, and to assess the evolutionary conservation of the affected regions through comparison with *Equus caballus* and *Mus musculus*.

### Specific Objectives
- **SO1 – Cause (WP2):** Retrieve and curate the reference human *GSN* gene and gelsolin protein records (UniProt, NCBI, Ensembl), and characterise the two pathogenic variants D187N and D187Y, justifying their selection based on clinical and literature evidence.
- **SO2 – Structure (WP3):** Map the selected variants onto an experimental gelsolin structure and characterise the local structural changes each one introduces relative to the reference state, including effects on the Ca²⁺-binding site and residue contacts.
- **SO3 – Patient impact (WP4):** Link the molecular consequences of each variant to the pathophysiological cascade leading to amyloid deposition and to the clinical manifestations reported in patients.
- **SO4 – Evolution (WP5):** Compare human gelsolin with its *Equus caballus* and *Mus musculus* orthologues through multiple sequence alignment, and quantify the conservation of residue D187 and of the key functional domains.

### Milestones
| ID | Milestone | Planned date |
|---|---|---|
| M1 | Gantt v1 and risk analysis submitted | 09/10/2026 |
| M2 | Variants (D187N, D187Y) and numbering convention confirmed | 09/10/2026 |
| M3 | Core analyses completed (structural comparison and MSA) | 19/10/2026 |
| M4 | Project Status retrospective | 22/10/2026 |
| M5 | Repository frozen (final delivery, 18:00) | 28/10/2026 |
| M6 | Oral defence | TBC |
### Project Members & Roles
| Member | Academic background | Project role | Responsibilities |
|---|---|---|---|
| Alexander | 1st-year student, BSc in Bioinformatics (UAB/UB/UPC/UPF) | Project & Structure Manager | Plans and tracks the project (Gantt), coordinates the team and submits deliverables. Leads WP1 (setup & planning), WP3 (structure) and WP7 (project management). |
| Arseniy | 1st-year student, BSc in Bioinformatics (UAB/UB/UPC/UPF) | Developer & Sequence Analyst | Retrieves orthologues and performs the multiple sequence alignment and conservation analysis. Leads WP5 (evolution) and maintains the README and repository conventions. |
| Biel | 1st-year student, BSc in Bioinformatics (UAB/UB/UPC/UPF) | Product Owner & Scientific Writer | Defines scientific priorities and scope, accepts deliverables and ensures the coherence of the final report. Leads WP4 (patient impact) and WP6 (report). |
| Isaac | 1st-year student, BSc in Bioinformatics (UAB/UB/UPC/UPF) | Scrum Master & Data Curator | Maintains the Project Status document, removes blockers and facilitates team coordination. Leads WP2 (gene/protein records and variants) and the annotated bibliography and references. |


## 2. Work Packages and Tasks

### 2.1 Project and Work Package dates

| ID | Work Package | Lead | Start | End | Working days |
|---|---|---|---|---|---|
| **Project** | Whole project (incl. provisional WP8) | All | 28/09/2026 | 04/11/2026 | 26 |
| WP1 | Setup & planning | Alexander | 28/09/2026 | 09/10/2026 | 10 |
| WP2 | Cause (B1) | Isaac | 06/10/2026 | 14/10/2026 | 6 |
| WP3 | Structure (B2) | Alexander | 08/10/2026 | 19/10/2026 | 7 |
| WP4 | Patient impact (B3) | Biel | 06/10/2026 | 21/10/2026 | 11 |
| WP5 | Evolution (B4) | Arseniy | 05/10/2026 | 15/10/2026 | 8 |
| WP6 | Report | Biel | 06/10/2026 | 27/10/2026 | 15 |
| WP7 | Project management | Alexander | 05/10/2026 | 28/10/2026 | 17 |
| WP8 | Defence (provisional, pending M6 date) | All | 29/10/2026 | 04/11/2026 | 4 |

---

## 3. Risk Analysis
Risks were identified during planning and scored with a 3-point scale (**Score = Likelihood × Impact**; 1–2 Low, 3–5 Medium, 6–9 High). Each risk has an owner and is reviewed weekly in the Project Status document (`status/`), where changes in score and any activation of the contingency plan are recorded.

| Likelihood \ Impact | 1 = Low | 2 = Moderate | 3 = High |
|---|---|---|---|
| **3 = Likely** | 3 Medium | 6 High | 9 High |
| **2 = Possible** | 2 Low | 4 Medium | 6 High |
| **1 = Unlikely** | 1 Low | 2 Low | 3 Medium |

### Risk register

| ID | Risk | L | I | Score | Category | Owner | Linked tasks | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | No experimental structure available for the D187N/D187Y variants | 2 | 3 | 6 | High | Alexander | 3.3, 3.4, 3.4b | Open |
| R2 | Inconsistent residue numbering (mature protein vs precursor) | 3 | 2 | 6 | High | Isaac | 2.3, 6.6 | Open |
| R3 | Delay on the critical path (structural comparison 3.4) | 2 | 3 | 6 | High | Alexander | 3.4, 6.3, 6.6 | Open |
| R4 | A team member becomes temporarily unavailable | 2 | 2 | 4 | Medium | Isaac | 7.1 | Open |
| R5 | Incomplete or ambiguous ortholog records (horse/mouse isoforms) | 2 | 2 | 4 | Medium | Arseniy | 5.2, 5.3 | Open |
| R6 | Report exceeds the length or figure limits (7 pages / 5000 words / 5 figures) | 2 | 2 | 4 | Medium | Biel | 6.1, 6.6 | Open |
| R7 | Merge conflicts or lost work in shared files | 2 | 1 | 2 | Low | Arseniy | 1.3, 7.3 | Open |

### Analysis and contingency plans

- **R1 (High).** Our identified risk is that no experimental structure of gelsolin carrying the D187N or D187Y variant is available in PDB; we have realized because most deposited gelsolin structures correspond to the wild-type protein or isolated domains, so the variant structures may be scarce or absent; our contingency plan consists of activating backlog task 3.4b, generating in silico D187N/D187Y models in PyMOL on the selected wild-type structure, and explicitly stating the limitations of modelled versus experimental data. The trigger is the result of task 3.3 (09/10).
- **R2 (High).** Our identified risk is that variants are reported with different residue numbers across sources (e.g. D187 vs D214); we have realized because the literature uses mature-protein numbering while UniProt uses precursor numbering including the signal peptide; our contingency plan consists of fixing a single convention in task 2.3, keeping a conversion table in the repository, and checking every residue number during the final cross-review (task 6.6).
- **R3 (High).** Our identified risk is a delay in the structural comparison (task 3.4), the longest task on the critical path; we have realized because any delay there propagates directly to tasks 4.3 and 6.4 and to the final delivery; our contingency plan consists of having decoupled report drafting (6.3) from 3.4, keeping a buffer (task 6.6 and 28/10 reserved), and, if 3.4 is not finished by milestone M3 (19/10), reducing the structural scope to a single variant (D187N).
- **R4 (Medium).** Our identified risk is that a team member becomes unavailable for several days; we have realized because the project overlaps with other courses' deadlines and possible illness; our contingency plan consists of assigning a backup member to each Work Package (Alexander ↔ Arseny, Isaac ↔ Biel) and updating the status document twice a week so that work can be handed over without loss.
- **R5 (Medium).** Our identified risk is that non-human gelsolin records are unreviewed or contain several isoforms; we have realized because records for *Equus caballus* may not be manually curated and gelsolin has plasma and cytoplasmic isoforms; our contingency plan consists of prioritising reviewed (Swiss-Prot) entries, always comparing the same isoform across species, and cross-checking any unreviewed sequence against Ensembl and NCBI RefSeq, documenting the choice.
- **R6 (Medium).** Our identified risk is exceeding the report limits; we have realized because the disease mechanism (proteolytic cascade) and three analyses could easily take more than seven pages; our contingency plan consists of fixing a figure budget now (figures from tasks 3.2, 3.4 and 5.4, plus at most two tables), assigning a word budget per section in task 6.1, and checking the word count in task 6.6.
- **R7 (Low).** Our identified risk is overwriting or losing work in shared files such as `report.md`; we have realized because four members edit the same files from the GitHub web interface; our contingency plan consists of announcing edits in the team chat, always pulling before editing, assigning one section per person, and using branches for large drafts.
