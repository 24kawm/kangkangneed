import cv2 as cv
import aircv as ac
import subprocess
import script
import numpy as np

script.connect()
subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
image_origin = cv.imread('./screenshot/screenshot.png')
image_s1 = cv.imread('./screenshot/screenshot.png')  # 旗舰大破

s1 = np.array(image_s1)

# match_s1 = ac.find_template(image_origin, image_s1, threshold=0.95)
# match_s2 = ac.find_template(image_origin, image_s2, threshold=0.95)
print(image_s1[130][1042][0], image_s1[130][1042][1], image_s1[130][1042][2])

