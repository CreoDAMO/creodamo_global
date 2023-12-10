# garden_watering.py

import datetime
import sms 
import RPi.GPIO as GPIO

PUMP_PIN = 17

def initialize():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PUMP_PIN, GPIO.OUT)

def water_garden():
  GPIO.output(PUMP_PIN, GPIO.HIGH)
  datetime.sleep(5)
  GPIO.output(PUMP_PIN, GPIO.LOW)

def main():
  
  initialize()
  
  while True:
    
    now = datetime.datetime.now()
    
    if now.hour == 7 and now.minute == 0:
      water_garden()
      sms.send("+15558675309", "Garden watered!")
      
    datetime.sleep(3600)
      
if __name__ == '__main__':
  main()
