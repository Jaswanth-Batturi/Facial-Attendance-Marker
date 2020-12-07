# Attendance marker

import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime
import pickle

# Loading the students images encodings that we processed before
# Note: If any changes made in the "Images" folder, re-run the encodings program
# before running this program.
classNames, encodeListKnown = pickle.load(open("data.p", "rb"))

Attendees = []

try:
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(',')
            Attendees.append(entry[0])
except:
    with open('Attendance.csv', 'w+') as f:
        f.write('Name,Time')

# Create already a "Attendance.csv" file in the same folder
# When a student comes in front the camera, it recognizes their face
# and saves the student name and time of arrival.
# If student already saved in the csv file, then it not save his name agian
# and also it wont update the arrival time.
def markAttendance(name):
    if name not in Attendees:
        Attendees.append(name)
        with open('Attendance.csv', 'a') as f:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.write(f'\n{name},{dtString}')

# opening the camera
cap = cv2.VideoCapture(0)

# camera runs foreover and captures students faces until "q" is pressed
while True:
    success, img = cap.read()
    
    # processing the image
    
    # making the image four times smaller, to speed up the process
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25) 
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS)
    
    # comparing the current faces on camera to the encodings we already have
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        
        # getting face coordinates and drawing a box around it
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            markAttendance(name)
            # coordinates of the person face 
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            # draws a rectangle around the face
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, f'{name}', (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255,255,255), 2)
            
    cv2.imshow("Output", img)
    
    # loop breaking condition, enter "q" to exit, this will turn off the camera
    if cv2.waitKey(1)  & 0xFF==ord('q'):
        cap.release()
        break
