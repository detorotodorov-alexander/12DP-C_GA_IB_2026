# Molecular basis of Gelsolin Amyloidosis: structural and comparative analysis of the pathogenic *GSN* variant D187N

Alexander, Arseniy, Biel, Isaac

*Introduction to Bioinformatics, Universitat Politècnica de Catalunya (UPC), Barcelona, Spain*

<!--
Format rules (BMC template):
- Max 7 pages or 5000 words (whichever is shorter). References do not count.
- Max 5 figures or tables in total, stored in files/figures/.
- Abstract max 350 words, structured (Background, Results, Conclusions).
- In-text citations: (Author year) / (Author et al. year); list alphabetical, Oxford style.
- UK spelling with -ize; Oxford comma; define abbreviations at first mention.
- Residue numbering: mature numbering (D187N); see files/data/residue_numbering.md.
-->

## Abstract

**Background:** *TO DO (All, at the end).*

**Results:** *TO DO (All, at the end).*

**Conclusions:** *TO DO (All, at the end).*

## Keywords

Gelsolin, amyloidosis, *GSN*, D187N, calcium binding, protein structure, sequence alignment

## Background

### Gelsolin amyloidosis: clinical picture and epidemiology
Familial amyloidosis of Finnish type (FAF), also known as Meretoja syndrome or gelsolin (AGel) amyloidosis, is a rare hereditary systemic amyloidosis first described in Finnish families in 1969 (Solomon *et al.* 2012). It belongs to the Finnish disease heritage: most patients come from two geographical clusters in south-eastern Finland, where approximately 1000 carriers are estimated, although patients without Finnish ancestry have been reported in many countries, including Spain, Japan, the United States, Denmark, and the Czech Republic, which suggests several independent founders (Solomon *et al.* 2012). The disease is inherited in an autosomal dominant manner, and homozygous patients present an earlier and more severe phenotype, with prominent kidney involvement (Solomon *et al.* 2012, OMIM #105120). As with most rare diseases, it is probably underdiagnosed (Solomon *et al.* 2012).

The first sign, usually appearing between the third and fourth decade of life, is corneal lattice dystrophy caused by amyloid deposition in the cornea (Solomon *et al.* 2012, OMIM #105120). As the disease progresses, amyloid affects cranial and peripheral nerves, producing a slowly progressive polyneuropathy: paresis of the facial nerve, starting in its upper branch, is almost universal, and involvement of other cranial nerves leads to reduced corneal sensitivity, dysarthria, and tongue atrophy, while a mainly sensory peripheral neuropathy and autonomic dysfunction may also develop (Solomon *et al.* 2012). Deposition in the skin causes cutis laxa which, together with facial paresis, gives the face a characteristic drooping, mask-like appearance. In later stages, proteinuria and cardiac conduction abnormalities may appear (Solomon *et al.* 2012). There is currently no treatment targeting the cause of the disease, and management is symptomatic, including eye lubrication, control of secondary glaucoma, and reconstructive facial surgery (Solomon *et al.* 2012).

### The *GSN* gene and the disease-associated variant
Gelsolin is encoded by the *GSN* gene, located on human chromosome 9 (9q33.2; RefSeq NM_000177.5). The gene produces an intracellular (cytoplasmic) and a secreted (plasma) isoform, both composed of six domains (Chen *et al.* 2001). The plasma isoform carries an N-terminal signal peptide of 27 residues that is removed during secretion (UniProt P06396). The sequence analysed in this project corresponds to the plasma gelsolin precursor (NP_000168.1, 782 residues).

The variant assigned to our team is a single nucleotide substitution, c.640G>A, which replaces an aspartate with an asparagine (p.Asp214Asn in precursor numbering). In this report we use the numbering of the mature protein, standard in the gelsolin literature, in which the variant is named **D187N** (mature position = precursor position − 27; see `files/data/residue_numbering.md`). D187N was the first mutation identified as the cause of hereditary gelsolin amyloidosis, also called familial amyloidosis of Finnish type (FAF) or Meretoja syndrome (Maury *et al.* 1990). The disease is inherited in an autosomal dominant manner (OMIM #105120).

### Normal function of gelsolin
Gelsolin is a calcium-regulated actin-binding protein formed by six homologous domains (G1–G6) (Nag *et al.* 2013). In the absence of Ca²⁺ the protein adopts a compact, inactive conformation; Ca²⁺ binding induces large conformational changes that expose its actin-binding surfaces, allowing gelsolin to sever actin filaments, cap their growing ends and sequester actin monomers (Nag *et al.* 2013). Plasma gelsolin circulates in the blood as part of the actin-scavenging system, which removes actin filaments released from damaged cells (Chen *et al.* 2001, Solomon *et al.* 2012). Ca²⁺ binding does not only activate gelsolin: it also stabilizes the fold of individual domains, which is central to the disease mechanism described below (Kazmirski *et al.* 2002).

### From the D187N variant to amyloid formation
D187 is located in domain G2 (residues 151–266), where its side chain forms part of a metal-binding site that corresponds to one of the two Ca²⁺-binding sites required for the activation of gelsolin and is essential for the stability of G2 (Kazmirski *et al.* 2002). Aspartate carries a negatively charged carboxylate group that coordinates the positive Ca²⁺ ion; asparagine has a side chain of almost identical size but no charge, so the substitution removes this electrostatic interaction without requiring a large change in the protein backbone. As a consequence, D187N disrupts Ca²⁺ binding in G2, and the domain becomes unstable when gelsolin is activated by Ca²⁺ (Kazmirski *et al.* 2002).

This loss of stability triggers an abnormal two-step proteolysis. First, in the trans-Golgi network, the destabilized G2 domain is cleaved between residues 172 and 173 by the protease furin, producing a secreted 68 kDa C-terminal fragment (C68) (Chen *et al.* 2001). Wild-type gelsolin escapes this cleavage because Ca²⁺ binding stabilizes G2 (Chen *et al.* 2001). Second, outside the cell, C68 is cleaved after residue 243 by the membrane metalloprotease MT1-MMP, releasing an 8 kDa fragment (residues 173–243) and a minor 5 kDa fragment (residues 173–225) that aggregate into amyloid fibrils (Chen *et al.* 2001, Page *et al.* 2005).

The resulting amyloidogenic fragments deposit systemically in tissues, which explains the clinical manifestations of the disease described above. Because a single mutant allele is sufficient to cause the disease with apparently complete penetrance, whereas gelsolin knockout mice show only a mild phenotype, gelsolin amyloidosis is considered a gain-of-toxic-function disease rather than the consequence of losing normal gelsolin activity (Solomon *et al.* 2012).

### Aims of this study
*TO DO (All): general objective (formal infinitive statement) and specific objectives.*

## Results

### Sequence comparison of wild-type and D187N gelsolin
Looking at the sequence alignment of human WT CDS vs the mutant CDS (see `files/data/Human WT - Human mutant CDS alignment.txt`
), it can be seen that the only difference between the 2 sequences is a single missense nucleotide substitution from guanine to adenine (c.640G>A). This substitution affects the formation of the protein by changing the codon GAC, which codes for the amino acid aspartate, into AAC, which codes for asparagine (p.Asp214Asn) (see `files/data/Human WT protein - Human mutant protein alignment.txt`). This mutation is labelled as D187N using the numbering of the mature protein, which can be figured out by subtracting 27 from the position of the precursor (214). (*TO DO (Arseniy): WT vs mutant CDS and protein alignments (c.640G>A, p.Asp214Asn / D187N).*

### Structural comparison of wild-type and D187N gelsolin
*TO DO (Alexander, Biel): local and global RMSD, chemical change Asp→Asn, Ca²⁺-binding site in domain G2.*

### Comparison of human gelsolin with other species
To look at the nature of the disease from an evolutionary perspective, we have chosen 2 homologs to compare to the human WT CDS and protein sequences, which are the horse (equus caballus) and the mouse (mus musculus). We have chosen these 2 homologs in particular as they share a great amount of their genes (around 90%) in common with humans and have high sequence conservation in regions related to the coding of proteins (Max Plank Society, 2026). *TO DO (Arseniy, Alexander): horse (mandatory), mouse and fly; identity, conservation of D187 and domain G2; human–horse structural superposition.*

## Discussion

*TO DO (All): integrate sequence, structure, function and clinical consequences; compare with literature; limitations (e.g. predicted structures do not model Ca²⁺).*

## Conclusions

*TO DO (All).*

## Methods

### Data sources
*TO DO (Isaac, Arseniy): UniProt, NCBI (RefSeq, Gene), Ensembl, PDB, OMIM; accessions and selection criteria.*

### Sequence alignment
The main tool used for sequence matching and sequence alignment is the BLAST (Basic Local Alignment Search Tool) website provided by the National Center for Biotechnology Information (NCBI). BLAST helps analyze and find regions of similarity between different biological sequences. 

Search parameters:

For all the human and homolog nucleotide sequences, the database used was the core nucleotide database (core nt). We specifically optimized for highly similar sequences (megablast).

For all the human and homolog protein sequences, the database used was the the reference proteins database (refseq protein). We used the blastp (protein-protein BLAST) algorithm. *TO DO (Arseniy): tools, parameters (BLASTn/BLASTp, etc.).*

### Structural analysis
*TO DO (Alexander): structures used, superposition, RMSD.*

## Abbreviations

*TO DO (All): add every abbreviation used, e.g. AGel: gelsolin amyloidosis; CDS: coding DNA sequence; MT1-MMP: membrane-type 1 matrix metalloproteinase; RMSD: root-mean-square deviation; WT: wild type.*

## Declarations

**Availability of data and materials:** All data, scripts, figures and sources are available in the project repository: https://github.com/detorotodorov-alexander/12DP-C_GA_IB_2026

**Authors' contributions:** *TO DO (Isaac, at the end).*

## References

Chen CD, Huff ME, Matteson J *et al.* Furin initiates gelsolin familial amyloidosis in the Golgi through a defect in Ca²⁺ stabilization. *EMBO J* 2001;**20**:6277–87.

Kazmirski SL, Isaacson RL, An C *et al.* Loss of a metal-binding site in gelsolin leads to familial amyloidosis–Finnish type. *Nat Struct Biol* 2002;**9**:112–6.

Maury CP, Kere J, Tolvanen R *et al.* Finnish hereditary amyloidosis is caused by a single nucleotide substitution in the gelsolin gene. *FEBS Lett* 1990;**276**:75–7.

Nag S, Larsson M, Robinson RC *et al.* Gelsolin: the tail of a molecular gymnast. *Cytoskeleton* 2013;**70**:360–84.

Online Mendelian Inheritance in Man. #105120 Amyloidosis, Finnish type. https://omim.org/entry/105120 (25 October 2026, date last accessed).

Page LJ, Suk JY, Huff ME *et al.* Metalloendoprotease cleavage triggers gelsolin amyloidogenesis. *EMBO J* 2005;**24**:4124–32.

Solomon JP, Page LJ, Balch WE *et al.* Gelsolin amyloidosis: genetics, biochemistry, pathology and possible strategies for therapeutic intervention. *Crit Rev Biochem Mol Biol* 2012;**47**:282–96.

The UniProt Consortium. Gelsolin (GELS_HUMAN), UniProtKB P06396. https://www.uniprot.org/uniprotkb/P06396 (25 October 2026, date last accessed).

“Why Do Researchers Investigate Mice?” Max Planck Society, https://www.mpg.de/10973923/why-do-scientists-investigate-mice. (26 October 2026, date last accessed).
