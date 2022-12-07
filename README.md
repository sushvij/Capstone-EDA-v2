# NIGHTINGALE - A DECISION SUPPORT SYSTEM FOR PATHOLOGISTS

## SUMMARY
Every two minutes a woman in the US is diagnosed with breast cancer. This is a tremedous burden, economic and otherwise, at the patient, family and societal level. Even with survival, there are downstream complications and impact on quality of life. Our motiviation is to improve the breast cancer diagnostic workflows, specifically the pathology workflows, by enhancing the information available to the pathologist. State of the art AI/ML techniques use object detection on whole slide images to quickly identify potential hot spots. A second stage counter, i.e. two class classifier, for dividing cells (mitotic or not-mitotic) has also been added in the literature. This has solidfied AI/ML's role of reducing turnaround time in the diagnostic workflow. This project takes the first big leap of increasing AI/ML's role in the workflow by focusing on outputs (e.g. in pathology reports) that determine better downstream prognosis and treatment outcomes. We do this by going beyond two classes to finding the abnormal images. Our work uses a VGG16 model and deploys an application [mitosisdx.com](mitosisdx.com) that both classifies the abonormal cells and provides usable pathologic explanations. 



## BACKGROUND
One aspect of grading cancers in patients is to understand the number of mitotic cells. While these don't determine the diagnosis of cancer, they do influence it through grading decisions. 

The challenge is that counting mitotic cells is a manually intensive and subjective process. Moreover, a pathologist may see as many as 100-300 images a day causing significant fatigue and ultimately burnout. There is a lot of grey area on classification based on the stage of mitotic development a cell may be undergoing, causing further complications. In summary, a toilsome and faulty process.

Enter AI.

