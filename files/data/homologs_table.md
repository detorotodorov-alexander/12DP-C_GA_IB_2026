# GSN homologs selected (Lab P5, Session 1)

Query sequences: provided human WT CDS (2349 nt) and protein (782 aa, plasma gelsolin precursor).
Searches: NCBI BLASTn (nr/nt) and BLASTp (refseq_protein), restricted by organism. Curated RefSeq (NM_/NP_) entries were prioritised.

| Species | Gene | CDS accession (coordinates) | Protein accession | Curated | Length | BLASTp query cover / identity / E-value |
|---|---|---|---|---|---|---|
| *Mus musculus* | Gsn | NM_146120.4 (85..2427) | NP_666232.2 | Yes | 780 aa / 2343 nt | 97% / 93.54% / 0.0 |
| *Equus caballus* | GSN | NM_001081953.1 (10..2205) | NP_001075422.1 | Yes | 731 aa / 2196 nt | 93% / 94.66% / 0.0 |
| *Drosophila melanogaster* | Gel | NM_080126.4 (320..2716) | NP_524865.2 | Yes | 798 aa / 2397 nt | 99% / 37.12% / 5e-147 |

## Selection rationale

- **Mouse:** curated gelsolin isoform 1 *precursor* (signal peptide present, equivalent to human plasma gelsolin); same length as reviewed UniProt entry P13020. Shorter isoforms 2 and 3 (731 and 742 aa) lack the N-terminal region and correspond to cytoplasmic forms; XP_ isoform X1 is non-curated.
- **Horse:** only curated RefSeq gelsolin for *E. caballus* (matches reviewed UniProt Q28372). It lacks the N-terminal region including the signal peptide (query cover 93%) but fully covers domain G2 and the position equivalent to human D214. The predicted isoform X1 (XP_023484372.2, 871 aa) was rejected: non-curated and with an 89-residue extension absent from human and mouse gelsolin.
- **Fly:** isoform B is annotated in UniProt (Q07171-1) as the secreted isoform with a predicted signal peptide (residues 1–28), the counterpart of human plasma gelsolin; it also had the highest BLASTp score. Isoform L corresponds to the cytoplasmic form.
- Other hits (scinderin, villin, advillin, flightless-I, quail, supervillin) belong to the gelsolin superfamily but are **paralogs**, not gelsolin orthologs, and were excluded.

## Checks performed
Each CDS was verified to start with ATG, end with a stop codon, have length (aa + 1) × 3, and translate exactly into its protein.
