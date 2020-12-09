
#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import time

import sqlite3
conn = sqlite3.connect('/media/usb/tesdb.db')
c = conn.cursor()

while True:
    name = input("input name : ")
    reader = SimpleMFRC522()

    print("Hold a tag near the reader")

    try:
        id, text = reader.read()
        print(id)
        print(text)

    finally:
        GPIO.cleanup()
    time.sleep(1)
    sql = "INSERT INTO data (name,card_id ) VALUES( '{}','{}');".format(name,id)
    print(sql)
    c.execute(sql)
    conn.commit()
    print("data telah terinput")
    time.sleep(1)
