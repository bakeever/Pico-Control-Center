from machine import Pin
from gpio_lcd import GpioLcd
#import time
#import board
#import digitalio

# Create the LCD object
lcd = GpioLcd(
    rs_pin=Pin(16),
    enable_pin=Pin(17),
    d4_pin=Pin(18),
    d5_pin=Pin(19),
    d6_pin=Pin(20),
    d7_pin=Pin(21),
    num_lines=2,
    num_columns=16,
)
# LCD Startup
lcd.clear()
lcd.move_to(0, 0)
lcd.putstr("PICO CTRL CENTER")
# Input Setup
b1 = digitalio.DigitalInOut(board.GP10)
b2 = digitalio.DigitalInOut(board.GP11)
b3 = digitalio.DigitalInOut(board.GP12)
b4 = digitalio.DigitalInOut(board.GP13)

b1.switch_to_input(pull=digitalio.Pull.DOWN)
b2.switch_to_input(pull=digitalio.Pull.DOWN)
b3.switch_to_input(pull=digitalio.Pull.DOWN)
b4.switch_to_input(pull=digitalio.Pull.DOWN)

# Operation Loop
while True:
    if b1:
        print('do the thing')

