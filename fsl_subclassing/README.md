## Subclassifying Mitotic Figures

### Frederick Lee, M.D.

This folder contains the run Jupyter notebooks that show all 984 image patches (64 × 64 pixels) that were:

- Extracted from Aubreville _et al._'s whole slide images (WSI's) of canine breast tumors (published training Slides #2, 3, 5, 7, and 8); and,
- Hand-labeled into one of the 4 subclasses as described below.
- All ground-truth subclass labels for the selected image patches were exported to the included csv files via pandas along with their identifying metadata (center image coordinates, annotation ID, and GUID as given by the authors in their "MEL" sqlite database).
- The final distribution of hand-subclassed labels in our dataset (n = 984) were as follows:
  - Subclass 5 (Metaphase): 151 (15.3%)
  - Subclass 6 (Anaphase/Telophase): 73 (7.4%)
  - Subclass 7 (Abnormal Mitosis): 227 (23.1%)
  - Subclass 8 (Non-Mitosis): 533 (54.2%)

### Pathologic criteria used to subclassify mitotic figures (MFs) and "mitotic-like" (i.e., non-mitotic) figures (MLFs):\*

**Subclass label 5: Metaphase**

- Members represent mitotic figures (MFs) in metaphase, which includes:
  - **Prometaphase:** MFs exhibit darkly condensed, shortened, and thickened chromosomes with visible, protruding rods and spikes, which are arranged centrally and occasionally in a ring-like form without predominant central clearing.
  - **Metaphase:** MFs with condensed chromosomal material exhibiting protruding, irregular rods and spikes (as in prometaphase above) but arranged in a linear band ("metaphase plate") at the midline of the cell, which has been sectioned parallel to the microtubule spindle apparatus.
  - " **Rosette"** form: Metaphase MF as above, except the dividing cell has been sectioned perpendicular to the microtubule spindle apparatus, resulting in the thickened chromosomes being viewed "head-on." Instead of appearing as a linear band, they appear as a ring with distinct central clearing.

**Subclass label 6: Anaphase/Telophase**

- Members represent MFs in either of the last two stages of mitosis:
  - **Anaphase:** Condensed chromosomes appear as two distinct aggregates, separated by variable distance, as the mitotic cell progresses toward the formation of daughter nuclei/cells. This stage is often difficult to distinguish clearly from telophase (below).
  - **Telophase:** This last stage of mitosis is characterized by separation of two chromosomal clusters at opposing poles of the cell, which now exhibits the formation of a midline of "cleavage furrow"—a contractile ring which "pinches" the cell membrane and cytoplasm down the middle, generating two fully separated daughter cells.

**Subclass label 7: Abnormal mitosis (atypical mitotic figure or AMF)**

- These MFs represent a diverse array of **atypical (abnormal) mitotic figures (AMFs),** in which derangements of the normal mitotic process result in a grossly abnormal distribution of chromosomal material to daughter cells. Examples include:
  - **Tri- or multi-polar AMF:** Formation of ≥ 3 chromosomal clusters instead of the normal two.
  - **Chromosome lagging or bridging AMF:** During anaphase/telophase, one or more chromosomes (or fragments) "lag" behind the main cluster of chromosomes, or alternatively, bridge the gap between the two separating chromosomal clusters.
  - **Asymmetric AMF:** During anaphase, chromosomes separate into unequal clusters.

**Subclass label 8: Non-mitotic ("mitotic-like") figures (MLFs)**

- These represent non-dividing cells, which for a variety of reasons, may resemble true MFs. Key identifying features are:
  - Smooth nuclear contour (in contrast to the protruding rods and spikes seen in MFs);
  - Eosinophilic (pink) cytoplasm (characteristic of dying cells); and,
  - Tissue context (e.g., cell appears in a degenerating area of tumor tissue).
- Examples of MLFs include:
  - Inflammatory cells such as polymorphonuclear leukocytes, which exhibit multi-lobed nuclei, or eosinophils, which possess bilobed nuclei.
  - Dying/degenerating cells e.g., in necrotic areas of tumor or cells undergoing apoptosis (programmed cell death). These exhibit thickened, condensed chromosomal material in the nucleus with smooth contours (pyknosis), followed by karyorrhexis, which is the final destructive fragmentation of the nuclear chromatin in a scattered distribution across the cytoplasm.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*Modified from Donovan _et al.__Mitotic Figures—Normal, Atypical and Imposters: A Guide to Identification. Veterinary Pathology_ **58** (2):243-257, 2021.