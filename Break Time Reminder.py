import time

def breakTime ():
  breakCount = 0
  
  print "Program started on " + time.ctime()
  
  while breakCount < 3:
    time.sleep(5)
    print "Break Time !!!"
     breakCount += 1
  
breakTime()
