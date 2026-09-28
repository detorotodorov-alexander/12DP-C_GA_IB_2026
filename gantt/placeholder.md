```mermaid
gantt
    title Disease Project – Gantt v1
    dateFormat YYYY-MM-DD
    excludes weekends, 2026-10-12
    section WP1 Setup
    1.1 Repo + folders (Arseniy)      :done, t11, 2026-09-28, 2d
    1.2 Sources per block (all)       :t12, after t11, 4d
    section WP2 Cause (B1)
    2.1 Gene, protein, UniProt (Isaac):t21, 2026-10-01, 4d
    2.2 Choose variants (all)         :crit, t22, after t21, 2d
    section WP3 Structure (B2)
    3.1 Get PDB/AlphaFold (Alexander) :t31, after t22, 2d
    3.2 Map variants in 3D (Alexander):t32, after t31, 3d
    section Milestones
    Gantt delivered                   :milestone, m1, 2026-10-09, 0d
    Repo freeze                       :milestone, m2, 2026-10-26, 0d
```
