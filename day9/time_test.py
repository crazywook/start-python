import time

localtime = time.localtime(time.time())
print(localtime)
print(type(localtime))

asc = time.asctime(localtime)
print(asc)

timeStr = time.strftime('%x', localtime)
print(timeStr)

sleepTime = 1
print('sleep %0.2f second' % sleepTime)
time.sleep(sleepTime)
print('sleep end')
