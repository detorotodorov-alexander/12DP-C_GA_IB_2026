# Human GSN / Gelsolin Database Identifiers (Task 2.1)

### Official Records Table

| Database | Record Type | Identifier / Accession | Version | Description / Notes |
|---|---|---|---|---|
| **UniProtKB / Swiss-Prot** | Protein (Reviewed) | `P06396` (`GELS_HUMAN`) | Canonical | Plasma gelsolin precursor (782 aa), contains 27-aa N-terminal signal peptide. |
| **NCBI Gene** | Gene entity | `2934` | Current | *GSN* (gelsolin), chromosomal location: 9q33.2. |
| **NCBI RefSeq** | mRNA transcript | `NM_000177.5` | Transcript variant 1 | Encodes the longer plasma isoform precursor. |
| **NCBI RefSeq** | Protein sequence | `NP_000168.1` | Isoform 1 precursor | Corresponds to 782 aa plasma precursor. |
| **Ensembl** | Gene | `ENSG00000148180` | Canonical | *GSN* locus. |
| **Ensembl** | Transcript (MANE Select) | `ENST00000432226.7` | MANE Select | Matches NM_198252.3 / NP_937895.1 (cytoplasmic isoform, 731 aa). |

---

### Rationale for Sequence Selection (Database Literacy)

Human gelsolin is expressed in two primary isoforms through alternative splicing and promoters:
1. **Cytoplasmic gelsolin** (731 aa): Intracellular isoform lacking a signal peptide, involved in cytosolic actin remodeling.
2. **Plasma gelsolin** (782 aa precursor / 755 aa mature): Secreted isoform containing an N-terminal 27-amino-acid signal peptide (`Met1–Ala27`), functioning in extracellular actin filament clearance.

**Selection criteria:** We selected the canonical plasma isoform (`P06396` / `NP_000168.1` / `NM_000177.5`) because Gelsolin Amyloidosis (FAF / Meretoja disease) is an extracellular, systemic amyloidosis. Aberrant proteolysis of mutant gelsolin occurs specifically during secretion and within the extracellular matrix/plasma, yielding circulating 8 kDa amyloidogenic fragments. Consequently, the plasma precursor sequence is the biologically accurate reference for modeling pathological cleavage, structural disruption, and sequence conservation.
