import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pre_status = current_status = GPIO.input(4)

while(1):
    current_status = GPIO.input(4)

    if (pre_status == 1 and current_status == 0):
        print '%d %d shocked' % (pre_status, current_status)
        subprocess.Popen("curl -XPOST http://pavlok-mvp.herokuapp.com/api/v1/stimuli/beep/1\?access_token\=278065f3ce5880ff1c50363b75ac3a1150a098f7a2fb93038146e61173279906  ", shell=True, stdout=subprocess.PIPE).stdout.read()

        subprocess.Popen("curl -XPOST http://pavlok-mvp.herokuapp.com/api/v1/stimuli/shock/200\?access_token\=278065f3ce5880ff1c50363b75ac3a1150a098f7a2fb93038146e61173279906", shell=True, stdout=subprocess.PIPE).stdout.read()


        print '%d %d' % (pre_status, current_status)
        pre_status = current_status
        time.sleep(0.01)
