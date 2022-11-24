import streamlit as st
from PIL import Image
from tensorflow.keras import layers
from tensorflow.keras import models,utils
from tensorflow.keras.models import load_model
from matplotlib import image as mpimg
import numpy as np

def upload_image():
    image = st.file_uploader(label='Please upload a .png file within dimensions 64 X 64 X 3.', type='png')
    model = load_model('final_model.h5')
    if image is not None:
       st.image(image)
       image = mpimg.imread(image)
       X = [image]
       X = np.asarray(X)
       if (image.shape == (64,64,3)):
          st.write(np.argmax(model.predict(X)) + 5)
       else:
          st.write('The image dimensions were not 64 X 64 X 3.')


def main():

     st.title('Subclassification of Mitotic asnd Mitotic-Like Figures')

     st.header('Nightingale Subclassifier')

     st.text('Please upload a 64 px X 64 px RGB image of a mitotic figure (MF) or mitotic-like figure (MLF) to see the likely subclassification.  The subclassifier will not work if the image is not of these dimensions.  It will also produce a label, but that label will be nonsense if the uploaded image is not of an MF or MLF.  Garbage in, garbage out!')

     

     

     upload_image()

     

if __name__ == '__main__':
     
     main()