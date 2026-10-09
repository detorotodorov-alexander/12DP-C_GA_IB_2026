# Gantt (live)

Updated at the end of every week with the real dates (task 7.2). It starts as a copy of [`gantt_v1.md`](gantt_v1.md); at the end of the project we compare both (task 7.4).

Last update: 09/10/2026

```mermaid
gantt
    title 12DP-C · Gelsolin Amyloidosis · live Gantt
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    excludes weekends, 2026-10-12
    todayMarker off

    section WP1 Setup and planning
    1.1 Repo and folders (Alexander)            :t11, 2026-09-28, 1d
    1.2 Read brief and rubric (All)             :t12, 2026-09-28, 2d
    1.3 README and conventions (Arseniy)        :t13, 2026-09-29, 2d
    1.4 Scope, objectives, roles (All)          :t14, 2026-10-05, 1d
    1.5 Gantt and risk draft (Alexander)        :t15, 2026-09-30, 3d
    1.6 Status document (Isaac)                 :t16, 2026-10-01, 2d
    1.7 Review and submit v1 (Alexander + Biel) :t17, 2026-10-09, 1d

    section WP2 Cause
    2.1 Gene and protein records (Isaac)        :crit, t21, 2026-09-30, 4d
    2.2 Variant evidence (Isaac)                :crit, t22, 2026-10-06, 3d
    2.3 Confirm variants (All)                  :crit, t23, 2026-10-09, 1d
    2.4 Normal function (Isaac)                 :t24, 2026-10-13, 2d

    section WP3 Structure
    3.1 Choose PDB structure (Alexander)        :t31, 2026-10-13, 1d
    3.3 Look for variant structures (Biel)      :t33, 2026-10-09, 1d
    3.2 Map variants (Alexander)                :crit, t32, 2026-10-14, 1d
    3.4b Backup in-silico models (Alexander)    :t34b, 2026-10-13, 2d
    3.4 Compare WT vs variant (Alexander + Biel):crit, t34, 2026-10-15, 3d

    section WP4 Patient impact
    4.1 Disease background (Biel)               :t41, 2026-09-30, 5d
    4.2 Pathophysiology (Biel)                  :t42, 2026-10-07, 5d
    4.3 Variant to symptoms (Biel + Isaac)      :crit, t43, 2026-10-20, 2d

    section WP5 Evolution
    5.1 Choose species (Arseniy)                :t51, 2026-10-06, 2d
    5.2 Get orthologues (Arseniy)               :t52, 2026-10-08, 2d
    5.3 Alignment (Arseniy)                     :t53, 2026-10-13, 2d
    5.4 Conservation of D187 (Arseniy + Alexander):t54, 2026-10-15, 2d

    section WP6 Report
    6.1 Report skeleton (Biel)                  :t61, 2026-10-05, 1d
    6.2 Bibliography (Isaac)                    :t62, 2026-10-09, 3d
    6.3 First drafts (WP leads)                 :t63, 2026-10-16, 3d
    6.4 Final sections (All)                    :crit, t64, 2026-10-22, 2d
    6.5 References format (Isaac)               :crit, t65, 2026-10-26, 1d
    6.6 Final review (All)                      :crit, t66, 2026-10-27, 1d

    section WP7 Project management
    7.1 Status updates (Isaac)                  :t71, 2026-10-01, 19d
    7.2 Live Gantt updates (Alexander)          :t72, 2026-10-13, 12d
    7.3 Sources to references/ (All)            :t73, 2026-09-28, 22d
    7.4 Final Gantt and review (Alexander)      :crit, t74, 2026-10-28, 1d

    section WP8 Defence (dates to confirm)
    8.1 Slides (All)                            :t81, 2026-10-29, 2d
    8.2 Rehearsal 1 (All)                       :t82, 2026-11-03, 1d
    8.3 Rehearsal 2 (All)                       :t83, 2026-11-04, 1d

    section Milestones
    M1 live Gantt submitted          :milestone, m1, 2026-10-09, 0d
    M2 Variants agreed             :milestone, m2, 2026-10-09, 0d
    M3 Main analyses done          :milestone, m3, 2026-10-19, 0d
    M4 Status review               :milestone, m4, 2026-10-22, 0d
    M5 Repo frozen                 :milestone, m5, 2026-10-28, 0d
```
