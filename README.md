Python AR.Drone 2.0
================

This python script was written to control an AR Drone 2.0 with a joystick. 
It support video (with ffplay) but much work remains...

I use this joystick to control the drone : http://www.thrustmaster.com/fr_FR/produits/t16000m<br>

![Alt text](http://img11.hostingpics.net/pics/792775Joystick.png "My Joystick")

I took a little video about my project : <br>
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/fM5P8-8vQnw/0.jpg)](http://www.youtube.com/watch?v=fM5P8-8vQnw)<br>
(Sorry for the bad quality :/)

Raspberry compatibility :
-----

This python script wonderfully work on a raspberry PI !


Demo:
-----

There is also a demo application included which shows the video from the drone
and lets you remote-control the drone with the joystick:

*Joystick t16000m*

Button 7    : Take Off !<br>
Button 13   : Land <br>
Button 6		: Stop and Land ! <br>
Button 3		: Altitude UP ! <br>
Button 2		: Altitude Down ! <br>
Button 1		: Emmergency mode ! <br>
Button 0		: Animation Boom ! <br>
Button 4		: Animation Turnarround ! <br>
Button 9		: Animation Yaw Shake ! <br>
Button 8		: Animation Yaw Dance ! <br>
Button 5		: Animation ThetaMixed ! <br>


Requirements:
-------------

This software was tested with the following setup:

  * Python 2.6.6
  * Python pygame
  * Unmodified AR.Drone firmware 2.0
