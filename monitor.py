import cv2
import os
import datetime
import json
 
json_object = json.dumps({ "date" : f'{datetime.date.today()}' }, indent = 1)

with open("date.json", "w") as outfile: 
    outfile.write(json_object) 

with open('date.json', 'r') as openfile: 
    data = json.load(openfile)

number = len(os.listdir('./videos'))
cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(f'./videos/{data["date"]}_{number}.avi', fourcc, 20.0, (640, 480))

while(True):
    
    ret, frame = cap.read()
    
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
    
    if data['date'] != f'{datetime.date.today()}':
        break

cap.release()
out.release()
cv2.destroyAllWindows()