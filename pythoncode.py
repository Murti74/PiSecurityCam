import time, sys, smtplib, picamera
import RPi.GPIO as GPIO
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SENSOR_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
frm = 'Example@gmail.com' #Sender
to = 'Example@gmail.com' #Reciever
subj = 'Movement detected'
msg = 'Someone was in your room'
pic = 'picture.jpg'

def mein_callback(channel):
print('BMovement detected!')
t = time.strftime("%d %m %Y / %H:%M:%S")
camera = picamera.PiCamera()
time.sleep(1.5)
camera.rotation = 180
camera.capture(foto, resize=(800,600))
camera.close()

mime = MIMEMultipart()
mime['From'] = frm
mime['To'] = to
mime['Subject'] = Header(subj, 'utf-8')
mime.attach(MIMEText(t, 'plain','utf-8'))
f = open(pic,'rb')
img = MIMEImage( f.read())
f.close()
mime.attach(img)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(frm,'Password') # input your password
server.sendmail(frm,to,mime.as_string())
server.quit()

try:
GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
while True:
time.sleep(10)
except KeyboardInterrupt:
GPIO.cleanup()
