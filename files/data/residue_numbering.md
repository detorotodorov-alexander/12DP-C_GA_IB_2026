# Residue numbering conversion (mitigation of risk R2)

Human gelsolin is numbered in two ways in the literature and in databases:

- **Precursor numbering** (UniProt P06396, NCBI NP_937895.1, our FASTA files, HGVS nomenclature): counts from the initiator methionine, including the 27-residue signal peptide.
- **Mature numbering** (most clinical and structural papers, PDB structures): counts from the first residue of secreted plasma gelsolin, after removal of the signal peptide.

**Conversion: mature position = precursor position − 27.**

**Convention adopted in this project:** the report uses **mature numbering** (D187N), because it is the standard in the gelsolin amyloidosis literature. The precursor equivalent is given at first mention, e.g. "D187N (p.Asp214Asn in precursor numbering; c.640G>A)".

| Feature | Precursor numbering | Mature numbering | Residue (human WT) | Source to cite |
|---|---|---|---|---|
| Signal peptide | 1–27 | — | — | UniProt P06396 |
| First residue of mature plasma gelsolin | 28 | 1 | A | UniProt P06396 |
| **Assigned variant (Finnish type, AGel)** | **D214N** (c.640G>A) | **D187N** | D → N | Provided FASTA files; literature |
| Other variant at the same position | D214Y | D187Y | D → Y | Literature |
| Furin cleavage site (Golgi) | after R199 | after R172 | R | Literature |
| N-terminus of the amyloidogenic 8 kDa / 5 kDa fragments | 200 | 173 | A | Literature |
| C-terminus of the 8 kDa fragment (MT1-MMP cleavage) | 270 | 243 | M | Literature |

Residue identities in the table were checked against `GA_protein_WT.fasta` (24/10/2026). Literature positions must be checked against the cited papers before the final review (task 6.6).

**Horse (*Equus caballus*, NP_001075422.1):** the record lacks the N-terminal region (signal peptide included). In the teaching-team structural alignment it starts at human precursor position 54, with no internal gaps, and **D214 (D187) is conserved**. Horse residue numbers therefore differ from both human numberings; always refer to the aligned human position.
