import  cv2
import  numpy as np


img = np.zeros((512,512,3),np.uint8)
#img[:] = 255,211,121
#drawing lines
cv2.line(img,(0,0),(100,100),(0,255,0),3 )
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3 )
# drawing rectangle
cv2.rectangle(img,(350,100),(450,200),(0,0,255),2)
#filling the rectangle with color
cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
#drawing circle
cv2.circle(img,(150,400),50,(255,0,0),6)
#puting text in images
cv2.putText(img,"Drawimg shapes # kodehauz",(15,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.putText(img,"Daniel Samuel",(15,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)


cv2.imshow("img",img)
cv2.waitKey(0)