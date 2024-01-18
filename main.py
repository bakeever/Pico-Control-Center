from machine import Pin, Timer
from gpio_lcd import GpioLcd
# == Global Variables == #
interrupt_flag = 0
state = 0
# == System Operation LED == #
# If blinking once per sec, system is functional
sys_led = Pin(25, Pin.OUT)
sys_led.value(0)  # LED off
timer = Timer(-1)
timer.init(
    period=1000,
    mode=Timer.PERIODIC,
    callback=lambda t: sys_led.value(not sys_led.value()),
)
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

# === Input Setup ===#
# Inlcudes all switches, pots, encoders in system
# -- Section 1 -- #
pin0 = Pin(2, Pin.IN, Pin.PULL_UP)
pin1 = Pin(3, Pin.IN, Pin.PULL_UP)
pin2 = Pin(4, Pin.IN, Pin.PULL_UP)
pin3 = Pin(5, Pin.IN, Pin.PULL_UP)
# -- Section 2 -- #
pin4 = Pin(6, Pin.IN, Pin.PULL_UP)
pin5 = Pin(7, Pin.IN, Pin.PULL_UP)
pin6 = Pin(8, Pin.IN, Pin.PULL_UP)
pin7 = Pin(9, Pin.IN, Pin.PULL_UP)
# -- Seciton 3 -- Outputs #
pin8 = Pin(10, Pin.OUT, Pin.PULL_DOWN)
pin9 = Pin(11, Pin.OUT, Pin.PULL_DOWN)
pin10 = Pin(12, Pin.OUT, Pin.PULL_DOWN)
pin11 = Pin(13, Pin.OUT, Pin.PULL_DOWN)
pin12 = Pin(14, Pin.OUT, Pin.PULL_DOWN)
pin13 = Pin(15, Pin.IN, Pin.PULL_UP)

def callback(pin13):
    global interrupt_flag
    interrupt_flag = 1

pin13.irq(trigger=Pin.IRQ_FALLING, handler=callback)
# == Main Loop == #
while True:
    if interrupt_flag == 1:
        lcd.move_to(0, 0)
        lcd.putstr("PICO CTRL CENTER")
        lcd.move_to(0, 1)
        lcd.putstr("Interrupt")
        interrupt_flag = 0
        if pin13.value() == 1:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("PICO CTRL CENTER")
            lcd.move_to(0, 1)
            lcd.putstr("Resetting")
    elif pin0.value() == 0:  # Screen Clear
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("PICO CTRL CENTER")
    elif pin1.value() == 0:
        state = 1
        lcd.move_to(0, 1)
        lcd.putstr("State: 1        ")
    elif pin2.value() == 0:
        state = 2
        lcd.move_to(0, 1)
        lcd.putstr("State: 2        ")
    elif pin3.value() == 0:
        state = 3
        lcd.move_to(0, 1)
        lcd.putstr("State: 3        ")
    if pin4.value() == 0:
        lcd.move_to(0, 1)
        lcd.putstr("Function 1")
    elif pin5.value() == 0:
        lcd.move_to(0, 1)
        lcd.putstr("Function 2")
    if pin6.value() == 0:
        lcd.move_to(0, 1)
        lcd.putstr("Function 3")
    if pin7.value() == 0:
        lcd.move_to(0, 1)
        lcd.putstr("Function 4")
    if pin8.value() == 1:
        lcd.move_to(0, 1)
        lcd.putstr("Function 5")
    if pin9.value() == 1:
        lcd.move_to(0, 1)
        lcd.putstr("Function 6")
    if pin10.value() == 1:
        lcd.move_to(0, 1)
        lcd.putstr("Function 7")
    if pin11.value() == 1:
        lcd.move_to(0, 1)
        lcd.putstr("Function 8")
    if pin12.value() == 1:
        lcd.move_to(0, 1)
        lcd.putstr("Function 9")
    if state == 0:
        pass
    elif state == 1:
        print('state 1')
    elif state == 2:
        print('state 2')
    elif state == 3:
        print('state 3')
    else:
        print('Waiting for command')