In this repository, we build AI models to classify the breast tissue samples (svs files) and the related sqlite files of canines, where experts had manually labelled cells as mitotic or not. Further [prior research](https://github.com/DeepPathology/MITOS_WSI_CCMCT) has been developed to have an AI (RetinaNet) do this determination of "mitotic" or "not mitotic"; this reasearch has been the primary basis of our understanding.

## LIMITATIONS OF MODEL, DATA AND MACHINE LEARNING PIPELINE

Limitations of our model are similar to the multiple breast cancer classfication models examined in detail in [A Comprehensive Survey on Deep-Learning-Based Breast Cancer Diagnosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8656730/). Specifically, models such as ours experience an imbalance in classes that needs to be handled within the model. We handled imbalance by continuing to expert label till we achieved a baseline number of classes. Additionally, they consume a lot of computing power.

A limitation of the data is that it is canine tissue samples and ultimately the desire is to make inferences on human breast cancer diagnosis. This is a significant roadblock in generalizability which is a current and important challenge across the field of AI. A second limitation of the data is that manual screening of images introduces risks of missing candidates for annotations.

A limitation of our machine learning pipeline is the requirement to upload patches of a certain size (64 by 64). The pipeline uses patches of images and not the Whole Slide Image. This places the burden on the user to ensure the data is in a particular format apriori to using our Nigthingale tool.

## INSTRUCTIONS TO DEPLOY THE DEMO LOCALLY AND IN CLOUD

Get started by cloning this repository. You can do this either locally OR if you prefer not to use local resources, first create an instance on the cloud, and then ssh into it. Here is an example of the series of commands we use to run the demo in both cases. This is a guideline you may choose to use.


**RUN DEMO LOCALLY EXAMPLE**

Start terminal and run the following 7 commands:
1. mkdir frs_capstone_demo
2. cd frs_capstone_demo
3. git clone https://github.com/sushvij/Capstone-EDA-v2.git
4. cd Capstone-EDA-v2
5. cd rv_backend_11212022
6. docker build -t streamlit .
7. docker run -p 8501:8501 streamlit
8. click on the link or copy paste the URL provided into a web browser window to run the demo

**RUN DEMO IN THE CLOUD EXAMPLE**

Establish an instance in the cloud and download the key. In our case, we downloaded "frs_nightingale.prem".
In a terminal, run the following commands:
1. chmod 600 frs_nightingale.pem
2. ssh -i frs_nightingale.pem ubuntu@ec2-18-236-239-181.us-west-2.compute.amazonaws.com (note the address after @ is the public DNS of our instance)
3. (now we are in our cloud instance Ubuntu) **ubuntu@ip-172-31-3-249:~$** git clone https://github.com/sushvij/Capstone-EDA-v2.git
4. **ubuntu@ip-172-31-3-249:~$** repeat commands 4-8 (check pro-tips below in case of issues)

Alternatively, go directly to [Hugging Face Deployment](https://huggingface.co/spaces/rajivvelury/nightingale).

**Pro-tips:** 
1. You may need to install docker. The command is **sudo snap docker install**
2. If you have any permission issues, run the command with **sudo** in front of it. This may particularly be the case for commands 6 and 7 while accesing through the cloud.

Once you are in the URL, you can load an image patch of size 64 by 64 and have the model predict not only let you know if the cell is mitotic or not but also predict the phase of mitosis. You will notice the English explanation provided by our expert, Dr. Frederick Lee, as to why the model is selecting the said classification for the image. This is our important contribution to this project.

Here are a couple of different slide image examples to get you started - 20.png, 5130.png, and 8229.png can be selected from the folder **Capstone-EDA-v2/rv_backend_11212022/patchExtraction_final**. Upload them as the image in the application, and see the results of the analysis by the model. And, the explanation as to why the cell was classified in that manner. Enjoy!


## CURRENT REPOSITORY

This repository currently contains our (1) Exploratory Data Analysis, (2) Baseline Models, and (3) Our Model and It's Deployment. 

Given the dataset is too large for a free github repository, this repository currently focuses on selected patches of data and jupyter notebooks with outputs. 

***Exploratory Data Analysis (folder eda_data_lineage)***

The [data lineaage diagram](https://github.com/sushvij/Capstone-EDA-v2/blob/main/eda_data_lineage/data%20lineage.jpg) contains the details of the sources and types of data of the entire dataset. 

Start with databaseStatistics.ipynb in this folder for a high level understanding of the data. And, then for a deeper dive into a particular sample, look at the Google colab notebook maub_eda_v2_present_xcc_fsl.ipynb.

Note re-running any cell for this background material will not work as the dataset has to be stored locally elsewhere. If you would like to go get the entire dataset, it can be found [here](https://github.com/DeepPathology/MITOS_WSI_CCMCT) under the WSI folder.

***Baseline Model (folders baseline_model and fsl_colab_base_model)***

There have been multiple two stage models deployed by various researchers on this database. The folders baseline_model and fsl_colab_base_model replicate these models.

***Our Model and It's Deployment (folders with rv and fsl_subclassing)***

The significant contribution of our work is that an expert (licensed doctor) provided sub-classifications which can be found in fsl_subclassing. This enabled the model to predict classes that are relevant to the real world. As such a model is fine tuned with this training data, it can help eliminate the tedius and faulty process for pathologists. Thereby saving resouces and having a useful clinical implementation. 

For our models and deployments, go to folder rv_backend_11212022. All data and models here will run, and the demo using these models can be deployed by executing the commands outlined in the previous instructions section.

## PRO TIP FOR THE CURRENT REPOSITORY
Because the notebooks themselves contain large sets of images, we recommend making a local copy of this repository and then opening the Jupyter Notebook locally.

## KEY CONTRIBUTION
As the team progresses you will find more branches created from this repository containing various AI models and developmental work towards a decision support system for pathologists, Nightingale. Our application will be ultimately deployed at **www.mitosisdx.com**. 

You can get a sneak peek at how our resident expert, Dr. Frederick, is reclassifying the mitotic figures by stages to build a more relevant AI, i.e. likely to be used in clinic one day, than the simplistic (mitotic vs not mitotic models) created before. 

![Example Sub-Classification of Phases](https://github.com/sushvij/Capstone-EDA-v2/blob/main/eda_data_lineage/eda_subclassing_slide2_mitotic_figs.png)

Come back again and join us on this journey!

### Warmly,
### Sush, Frederick and Rajiv
