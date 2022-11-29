import streamlit as st
from PIL import Image
from tensorflow.keras import layers
from tensorflow.keras import models,utils
from tensorflow.keras.models import load_model
from matplotlib import image as mpimg
import numpy as np

def upload_image():
    image = st.file_uploader(" ")
    model = load_model('final_model.h5')
    if image is not None:
       st.image(image)
       image = mpimg.imread(image)
       X = [image]
       X = np.asarray(X)
       classif = np.argmax(model.predict(X)) + 5
       if (image.shape == (64,64,3)):
          st.empty()
          if (classif == 5):
             st.write('The model believes that this is a mitotic figure in metaphase.  This could be one of three phases.')
             if st.button('Click for further explanation'):
                 st.write('The first is prometaphase.  MFs exhibit darkly condensed, shortened, and thickened chromosomes with visible, protruding rods and spikes, which are arranged centrally and occasionally in a ring-like form without predominant central clearing..')
                 st.write('The second is metaphase. MFs with condensed chromosomal material exhibiting protruding, irregular rods and spikes (as in prometaphase above) but arranged in a linear band (“metaphase plate”) at the midline of the cell, which has been sectioned parallel to the microtubule spindle apparatus.')
                 st.write('The third is Rosette form.  Metaphase MF as above, except the dividing cell has been sectioned perpendicular to the microtubule spindle apparatus, resulting in the thickened chromosomes being viewed head-on. Instead of appearing as a linear band, they appear as a ring with distinct central clearing.')

          elif (classif == 6):
             
             st.write('The model believes that this is a mitotic figure in anaphase or telophase.')
             if st.button('Click for further explanation'):
                 st.write('Anaphase is characterized by vondensed chromosomes appear as two distinct aggregates, separated by variable distance, as the mitotic cell progresses toward the formation of daughter nuclei/cells. This stage is often difficult to distinguish clearly from telophase (below).')
                 st.write('Telophase, the last stage of mitosis is characterized by separation of two chromosomal clusters at opposing poles of the cell, which now exhibits the formation of a midline of “cleavage furrow”—a contractile ring which “pinches” the cell membrane and cytoplasm down the middle, generating two fully separated daughter cells.')
          elif (classif == 7):
             st.write('The model believes that this is an atypical mitotic figure.')
             if st.button('Click for further explanation'):
                 st.write('These MFs represent a diverse array of atypical (abnormal) mitotic figures (AMFs), in which derangements of the normal mitotic process result in a grossly abnormal distribution of chromosomal material to daughter cells. Examples include:')
                 st.write('Tri- or multi-polar AMF: Formation of ≥ 3 chromosomal clusters instead of the normal two.')
                 st.write('Chromosome lagging or bridging AMF: During anaphase/telophase, one or more chromosomes (or fragments) “lag” behind the main cluster of chromosomes, or alternatively, bridge the gap between the two separating chromosomal clusters.')
                 st.write('Asymmetric AMF: During anaphase, chromosomes separate into unequal clusters.')
          elif (classif == 8):
             st.write('The model believes that this is a mitotic-like figure, not a mitotic figure')
             if st.button('Click for further explanation'):
                 st.write('These represent non-dividing cells, which for a variety of reasons, may resemble true MFs. Key identifying features are: (a) smooth nuclear contour (in contrast to the protruding rods and spikes seen in MFs); (b) eosinophilic (pink) cytoplasm (characteristic of dying cells); and (c) tissue context (e.g., cell appears in a degenerating area of tumor tissue). Examples of MLFs include:')
                 st.write('Inflammatory cells such as polymorphonuclear leukocytes, which exhibit multi-lobed nuclei, or eosinophils, which possess bilobed nuclei.')
                 st.write('Dying/degenerating cells e.g., in necrotic areas of tumor or cells undergoing apoptosis (programmed cell death). These exhibit thickened, condensed chromosomal material in the nucleus with smooth contours (pyknosis), followed by karyorrhexis, which is the final destructive fragmentation of the nuclear chromatin in a scattered distribution across the cytoplasm.')

       else:
          st.write('The image dimensions were not 64 X 64 X 3.')
      

def main():

     st.title('Subclassification of Mitotic and Mitotic-Like Figures in Canine Breast Tissue')

     st.header('Nightingale Subclassifier')
     st.latex('By~Frederick~Lee,~Rajiv~Velury,~and~Sushmita~Vij.')
     tab1, tab2 = st.tabs(["About","VGG-16"])
     st.sidebar.title('Links')
     link1 = '[MITOS_WSI_CMC GitHub Repository](https://github.com/DeepPathology/MITOS_WSI_CMC)'
     link2 = '[Aubreville et. al. (2020)](https://www.nature.com/articles/s41597-020-00756-z)'
     link3 = '[Donovan et. al. (2021)](https://journals.sagepub.com/doi/full/10.1177/0300985820980049)'
     st.sidebar.markdown(link1, unsafe_allow_html=True)
     st.sidebar.markdown(link2, unsafe_allow_html=True)
     st.sidebar.markdown(link3, unsafe_allow_html=True)
     tab1.write('In this project, we extend work done by Aubreville et. al.(2020), who provided a dataset and used RetinaNet and ResNet to identify mitotic and mitotic-like figures.')
     tab1.write('Here, we use VGG-16 in an attempt to make this work clinically relevant to a pathologist-- can we accurately automate subclassification of these figures?')
     tab1.write('In executing this task, we took a measure of inspiration from Donovan et. al. (2021) to give English-language annotations for each of the subclassifications .')
     tab2.write('Please upload a 64 px X 64 px RGB image of a mitotic figure (MF) or mitotic-like figure (MLF) to see the likely subclassification.  The subclassifier will not work if the image is not of these dimensions.  It will also produce a label, but that label will be nonsense if the uploaded image is not of an MF or MLF.  Garbage in, garbage out!')

     

     
     with tab2:
         upload_image()

     

if __name__ == '__main__':
     
     main()

