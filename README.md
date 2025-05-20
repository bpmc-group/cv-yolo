# cv-yolo
## Code for running Yolo (You Only Look Once) Models

Ultralytics produces/publishes the Yolo models. These models can be used with other tools, like OpenCV, but alos provide many conveniences. For example, by changing from the yolo11s.pt (pre-trained) model to the yolo11s-pose.pt model, pose estimation of the detected humans can be performed. Or by including the track option with a model, tracking of people/objects can be performed. 

## Goals

* Learn the basic capabilities of Yolo models
* Learn how to incorporate Yolo into CV projects without Yolo taking over 
* Learn how to train Yolo models further
* Learn how to translate Yolo models into TensorFlow Lite format suitable for downloading into edge devices
