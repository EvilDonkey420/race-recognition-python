# Copyright © 2019 by Spectrico

model_file = "model-weights-spectrico-races-mobilenet-224x224-038BB571.pb"  # path to the race classifier
label_file = "labels.txt"   # path to the text file, containing list with the supported classes
input_layer = "input_1"
output_layer = "softmax/Softmax"
classifier_input_size = (224, 224) # input size of the classifier
