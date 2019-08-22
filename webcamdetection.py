import cv2
import time
import datetime
import pandas as pd
from pandas import DataFrame
faceCascade= cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
vs = cv2.VideoCapture(0)

list_tmp = []
while True:

    ret,frame=vs.read()
    if frame is None:
        pass
    faces = faceCascade.detectMultiScale(frame, 1.3, 5,minSize=(20,20))
    faces_num = len(faces)

    if(faces_num < 1):
          pass
    current = datetime.datetime.now()
    #current=datetime.datetime.ctime(current)
    current=datetime.datetime.strftime(current,'%c')
    current_series=pd.Series(current,name='Zaman')
    #print("Current Face Number: ", faces_num)
    #faces_num_series=pd.Series(faces_num,name='Current Face Number')

    #print(current_series)
    list_tmp.append([current_series,faces_num ])
    #dataframe_series=pd.Series(faces_num,index=current_series,name='kişi sayısı')
    df=pd.DataFrame(list_tmp,columns=["DATETİME", "NUMBER OF PEOPLE"])
    #print(dataframe_series)
    #dataFrame=pd.DataFrame(dataframe_series)
    #dataFrame=dataFrame.append(dataframe_series)
    #dataFrame=dataFrame.loc[0:]=pd.Series(['5', '6'], index=dataFrame.index)
    df.to_excel('output.xlsx')
    print(df)

    #time.sleep(10)
    for(x,y,w,h)in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #key = cv2.waitKey(1) & 0XFF

    cv2.imshow("Video", frame)
    cv2.waitKey(500)
          # dataFrame.to_excel('excel.xlsx')
          #with ExcelWriter('C:\asus\Desktop\staj-vakıfbank.xlsx') as writer:
          # dataframe_series.to_excel(writer)
          #vs.release()
          #print(a)

vs=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.destroyAllWindows()
print(list_tmp)
