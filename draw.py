import cv2
image=cv2.imread("lena.png",1)
cv2.line(image,(0,0),(800,800),(255,0,0),5)
cv2.rectangle(image,(100,100),(400,400),(0,255,0),7)
cv2.circle(image,(50,50),50,(0,0,255),-1)
cv2.circle(image,(460,50),50,(0,255,0),-1)
cv2.circle(image,(50,460),50,(300,0,255),-1)
cv2.circle(image,(460,460),50,(100,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(image,"GOOD MORNING",(150,200),font,1.2,(10,0,300))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()