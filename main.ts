input.onButtonPressed(Button.A, function () {
    led1 = Math.abs(led1 - 1)
})
input.onButtonPressed(Button.AB, function () {
    led3 = Math.abs(led3 - 1)
})
input.onButtonPressed(Button.B, function () {
    led2 = Math.abs(led2 - 1)
})
let led3 = 0
let led2 = 0
let led1 = 0
led.enable(false)
led1 = 1
led2 = 1
led3 = 1
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, led1)
    pins.digitalWritePin(DigitalPin.P1, led2)
    pins.digitalWritePin(DigitalPin.P2, led3)
})
