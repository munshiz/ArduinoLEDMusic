# ArduinoLEDMusic
This was a project I did just for fun, I got a cheap RGB LED strip and really wanted to make it react to my PC's audio - so I did. I find music visualizers
really cool, so building this was nice. 

This code is specificially for my setup - if you'd like to replicate it, you can probably use the same code / circuit but change things like the port number and pin number. The python converts input/microphone signals and sends it to the Arduino over serial which processes the LEDs.

Server.py uses the [SoundDevice Python Module](https://python-sounddevice.readthedocs.io/en/0.4.1/), so if you'd like to use it you will need this. 

The circuit itself is relatively simple, just a MOSFET controlling the blue and green LEDS at the same time (I could give it manual control of all 3 LED colors, but I only want to use Blue and Green anyway and my breadboard was too small.) The Gate pin / pin 1 is connected to a 220ohm resistor connected to pin D3 of my Arduino Nano. This controls the intensity of the brightness. Pin 2 / Drain is connected to both the green and blue terminal of my LED strip, and Source / pin 3 is connected to GND. The + rail of the LED strip is connected to the 5v rail of the Arduino. 
(I should add a schematic in a later commit)

![first circuit image](https://lh3.googleusercontent.com/zoMjD3qkOgldb1UwwxMJKbCyOSkN9xQGNDcSiOT3Wmci3Y3GCpgdANnpMzTZFIgVXm1Hl8BfLO9RDNx9p_rcaypulymyiwovI5-AB6arh4_26jDVFxVAPMKNBPSqSpekoazXPlvJGPvpueF5qEXyEzGBhz4a_gohIKBTjcFWE48RD2NEqx6BdiNWdH19xeud375dlQc2E1TM1R-17WuYo7QIQKD_pdZFSWlr6xlBNxgzLxQ960QeQ2oZ5LMe15g09KScI1X-4PmehG3JvLG86JW6CXj5XU2YGcfk0JnCwUFqPQbheOJ_uRGC1qjgZZPeJwgXhz4ogjJsdigF5hXhEO-WwMW5fRQaHkqN2dyzwotfai124zDUSDhU0PREQgGBp3FF78BNLngbgcawEdHCK-hTty8J9YZ_reejJHqTGQ0rYZJV_Cd0EyH6HZeNPnn_wc1hW-DHO8UuUHQpnSk5ip_M1Yx0Nx92gU4Pbx1X7CN3uPEI4iZrTY4vWpJfLFpiNLyc-G-LzKJBh69FlWWXM8DknJ9FtjNPPH43dd-2LDcKPZ2aCDtJ52NplMK3PuV1wIKCutTP7L8fOReH6Hc9e_0yeAm6tEAmNpZP1tvZVB5MXHoFPXQbCbv6S4UQN8dK6kvQHpL1GxAlw39GkiniMnOvl9djrh4-YZ_3u27Vh4zU1xPgbMrjbe4kNVpurg=w1302-h976-no?authuser=0)

![second circuit image](https://lh3.googleusercontent.com/OD9yY1edvLrMyhKJvpD08lFQ-VxshEL1RbgSriVXA3ysPFwgxgi614zL2h9fqcv6op2J4OvKMwW_Ub1jwzuvjXWJQeK2pYFTvCu3Djcc-vOIEl3oD0-Otidcqg4Uoh88e95FB3nExITpJDyvSTpfEtBpf9IKxtNpcZ_0bbr4Nd5JAS53_rQKcAp_N2nQl29_sKt56AabzCIve0SbUcWHqaWFCrYKhjbWN-pGSmU1aDX1tOM9o8tBgYf82bNQEpXTzxJv3R6oCUovfXRnKN0ifycI-CPJrUAZxezHUDMgFvYgDBcZ4SkHDjPIa628eiT3CrjACS3PVFpWlO9vJECb21_22UezK-E2ktyJ-zc8qYwpm5Y7NhACeCGbaTEdiIy2lUlM8hBqbGIb8Znwd51ra4SroXHhVDD_i-V8eExA4GF4N-EeJM69aMIHDBVV6fEOCtxSU9egJygsk2uLzzVzeHWgorwA0FSqQ0WNxk1Lc1Xlq0xDjTmqnYxJ8vsY73XG29WyF36bXBTLR2qlvG8oZBJb5O7bsg1BxTTha0dbIJCTfxIipEoIpe7Rqluh0TWiFwRkPyiep3bBJGby5qUQvCNWeZ1VRKUZ3wXBourLzpW-PjRuTTkdlaQnN4hJXVlPJSIwX4niTlPJ0ajxygyHDBOe4mGtD0ePO6F24qHuP6tfoF3Hbjl5DmIhcHinUA=w1302-h976-no?authuser=0)

Here is a [Demonstration](https://youtu.be/stRL5KbsdQk), if you're interested in how this works in practice. 





