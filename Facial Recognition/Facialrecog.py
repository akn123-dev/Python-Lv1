# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:47:32 2025

@author: akhil.nair
"""

import face_recognition
import cv2
import matplotlib.pyplot as plt

elonmusk= face_recognition.load_image_file(r"C:\Users\akhil.nair\elonmusk.jpg")
elonmusk=cv2.cvtColor(elonmusk, cv2.COLOR_BGR2RGB)

elonmusktest= face_recognition.load_image_file(r"C:\Users\akhil.nair\elonmusktest.jpg")
elonmusktest=cv2.cvtColor(elonmusk, cv2.COLOR_BGR2RGB)

warren=face_recognition.load_image_file(r"C:\Users\akhil.nair\Downloads\warren.jpg")
warren=cv2.cvtColor(warren, cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(elonmusk)[0]
faceencode1=face_recognition.face_encodings(elonmusk)[0]
cv2.rectangle(elonmusk, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]), (255,0,255),2)


faceloc=face_recognition.face_locations(elonmusktest)[0]
faceencode2=face_recognition.face_encodings(elonmusktest)[0]
cv2.rectangle(elonmusktest, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]), (255,0,255),2)

faceloc=face_recognition.face_locations(warren)[0]
faceencode3=face_recognition.face_encodings(warren)[0]
cv2.rectangle(warren, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]), (255,0,255),2)

results=face_recognition.compare_faces([faceencode1], faceencode2)
print(results)

