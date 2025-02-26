Face Recognition Project

Overview
This project demonstrates facial recognition using the face_recognition and OpenCV libraries. It identifies and compares faces from images to determine whether they belong to the same person.

Features
Loads images and converts them to RGB format.
Detects and encodes facial features using face_recognition.
Draws bounding boxes around detected faces.
Compares faces to check if they match.

Dependencies
Ensure you have the following libraries installed:

face_recognition
opencv-python (cv2)
matplotlib

How It Works
The script loads three images:

elonmusk.jpg: The reference image of Elon Musk.
elonmusktest.jpg: Another image of Elon Musk (to test matching).
warren.jpg: An image of Warren Buffett (for comparison).
It detects and encodes faces from these images.

A rectangle is drawn around each detected face.

It compares the first two images (elonmusk.jpg and elonmusktest.jpg) and prints True if they match or False if they do not.

Usage
Replace the image paths with your own dataset.
Run the script, and it will display the comparison results in the console.

Future Enhancements

Support for multiple face comparisons.
Implementing a GUI for easier interaction.
Real-time face recognition using a webcam.


Author
Akhil Nair

