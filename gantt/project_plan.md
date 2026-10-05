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
| M3 | Core analyses completed (structural comparison and MSA) | 20/10/2026 |
| M4 | Project Status retrospective | 22/10/2026 |
| M5 | Repository frozen (final delivery, 18:00) | 28/10/2026 |
| M6 | Oral defence | TBC |
### Project Members & Roles
| Member | Academic background | Project role | Responsibilities |
|---|---|---|---|
| Biel | 1st-year student, BSc in Bioinformatics (UPC/UB/UAB) | Product Owner & Scientific Writer | Defines scientific priorities and scope, accepts deliverables and ensures the coherence of the final report. Leads WP4 (patient impact) and WP6 (report). |
| Alexander | 1st-year student, BSc in Bioinformatics | Project & Structure Manager | Plans and tracks the project (Gantt), coordinates the team and submits deliverables. Leads WP1 (setup & planning), WP3 (structure) and WP7 (project management). |
---

## 2. Work Packages and Tasks

### 2.1 Project and Work Package dates

| ID | Work Package | Lead | Start | End | Working days |
|---|---|---|---|---|---|
| **Project** | Whole project (incl. provisional WP8) | All | 28/09/2026 | 04/11/2026 | 26 |
| WP1 | Setup & planning | Alexander | 28/09/2026 | 09/10/2026 | 10 |
| WP2 | Cause (B1) | Isaac | 06/10/2026 | 14/10/2026 | 6 |
| WP3 | Structure (B2) | Alexander | 08/10/2026 | 19/10/2026 | 7 |
| WP4 | Patient impact (B3) | Biel | 06/10/2026 | 21/10/2026 | 11 |
| WP5 | Evolution (B4) | Arseny | 05/10/2026 | 15/10/2026 | 8 |
| WP6 | Report | Biel | 06/10/2026 | 27/10/2026 | 15 |
| WP7 | Project management | Alexander | 05/10/2026 | 28/10/2026 | 17 |
| WP8 | Defence (provisional, pending M6 date) | All | 29/10/2026 | 04/11/2026 | 4 |

### 2.2 Task specifications

Critical path tasks are marked in **bold** (2.1 → 2.2 → 2.3 → 3.2 → 3.4 → 4.3 → 6.4 → 6.5 → 6.6 → 7.4). Task 3.4b is a contingency task kept in *Backlog*.

