# Gantt (live) with retrospective analysis

Last update: 26/10/2026, 21:00, checked against the commit history of `main`. Bars without colour in WP8 are pending (oral defence, dates to confirm).

Final version of the Gantt chart, reflecting the **real** development of the project up to the delivery on **26/10/2026 at 22:00**. Real dates come from the commit history and from [`status/project_status.md`](../status/project_status.md). The frozen plan submitted on 9 October is in [`gantt_v1.md`](gantt_v1.md).

Weekends are **not** excluded in this version, because a significant part of the work was done on Saturday 24 and Sunday 25 October. Grey bars are completed, red bars mark incidents (periods in which a planned activity did not happen) and bars with a red outline belong to the critical path.

```mermaid
gantt
    title 12DP-C · Gelsolin Amyloidosis · Final Gantt (real dates)
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    tickInterval 1week
    todayMarker off

    section WP1 Setup and planning
    1.1 Repo and folders (Alexander)                 :done, t11, 2026-09-14, 1d
    1.2 Read brief and rubric (All)                  :done, t12, 2026-09-14, 4d
    1.3 README and conventions (Arseniy)             :done, t13, 2026-09-17, 23d
    1.4 Scope, objectives, roles (All)               :done, t14, 2026-10-05, 4d
    1.5 Gantt and risk draft (Alexander, Biel)       :done, t15, 2026-09-28, 12d
    1.6 Status document (Isaac) · late               :done, t16, 2026-10-09, 1d
    1.7 Review and submit v1 (Alexander + Biel)      :done, t17, 2026-10-09, 1d

    section WP2 Cause
    2.1 Gene and protein records (Isaac) · late      :crit, done, t21, 2026-10-19, 1d
    2.2 Variant evidence (Isaac) · late              :crit, done, t22, 2026-10-24, 2d
    2.3 Confirm variant and numbering (All)          :crit, done, t23, 2026-10-19, 6d
    2.4 Normal function (Isaac)                      :done, t24, 2026-10-24, 2d

    section WP3 Structure
    3.1-3.3 Canceled, replaced by teaching-team report :t31, 2026-10-13, 0d
    3.4 Compare WT vs D187N (Biel)                   :crit, done, t34, 2026-10-25, 1d
    3.4b Backup PyMOL models (canceled)              :t34b, 2026-10-13, 0d
    3.5 AlphaFold superposition human-mouse (Alexander) :done, t35, 2026-10-26, 1d

    section WP4 Patient impact
    4.1 Disease background (Isaac, from Biel)        :done, t41, 2026-10-25, 1d
    4.2 Pathophysiology (Isaac, from Biel)           :done, t42, 2026-10-25, 1d
    4.3 Variant to symptoms (Isaac, from Biel)       :crit, done, t43, 2026-10-25, 1d

    section WP5 Evolution
    5.1 Choose species (Biel, from Arseniy)          :done, t51, 2026-10-15, 1d
    5.2 Get orthologues (Biel, from Arseniy)         :done, t52, 2026-10-15, 1d
    5.3 Alignments (Arseniy)                         :done, t53, 2026-10-19, 7d
    5.4 Conservation of D187 (Arseniy, Isaac)        :done, t54, 2026-10-25, 2d

    section WP6 Report
    6.1 Report skeleton (Biel, then Isaac in BMC format) :done, t61, 2026-09-17, 39d
    6.2 Bibliography (Isaac)                         :done, t62, 2026-10-24, 2d
    6.3 First drafts (WP leads)                      :done, t63, 2026-10-24, 3d
    6.4 Results, Discussion, Abstract, Conclusions (All) :crit, done, t64, 2026-10-26, 1d
    6.5 References, Abbreviations, Declarations (Isaac) :crit, done, t65, 2026-10-25, 2d
    6.6 Final review 18h-21h (All)                   :crit, done, t66, 2026-10-26, 1d

    section WP7 Project management
    7.1 Status updates (Isaac) · first version       :done, t71a, 2026-10-09, 1d
    7.1 Status not updated · incident                :crit, t71g, 2026-10-10, 14d
    7.1 Status updates (Isaac) · resumed             :done, t71b, 2026-10-24, 3d
    7.2 Live Gantt not updated · incident            :crit, t72, 2026-10-10, 16d
    7.3 Sources to references/ (Isaac)               :done, t73, 2026-10-24, 3d
    7.4 Final Gantt and retrospective (Alexander)    :crit, done, t74, 2026-10-26, 1d

    section WP8 Defence (dates to confirm)
    8.1 Slides (All)                                 :t81, 2026-10-29, 2d
    8.2 Rehearsal 1 (All)                            :t82, 2026-11-03, 1d
    8.3 Rehearsal 2 (All)                            :t83, 2026-11-04, 1d

    section Milestones
    M1 Gantt v1 submitted                            :milestone, m1, 2026-10-09, 0d
    M4 Status review                                 :milestone, m4, 2026-10-22, 0d
    M2 Variant and numbering agreed (planned 09/10)  :milestone, m2, 2026-10-24, 0d
    M3 Main analyses done (planned 19/10)            :milestone, m3, 2026-10-26, 0d
    M5 Final delivery 26/10 22h (v1 said 28/10)      :milestone, m5, 2026-10-26, 0d
```

