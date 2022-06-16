import cv2
import math
import argparse

from sqlalchemy import BLOB

def highlightFace(net, frame, conf_threshold = 0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    BLOB = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True)
