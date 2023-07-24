from picamera2 import Picamera2
import time

dispW=640
dispH=360
picam2 = Picamera2()
picam2.start()

for i in range(1,200):
    
#     fname=(f"img_{time.time()}.jpg")
    picam2.capture_file('image{0:04d}.jpg'.format(i))
    #picam2.capture(fname)
    time.sleep(0.5)
    
    #if cv2.waitKey(1)==ord('q'):
        #break
    