| ID | Task | Owner | Output | Predecessor(s) | Duration (working days) | Start | End | Accomplished when |
|---|---|---|---|---|---|---|---|---|
| **WP1** | **Setup & planning** | **Alexander** | | | | | | |
| 1.1 | Create repo and folder structure | Alexander | Repo with report/ status/ gantt/ references/ figures/ | — | 1 | 28/09/2026 | 28/09/2026 | The repository exists with the five required folders and all four members have push access. |
| 1.2 | Read brief and rubric | All | Shared notes on requirements | — | 1 | 29/09/2026 | 29/09/2026 | All members have read the Overview, Formal Requirements, BMC template and rubric, and open questions are listed. |
| 1.3 | README and repo conventions | Arseny | README.md + commit message convention | 1.1 | 1 | 05/10/2026 | 05/10/2026 | README.md describes the project, the repository structure and the commit message convention, and renders on the repo homepage. |
| 1.4 | Define scope, objectives and roles | All | Section 1 of project_plan.md | 1.2 | 1 | 05/10/2026 | 05/10/2026 | Project name, general objective, four specific objectives, milestones and roles are committed in project_plan.md and agreed by all members. |
| 1.5 | Draft Gantt v1 and risk analysis | Alexander | Draft task table, Gantt, risk matrix | 1.4 | 2 | 06/10/2026 | 07/10/2026 | The task table (owner, output, duration, predecessor, accomplished when, dates), the Gantt chart and the risk matrix are committed as a draft. |
| 1.6 | Set up Project Status document | Isaac | status/project_status.md | 1.5 | 1 | 08/10/2026 | 08/10/2026 | status/project_status.md lists every Gantt task with its owner, planned dates and current status. |
| 1.7 | Review, freeze and submit Gantt v1 | Alexander + Biel | Frozen v1 + git tag gantt-v1 | 1.5, 1.6 | 1 | 09/10/2026 | 09/10/2026 | Gantt v1 has been reviewed by a second member, frozen under the git tag gantt-v1, and the repository URL is submitted before 9 Oct, 22:00. |
| **WP2** | **Cause (B1)** | **Isaac** | | | | | | |
| **2.1** | Retrieve gene and protein records | Isaac | FASTA + records table (UniProt, NCBI, Ensembl) | 1.4 | 2 | 06/10/2026 | 07/10/2026 | Human GSN gene and plasma gelsolin protein sequences are stored as FASTA in the repo, with UniProt, NCBI and Ensembl IDs recorded in a table. |
| **2.2** | Collect pathogenic variant evidence | Isaac | Variant evidence table | 2.1 | 1 | 08/10/2026 | 08/10/2026 | A table lists the pathogenic GSN variants reported in UniProt, ClinVar and the literature, with position, amino acid change, phenotype and source. |
| **2.3** | Confirm D187N/D187Y and numbering convention | All | Justified selection + numbering note | 2.2 | 1 | 09/10/2026 | 09/10/2026 | D187N and D187Y are confirmed with a written justification, and the numbering convention (mature vs precursor) is stated and applied consistently. |
| 2.4 | Describe normal gelsolin function and domains | Isaac | Domain/function summary | 2.1 | 2 | 13/10/2026 | 14/10/2026 | The six gelsolin domains, their boundaries, Ca²⁺-dependent activation and actin-severing function are summarised with references. |
| **WP3** | **Structure (B2)** | **Alexander** | | | | | | |
| 3.1 | Select reference PDB structure | Alexander | Chosen PDB ID + selection rationale | 2.1 | 1 | 08/10/2026 | 08/10/2026 | One PDB entry is selected and its choice over alternatives is justified by resolution, coverage of domain G2 and Ca²⁺ state. |
| **3.2** | Map variants onto structure | Alexander | Figure: D187 location in G2 | 2.3, 3.1 | 2 | 13/10/2026 | 14/10/2026 | A figure in figures/ shows residue D187 on the reference structure, with domain G2 and the Ca²⁺-binding site labelled. |
| 3.3 | Search for experimental variant structures | Biel | List of available structures (or none) | 3.1 | 1 | 09/10/2026 | 09/10/2026 | The PDB search criteria and results for D187N/D187Y structures are documented, stating whether a usable experimental structure exists. |
| **3.4** | Compare WT vs variant structural environment | Alexander + Biel | Figure: Ca²⁺ site and contacts, WT vs variant | 3.2, 3.3 | 3 | 15/10/2026 | 19/10/2026 | A figure compares the WT and variant environment around residue 187 (Ca²⁺ coordination and residue contacts), and the differences are described in text. |
| 3.4b | Contingency: model variants in silico | Alexander | Mutated model in PyMOL | 3.3 | 2 | 13/10/2026 | 14/10/2026 | (Only if triggered) In silico D187N/D187Y models are generated in PyMOL, saved in the repo, and their limitations versus experimental data are stated. |
| **WP4** | **Patient impact (B3)** | **Biel** | | | | | | |
| 4.1 | Disease background and clinic | Biel | Background notes with refs | 1.4 | 3 | 06/10/2026 | 08/10/2026 | A referenced summary of the epidemiology, inheritance and clinical manifestations of GA is drafted, citing at least one recent review. |
| 4.2 | Pathway and pathophysiology | Biel | Description of the proteolytic cascade | 4.1 | 3 | 09/10/2026 | 14/10/2026 | The proteolytic cascade from the variant to amyloid deposition is described step by step, each step supported by a primary source. |
| **4.3** | Link variants to clinical phenotype | Biel + Isaac | Variant → mechanism → phenotype chain | 2.3, 3.4, 4.2 | 2 | 20/10/2026 | 21/10/2026 | For each variant, a variant → structural effect → mechanism → clinical phenotype chain is written and agreed by both owners. |
| **WP5** | **Evolution (B4)** | **Arseny** | | | | | | |
| 5.1 | Species selection and rationale | Arseny | Justification (Equus caballus + Mus musculus) | 1.4 | 1 | 05/10/2026 | 05/10/2026 | The choice of Equus caballus and Mus musculus is justified in writing in project_plan.md. |
| 5.2 | Retrieve orthologues | Arseny | FASTA of 3 orthologues | 2.1, 5.1 | 1 | 08/10/2026 | 08/10/2026 | Human, horse and mouse gelsolin sequences are stored as FASTA with accession numbers, and the selection criteria (isoform, review status) are noted. |
| 5.3 | Multiple sequence alignment | Arseny | MSA file + tool parameters | 5.2 | 2 | 09/10/2026 | 13/10/2026 | The MSA of the three orthologues is in the repo, with tool name, version and parameters documented. |
| 5.4 | Conservation of D187 and functional domains | Arseny + Alexander | Figure: annotated MSA | 2.3, 5.3 | 2 | 14/10/2026 | 15/10/2026 | A figure of the annotated MSA highlights position 187 and the functional domains, and percent identity per domain is reported in a table. |
| **WP6** | **Report** | **Biel** | | | | | | |
| 6.1 | Report skeleton in BMC format | Biel | report/report.md with sections | 1.1 | 1 | 06/10/2026 | 06/10/2026 | report/report.md contains every BMC section (Abstract to References), each with an assigned owner. |
| 6.2 | Annotated bibliography | Isaac | References list, primary vs secondary, commented | 4.1 | 3 | 09/10/2026 | 14/10/2026 | Every source in references/ is listed in Oxford SCIMED style with a one-line comment and a primary/secondary label. |
| 6.3 | Draft Background, Methods and preliminary Results | Each WP owner | Section drafts in report.md | 4.2, 5.4 | 3 | 16/10/2026 | 20/10/2026 | Background, Methods and preliminary Results are drafted in report.md by their owners and reviewed by one other member. |
| **6.4** | Final Results, Discussion, Abstract, Conclusions | All | Complete sections | 4.3, 6.3 | 2 | 22/10/2026 | 23/10/2026 | Results, Discussion and Conclusions are complete, the Abstract is under 350 words, and all members have approved them. |
| **6.5** | References format and Declarations | Isaac | Oxford SCIMED refs + Declarations | 6.4 | 1 | 26/10/2026 | 26/10/2026 | Every in-text citation matches the reference list in Oxford SCIMED style, and the Declarations section is complete. |
| **6.6** | Final cross-review (buffer) | All | Reviewed report, word count checked | 6.5 | 1 | 27/10/2026 | 27/10/2026 | The report passes the rubric checklist: ≤7 pages / 5000 words, ≤5 figures or tables stored in the repo, every claim cited. |
| **WP7** | **Project management** | **Alexander** | | | | | | |
| 7.1 | Status document updates | Isaac | Updated status table | 1.6 | 14 | 08/10/2026 | 28/10/2026 | The status document shows the real dates and status of every task and is updated at least twice a week. |
| 7.2 | Live Gantt updates | Alexander | Updated gantt_live | 1.7 | 12 | 13/10/2026 | 28/10/2026 | The live Gantt shows real start and end dates for every task at the end of each week. |
| 7.3 | Upload sources to references/ | All | PDFs in repo | — | 17 | 05/10/2026 | 28/10/2026 | Every source cited in the report has its PDF (or saved web page) in references/. |
| **7.4** | Final Gantt and retrospective gap analysis | Alexander | Final Gantt + v1 vs final analysis | 6.6 | 1 | 28/10/2026 | 28/10/2026 | The final Gantt with real dates is committed next to v1, together with a written analysis of the gaps and their causes. |
| **WP8** | **Defence (provisional, pending M6 date)** | **All** | | | | | | |
| 8.1 | Presentation support | All | Slides | 6.6 | 2 | 29/10/2026 | 30/10/2026 | Slides cover the main findings and every member presents one section. |
| 8.2 | Rehearsal 1 | All | Feedback notes | 8.1 | 1 | 03/11/2026 | 03/11/2026 | A full run-through is completed within the time limit and feedback is recorded. |
| 8.3 | Rehearsal 2 | All | Final timing | 8.2 | 1 | 04/11/2026 | 04/11/2026 | A second run-through is completed with feedback applied, and every member can answer questions on any section. |
---

## 3. Risk Analysis
