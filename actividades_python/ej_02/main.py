from gpiozero import LED
from time import sleep

red = LED(19)      # 1 Segundo 
blue = LED(26)     #.25 segundos 
green = LED(13)    #.25 segundo

while True:
   green.on()
   sleep(.25)
   green.off()
   sleep(.25)
   blue.on()
   green.on()
   sleep(.25)
   green.off()
   sleep(1)
   blue.off()
   sleep(.25)
   red.on()
   green.on()
   green.off()
   sleep(.25)
   blue.on()
   green.on()
   sleep(.25)
   green.off()
   blue.off
   red.off()
   sleep(1)

