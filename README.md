# Race Recognition - Python example

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

## Introduction

A Python example for using [Spectrico's race classifier](http://spectrico.com/race-recognition.html). It consists of a face detector for finding the faces, and a classifier to recognize the race of the detected faces. The face detector is an implementation of MTCNN (Tensorflow backend). The classifier is based on MobileNet (Tensorflow backend). Tested under Windows 10 and Ubuntu.

The recognized races are: White, Hispanic, Black, Asian and East Indian.

The race classifier is released as an open-source project to help AI researchers overcome the racial bias in facial recognition algorithms.

Here is a web demo to test it: [Age, Gender and Race Recognition Demo](http://spectrico.com/demo-face-demographics.html)

![image](https://github.com/spectrico/race-recognition-python/blob/main/asian.jpg?raw=true)

#### Usage
```
$ python race_demo.py
```

---
## Dependencies
  pip install numpy

  pip install opencv-python

  pip install tensorflow

  If you use Windows, the OpenCV package is recommended to be installed from: https://www.lfd.uci.edu/~gohlke/pythonlibs/

---
## Credits
The race classifier is based on MobileNet neural network architecture: [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
```
@misc{howard2017mobilenets,
      title={MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications}, 
      author={Andrew G. Howard and Menglong Zhu and Bo Chen and Dmitry Kalenichenko and Weijun Wang and Tobias Weyand and Marco Andreetto and Hartwig Adam},
      year={2017},
      eprint={1704.04861},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

The face detector is MTCNN: [Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks](https://kpzhang93.github.io/MTCNN_face_detection_alignment/)
```
@ARTICLE{7553523, 
author={K. Zhang and Z. Zhang and Z. Li and Y. Qiao}, 
journal={IEEE Signal Processing Letters}, 
title={Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, 
year={2016}, 
volume={23}, 
number={10}, 
pages={1499-1503}, 
keywords={Benchmark testing;Computer architecture;Convolution;Detectors;Face;Face detection;Training;Cascaded convolutional neural network (CNN);face alignment;face detection}, 
doi={10.1109/LSP.2016.2603342}, 
ISSN={1070-9908}, 
month={Oct},}
```
Reference MTCNN implementation:

[https://github.com/davidsandberg/facenet/tree/master/src/align](https://github.com/davidsandberg/facenet/tree/master/src/align)
