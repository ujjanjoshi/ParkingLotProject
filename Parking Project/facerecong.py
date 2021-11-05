#histogram of oriented gradients
import cv2
import numpy as np
import face_recognition
#orginal
imgBill = face_recognition.load_image_file('../photochecl/BillGates.jpg')
imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
#test
imgBillTest = face_recognition.load_image_file('../photochecl/BillGatesTest.jpg')
imgBillTest = cv2.cvtColor(imgBillTest, cv2.COLOR_BGR2RGB)

#detect face
faceloc = face_recognition.face_locations(imgBill)[0]
encodeBill = face_recognition.face_encodings(imgBill)[0]
cv2.rectangle(imgBill, (faceloc[3],faceloc[0]), (faceloc[1],faceloc[2]),(255,0,255),2)

facelocTest = face_recognition.face_locations(imgBillTest)[0]
encodeBillTest = face_recognition.face_encodings(imgBillTest)[0]
cv2.rectangle(imgBillTest, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)
#result
faceDis=face_recognition.face_distance([encodeBill],encodeBillTest)
results = face_recognition.compare_faces([encodeBill], encodeBillTest)
print(results,faceDis)
cv2.putText(imgBillTest,f'{results}{round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

#show image
cv2.imshow('Bill Gates', imgBill)
cv2.imshow('Bill Gates Test', imgBillTest)
cv2.waitKey(0)
