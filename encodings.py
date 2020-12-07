# Run this program to encode all the class members images

# It is not necessary to run this code each time while taking
# attendance unless there are changes made in students profiles.

import cv2
import face_recognition
import os
import pickle

# Folder path of the images
path = 'Images'

classNames = [] # names
images = [] # images

# Listing out all the class members profiles in images folder
profiles = os.listdir(path)

# For each profile, read the image and store the name
for person in profiles:
    curImg = cv2.imread(f'{path}/{person}')
    images.append(curImg) 
    classNames.append(os.path.splitext(person)[0])
    
encodeList = [] # encodings

# Processing the images and getting the encodings
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
    
data = [classNames, encodeList]

# storing the encodings and names, because it takes a lot of time.
# if we run this program, to get the encodings of all the profile photos
# each time while taking attendance.
pickle.dump(data, open("data.p", "wb"))
