## Facial-Attendance-Marker
Marks the Attendance and the attended time using facial recognition

This program will help you to take the attendance of the students or the members of an organization and the time of their arrival.

Firts create a folder named as "Images", and upload all the photos of the students/employees with their names as the title of their photos.
For example: "Elon Musk.jpg"

Now run the "encodings.py" file to encode all the photos in the "Images" folder. 
This gives us the 128 encodings for each photo, which we later use to compare the faces and mark the attendance. 
It is not necessary to run "encodings.py" file everytime you take the attendance, instead run it just once and we can use these same encodings everytime.
Note: If you make any changes in the "Images" folder, don't forget to run the "encodings.py" file to reflect these changes.

Now run the "Attendance.py" file, which opens the camera and it starts video capturing.

If any student/employee comes in front of the camera, it recognizes the face and compares with the encodings of photos in "Images" folder.
If matches with any of the photos, it draws a rectangle over that person's face, showing their name under their face.

Eventually it will note downs the person's name and their time of arrival in the "Attendance.csv" file.
If "Attendance.csv" file is not found, it creates a file on its own and marks the attendace.

Note: The first arrival time is only saved in the "Attendance.csv" file.

**Important: If you want to take the attendance again on the next day, don't forget to clear the "Attendance.csv" file old data.

Press 'q' to turn off the camera.
