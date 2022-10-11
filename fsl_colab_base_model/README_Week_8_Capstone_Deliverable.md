# _Overview & Findings:_  

Given difficulties running the published canine object detection/classification models locally in a VM as well as on AWS, we attempted to run the authors' original `RetinaNet-CMC-MEL` model on Google Colaboratory, configuring the instance with "high RAM" (52 GB) and a backend TPU, which Colab describes as significantly faster than using "GPU" hardware acceleration. The RetinaNet model was successfully trained to completion (10 + 30 epochs) on Colab after making appropriate modifications:
*  Py v3.7.14 (Colab default) was used.
*  Fastai v. 1.0.61 was pip-installed (with removal of fastai v. 2.7.9 and installation of nvidia-ml-py3-7.352.0): This was required for compatibility with the authors' implementation of fastai v.1's `callbacks` functionality (deprecated in the current fastai v.2).
*  An error in the authors' posted `~/lib/calculate_F1.py` helper function, which caused failure of their critical `data_loader` function was tracked down & corrected.

Despite the Colab instance configuration above as well as loading all sqlite annotation data, training code, and complete WSI data for all 21 slides (~50 GB) in the instance's memory, training took _13 hours (about 15 min. per epoch)!_  This lengthy duration was unexpected given our setup and may well be due to e.g., the use of the outdated fastai v.1, the authors' `SlideRunner` code, other outdated code (not updated since publication), and/or implementation inefficiencies _(NB: The authors provide scant documentation of specific details of their implementation.)_

Final train/validation loss achieved was 0.17 / 0.18, directly comparable to what the authors reported (see notebook). Plots of the training/validation loss vs. epoch did not show any overt evidence of overfitting.

The images of mitotic/non-mitotic cell figures in the last cell of our notebook show examples of typical bounding boxes localizing the model's detections, with accompanying 'certainty' scores and corresponding class activation mapping (CAM) images. The latter activation images correspond nicely with bounding boxes identified by the model.

Our efforts will now focus on extending the authors' two-stage model to a third stage, which will attempt to implement a CNN (e.g. Resnet18) in an up-to-date framework to take as inputs, patches of mitotic figures and mitotic-like figures (mitotic look-alikes or 'imposters') identified by the authors' model, and subclassify them by mitotic stage or as _atypical mitotic figures_ (which may have prognostic significance from a clinical standpoint), or non-mitoses. This will require hand-labeling an estimated 160 to 800 image patches for training and semi-supervised model development.

Frederick Lee, M.D.

