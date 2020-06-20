def on_button_pressed_a():
    global led1
    led1 = abs(led1 - 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global led3
    led3 = abs(led3 - 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global led2
    led2 = abs(led2 - 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

led3 = 0
led2 = 0
led1 = 0
led.enable(False)
led1 = 1
led2 = 1
led3 = 1

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, led1)
    pins.digital_write_pin(DigitalPin.P1, led2)
    pins.digital_write_pin(DigitalPin.P2, led3)
basic.forever(on_forever)
