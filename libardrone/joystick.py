from pygame import * 
init() 
display.init()

#Setup and init joystick 
j=joystick.Joystick(0) 
j.init() 

#Check init status 
if j.get_init() == 1: print "Joystick is initialized" 

#Setup event information and print data from joystick 
while 1: 
    for e in event.get(): 
        if e.type != QUIT: 
            print '%s: %s' % (event.event_name(e.type), e.dict)