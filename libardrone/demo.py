# Python AR.Drone 2.0
#
# Copyright (C) 2013 Quadeare <lacrampe.florian@gmail.com>
# Twitter : @quadeare
# Glances is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Glances is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from pygame import *  
import pygame
import libardrone
import threading
import time
from subprocess import call

import signal 
import sys



class video(threading.Thread):
    """Video class to launch media flux"""
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self.process = None
    def run(self):
        print "Video"
        call(["ffplay", "http://192.168.1.1:5555/"])
    def stop(self):
        call(["killall", "ffplay"])
        if self.process is not None:
            self.process.terminate()
            self.process = None

class controle(threading.Thread):
    """Control class (to control the drone)"""
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event( )
    def stop(self):
        self._stopevent.set( )
    def run(self):
    
        """We call pygame (to use controler)"""
        pygame.init()

        """Launch drone class"""
        drone = libardrone.ARDrone(True)
        clock = pygame.time.Clock()
        running = True

        """Set up and init joystick"""
        j=joystick.Joystick(0) 
        j.init()
        
        move_forward = 0
        move_backward = 0
        move_left = 0
        move_right = 0
        turn = 0
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    
                    # takeoff
                    if event.button == 7:
                        print "Take Off !"
                        drone.takeoff()
                    # Land
                    elif event.button == 13:
                        print "Land !"
                        drone.land()
                    # Stop and land
                    elif event.button == 6:
                        print "Stop and Land !"
                        drone.land()
                        running = False
                    # Altitude UP
                    elif event.button == 3:
                        print "Altitude UP"
                        drone.speed = 1
                        drone.move_up()
                    # Altitude Down
                    elif event.button == 2:
                        print "Altitude Down"
                        drone.speed = 1
                        drone.move_down()
                    # Emmergency
                    elif event.button == 1:
                        print "Emergency !"
                        drone.reset()
                        
                    # Anim : Boom !
                    elif event.button == 0:
                        print "Anim : Boom !"
                        drone.event_boom()
                        
                    # Anim : Turnarround !
                    elif event.button == 4:
                        print "Anim : Turnarround !"
                        drone.event_turnarround()  

                    # Anim : Yaw Shake !
                    elif event.button == 9:
                        print "Anim : Yaw Shake !"
                        drone.event_yawshake()
                        
                    # Anim : Yaw Dance !
                    elif event.button == 8:
                        print "Anim : Yaw Dance !"
                        drone.event_yawdance()
                        
                    # Anim : ThetaMixed !
                    elif event.button == 5:
                        print "Anim : ThetaMixed !"
                        drone.event_thetamixed()
                        
                        
                if event.type == pygame.JOYBUTTONUP:
                    # Altitude UP
                    if event.button == 3:
                        print "Altitude UP STOP !"
                        drone.speed = 0
                        drone.hover()
                    # Altitude Down
                    elif event.button == 2:
                        print "Altitude Down STOP !"
                        drone.speed = 0
                        drone.hover()
                    
                            
                if event.type == pygame.JOYAXISMOTION:
                    # Axe 0 / Gauche - Droite
                    if event.axis == 0:
                        if event.value < 0:
                            if round(event.value*-1,1) != move_left:
                                # Axe 0 / Gauche
                                print "Axe 0 / Gauche"
                                print "Speed" + " : " + str(round(event.value*-1,1))
                                move_left = round(event.value*-1,1);
                                drone.speed = round(event.value*-1,1)
                                drone.move_left()
                        elif event.value > 0:
                            if round(event.value,1) != move_right:
                                # Axe 0 / Droite
                                print "Axe 0 / Droite"
                                print "Speed" + " : " + str(round(event.value,1))
                                move_right = round(event.value,1)
                                drone.speed = round(event.value,1)
                                drone.move_right()
                        
                    # Axe 1 / Avance - Recule
                    elif event.axis == 1:
                        if event.value < 0:
                            if round(event.value*-1,1) != move_forward:
                                # Axe 1 / Avance
                                print "Axe 1 / Avance"
                                print "Speed" + " : " + str(round(event.value*-1,1))
                                move_forward = round(event.value*-1,1)
                                drone.speed = round(event.value*-1,1)
                                drone.move_forward()
                        elif event.value > 0:
                            if round(event.value,1) != move_backward:
                                # Axe 1 / Recule
                                print "Axe 1 / Recule"
                                print "Speed" + " : " + str(round(event.value,1))
                                move_backward = round(event.value,1)
                                drone.speed = round(event.value,1)
                                drone.move_backward()
                        
                    # Axe 2 / Lacet
                    elif event.axis == 2:
                        if round(event.value*1,0) > 0:
                            if round(event.value*1,0) != turn:
                                # Axe 2 / Lacet Droite
                                print "Axe 2 / Lacet Droite" + " : " + str(round(event.value*1,0))
                                turn = round(event.value*1,0)
                                drone.speed = 1
                                drone.turn_right()
                        elif round(event.value*-1,0) > 0:
                            if round(event.value*-1,0) != turn:
                                # Axe 1 / Lacet Gauche
                                print "Axe 2 / Lacet Gauche" + " : " + str(round(event.value*-1,0))
                                turn = round(event.value*-1,0)
                                drone.speed = 1
                                drone.turn_left()
                        elif round(event.value*1,0) == 0:
                            if round(event.value*1,0) != turn:
                                # Axe 1 / Stop lacet
                                print "Axe 2 / Stop Lacet" + " : " + str(round(event.value*1,0))
                                turn = round(event.value*1,0)
                                drone.speed = 0
                                drone.hover()
            clock.tick(10000)
        print "Shutting down...",
        drone.reset()
        drone.halt()
        video.stop()
        print "Ok."
        quit()

    
if __name__ == '__main__':
    try:
        # Controle
        controle = controle('Thread Controle')
        controle.start()
        time.sleep(5)
        # Video
        video = video('Thread Video')
        video.start()
    except (KeyboardInterrupt, SystemExit):
        cleanup_stop_thread();
        sys.exit()
