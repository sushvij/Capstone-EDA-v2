# NIGHTINGALE - A DECISION SUPPORT SYSTEM FOR PATHOLOGISTS
BACKGROUND
One aspect of grading cancers in patients is to understand the number of mitotic cells. While these don't determine the diagnosis of cancer, they do influence it through grading decisions. 
Counting mitotic cells is a manually intensive and subjective process. There is a lot of grey area based on the stage of mitotic development a cell may be undergoing.
In this repository, we examine the breast tissue samples (svs files) and the related sqlite files of canines where experts have manually labelled cells as mitotic or not. Further baseline models have been developed by researchers to have an AI do this determination.

CURRENT REPOSITORY
This repository currently contains our Exploratory Data Analysis. And, branches will be created to add more outputs as they are developed.
Given the dataset is too large for a free github repository, this repository currently focuses on jupyter notebooks with outputs. The #data lineage.jpg 
file contains the details of the sources and types of data.
Please see the outputs within the jupyter notebooks.
Start with databaseStatistics.ipynb in the main directory for a high level understanding of the data. And, then for a deeper dive into a particular sample, look at the Google colab notebook maub_eda_v2_present_xcc_fsl.ipynb.
Note running any cell will not work as the dataset has to be stored locally elsewhere.

VIEWING PRO TIP FOR THE CURRENT REPOSITORY
Because the notebooks themselves contain images, we recommend making a local copy of this repository and then opening the Jupyter Notebook locally.

FURTHER DEVELOPMENT
As the team progresses you will find more branches created from this repository containing various AI models and developmental work towards a decision support system for pathologists. For example, you can get a sneak peek at how our resident expert, Dr. Frederick, is reclassifying the mitotic figures by stages to build a more sophisticated AI. #See image.png.

Come back again and join us on this journey!

Warmly,
Sush, Frederick and Rajiv
