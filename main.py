#!/usr/bin/env python

from sense_hat import SenseHat
import time, converter, sys, signal

#Sets up the list of arguments
argumentList = sys.argv[1:]

def signal_term_handler(signal, frame):
    print('got SIGTERM')
    sys.exit(0)

def main():
    ##Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0) 
    blue = (0, 0, 255)

    ##Variables
    # Set the loop to true by default, to ensure a endless loop
    loop = True
    sh = SenseHat()
    
    # Used to swtich between the 12 and 24 hour format
    # A value of 0 is the 24 hour format
    # A value of 1 is the 12 hour format
    changeHourFormat = 0
    
    # Sets orientation.
    # A value of '1' is horizontal
    # A value of '0' is vertical
    direction = 1

    sh.show_message("Programmet starter", text_colour=white, scroll_speed = 0.1)
    #Loop
    while loop == True:
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        seconds = time.localtime().tm_sec

        if changeHourFormat != 1:
            hoursTens = hour // 10
            hoursOnes = hour % 10
        else:
            hoursTens = (hour - 12) // 10
            hoursOnes = (hour - 12) % 10

        minutesFull = minute
        hoursFull = hour
        secondsFull = seconds
        minuteTens = minute // 10
        minuteOnes = minute % 10
        secondTens = seconds // 10
        secondOnes = seconds % 10

        if direction != 0:
            converter.binary(hoursTens, 1, direction, red)
            converter.binary(hoursOnes, 2, direction, red)
            converter.binary(minuteTens, 3, direction, green)
            converter.binary(minuteOnes, 4, direction, green)
            converter.binary(secondTens, 5, direction, blue)
            converter.binary(secondOnes, 6, direction, blue)
        else:
            converter.binary(hoursFull, 3, direction, red)
            converter.binary(minutesFull, 4, direction, green)
            converter.binary(secondsFull, 5, direction, blue)


        for event in sh.stick.get_events():
            if event.direction == "up": 
                changeHourFormat = 0
                direction = 1
            elif event.direction == "down": 
                changeHourFormat = 1
                direction = 1
            elif event.direction == "left":
                direction = 0
                changeHourFormat = 0 
            elif event.direction == "right":     
                direction = 0 
                changeHourFormat=1
            elif event.direction == "middle":
                sh.show_message("Programmet slutter", text_colour=white, scroll_speed = 0.1)
                sh.clear()
                signal.signal(signal.SIGTERM, signal_term_handler)
                loop = False
            sh.clear()  
        time.sleep(0.1)

if __name__ == '__main__':
    exit(main())          


#cd /lib/systemd/system/
#sudo nano hello.service

#sudo chmod 644 /lib/systemd/system/hello.service
#chmod +x /home/pi/hello_world.py
#sudo systemctl daemon-reload
#sudo systemctl enable hello.service
#sudo systemctl start hello.service
