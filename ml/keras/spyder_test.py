# -*- coding: utf-8 -*-
"""
Keras vision (OCR) sample from
Deep Learning With Python (MEAP v6) CH2 

installation notes:
    on an anaconda installation, ensure that python and pip at
    the command line are pointing to the anaconda version.
    installing tensorflow and keras should then make them availabile
    inside Spyder.
    pip install tensorflow
    pip install keras
    
    Anaconda does not run inside a virtualenv -- basically it has
    its own environment.
    
    you'll get a runtime warning about fast_tensor_util being v3.5
    but expected to be v3.6, this causes no errors however.
"""

print ('attempting to run Keras inside Spyder')
from keras.datasets import mnist

# load the MNIST image data into training and testing sets
# each set contains images and corresponding labels

# our goal is to eventually test the network against
# the test data, which it has not previously seen 

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# inspect the training data
# >>> train_images.shape
# (60000, 28, 28)
# >>> len(train_labels)
# 60000
# >>> train_labels
# array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)

# inspect the test data
# >>> test_images.shape
# (10000, 28, 28)
# >>> len(test_labels)
# 10000
# >>> test_labels
# array([7, 2, 1, ..., 4, 5, 6], dtype=uint8)

# in IPython (Spyder or Jupyter) we can use numpy to
# easily view some of our training images.
# make plots appear inline
# %matplotlib inline
import matplotlib.pyplot as plt
# choose a style if desired)
plt.style.use('classic')
#plt.style.use('grayscale')

import numpy as np
selection = np.random.randint(len(train_images))
random_image = train_images[selection]
# display the image chosen
print("displaying a random selection from train_images")
plt.imshow(random_image)
print("it is labeled:",train_labels[selection])


# once we're satisfied that we have loaded the data properly, let's continue.
