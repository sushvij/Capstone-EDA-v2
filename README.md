# NIGHTINGALE - A DECISION SUPPORT SYSTEM FOR PATHOLOGISTS

## BACKGROUND
One aspect of grading cancers in patients is to understand the number of mitotic cells. While these don't determine the diagnosis of cancer, they do influence it through grading decisions. 

The challenge is that counting mitotic cells is a manually intensive and subjective process. Moreover, a pathologist may see as many as 100-300 images a day causing significant fatigue and ultimately burnout. There is a lot of grey area on classification based on the stage of mitotic development a cell may be undergoing, causing further complications. In summary, a toilsome and faulty process.

Enter AI.

In this repository, we build AI models to classify the breast tissue samples (svs files) and the related sqlite files of canines where experts have manually labelled cells as mitotic or not. Further [prior research](https://github.com/DeepPathology/MITOS_WSI_CCMCT) has been developed to have an AI do this determination of "mitotic" or "not mitotic"; this reasearch has been the basis of our understanding.

## LIMITATIONS OF MODEL, DATA AND MACHINE LEARNING PIPELINE

Limitations of our model are similar to the multiple breast cancer classfication models examined in detail in [A Comprehensive Survey on Deep-Learning-Based Breast Cancer Diagnosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8656730/). Specifically, ResNet models such as ours use only patch level images to train the model vs whole slide images and experience an imbalance in classes that needs to be accounted. Additionally, they consume a lot of computing power.

A limitation of the data is that it is canine tissue samples and ultimately the desire is to make inferences on human breast cancer diagnosis. This is a significant roadblock in generalizability which is a current and important challenge in the field of AI.

A limitation of our machine learning pipeline is the requirement to upload patches of a certain size (64 by 64). This places the burden on the user to ensure the data is in a particular format apriori to use our Nigthingale tool.

## CURRENT REPOSITORY
This repository currently contains our Exploratory Data Analysis. And, branches will be created to add more outputs as they are developed.
Given the dataset is too large for a free github repository, this repository currently focuses on jupyter notebooks with outputs. The #data lineage.jpg 
file contains the details of the sources and types of data.
Please see the outputs within the jupyter notebooks.

Start with databaseStatistics.ipynb in the ipynb_checkpoints directory for a high level understanding of the data. And, then for a deeper dive into a particular sample, look at the Google colab notebook maub_eda_v2_present_xcc_fsl.ipynb.
Note running any cell will not work as the dataset has to be stored locally elsewhere.

## VIEWING PRO TIP FOR THE CURRENT REPOSITORY
Because the notebooks themselves contain images, we recommend making a local copy of this repository and then opening the Jupyter Notebook locally.

## FURTHER DEVELOPMENT
As the team progresses you will find more branches created from this repository containing various AI models and developmental work towards a decision support system for pathologists. You can get a sneak peek at how our resident expert, Dr. Frederick, is reclassifying the mitotic figures by stages to build a more sophisticated AI. 

![Example Sub-Classification of Phases](https://github.com/sushvij/Capstone-EDA-v2/blob/main/eda_data_lineage/eda_subclassing_slide2_mitotic_figs.png)

Come back again and join us on this journey!

### Warmly,
### Sush, Frederick and Rajiv
