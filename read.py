
#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import time
reader = SimpleMFRC522()
import sqlite3
conn = sqlite3.connect('/media/usb/tesdb.db')
while True:
  print("Hold a tag near the reader")
  try:
    id, text = reader.read()
    print(id)
    print(text)

  finally:
    GPIO.cleanup()
  sql = "SELECT name FROM data where card_id={};".format(id)
  c = conn.cursor()
  c.execute(sql)
  name = c.fetchone()
  print(name)
  time.sleep(1)