## Retrospective analysis: Gantt v1 vs final

### 1. Main deviations

| Area | Planned (v1) | Real | Cause |
|---|---|---|---|
| Final delivery | 28/10, with buffer day 27/10 | **26/10, 22:00** | v1 used a wrong deadline. Detected on 24/10 (new risk R8): tasks 6.4–7.4 were compressed into 24–26/10 and the buffer day was lost. |
| WP2 Cause (critical path) | 30/09–09/10 | 19/10–26/10 | Gene records (2.1) were done on 19/10 but stayed on a personal branch until 25/10, so the rest of the team did not see them. |
| WP3 Structure | Own PDB selection and comparison, 13/10–19/10 | Structural report provided by the teaching team, interpreted on 25/10; a human–mouse AlphaFold superposition (3.5) was added on 26/10 | Tasks 3.1–3.3 were replaced by the teaching-team report, so the backup task 3.4b was canceled (risk R1 closed without materialising). |
| WP4 Patient impact | Biel, 30/09–21/10 | Isaac, 24/10–26/10 | Reassigned by agreement with Biel. |
| WP5 Evolution | Arseniy, 06/10–16/10 | Species chosen by Biel on 15/10; alignments by Arseniy 19/10–26/10 | Species selection was done by Biel instead of Arseniy. The fly (*Drosophila melanogaster*) was retrieved but officially removed from the aims, the analysis and the structural comparison on 26/10, so the comparison covers horse and mouse only. |
| WP6 Report | Drafts 16/10–20/10, final 22/10–23/10 | Almost all writing on 24/10–26/10, including the weekend | Accumulated delays in WP2–WP5 and the deadline error. |
| WP7 Management | Status twice a week; live Gantt weekly | Status and live Gantt not updated between 09/10 and 24/10 | Recorded as incidents in the status document (7.1, 7.2). |

### 2. What worked

- **Risk analysis.** R2 (187/214 numbering) materialised and was mitigated as planned with a conversion table (`files/data/residue_numbering.md`); R8 (deadline mismatch) was detected and handled by re-planning. R1 (no variant structure) did not materialise, and the backup task 3.4b was canceled.
- **Critical path.** Identifying it helped us prioritise WP2 → WP3 → WP4 → WP6 when the schedule had to be compressed.
- **Version control.** Each member worked on a personal branch and merged through pull requests with merge commits, keeping a traceable history.

### 3. What did not work, and lessons learned

1. **Verify official deadlines against the course documents** before planning. The wrong deadline removed our buffer.
2. **Fix the scientific question early.** Until the mechanism (loss of the Ca²⁺-binding site in G2) was clear, tasks were executed as isolated steps; once it was clear, the analysis and the writing converged quickly.
3. **Merge personal branches frequently.** Work that stays on a branch is invisible to the team and to the contribution graph.
4. **Keep the live Gantt and the status document updated weekly**, so that delays are detected as they happen and not at the end.
5. **Distribute the workload over time.** To reduce the risk of errors and limited the time for review.
