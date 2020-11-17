# ArduinoLEDMusic
This was a project I did just for fun, I got a cheap RGB LED strip and really wanted to make it react to my PC's audio - so I did. I find music visualizers
really cool, so building this was nice. 

This code is specificially for my setup - if you'd like to replicate it, you can probably use the same code / circuit but change things like the port number and pin number. The python converts input/microphone signals and sends it to the Arduino over serial which processes the LEDs.

Server.py uses the [SoundDevice Python Module](https://python-sounddevice.readthedocs.io/en/0.4.1/), so if you'd like to use it you will need this. 

The circuit itself is relatively simple, just a MOSFET controlling the blue and green LEDS at the same time (I could give it manual control of all 3 LED colors, but I only want to use Blue and Green anyway and my breadboard was too small.) The Gate pin / pin 1 is connected to a 220ohm resistor connected to pin D3 of my Arduino Nano. This controls the intensity of the brightness. Pin 2 / Drain is connected to both the green and blue terminal of my LED strip, and Source / pin 3 is connected to GND. The + rail of the LED strip is connected to the 5v rail of the Arduino. 
(I should add a schematic in a later commit)

![first circuit image](https://media.discordapp.net/attachments/472242801304928259/778296434621415454/ifSJizLcITDFFqFqG3RjBsmA9ZoMH6Ryt5h3Ug1K8OdZcKopKbEeTVYMDeeNBMeHUGM8ALmq2rK3313F92A5HeM1noa0L6821dMG.png?width=624&height=468)

![second circuit image](https://media.discordapp.net/attachments/472242801304928259/778296479026249758/-ZipDbwIIo9e2p0L821rNoyNifhnKt8K5OuT1iGnKBa2Rke42PYuC22xmNZqatbZ8gzYk0cAizCtZtC3hOGmTS_vOQT5JHAelh5U.png?width=624&height=468)

Here is a [Demonstration](https://youtu.be/stRL5KbsdQk), if you're interested in how this works in practice. 





