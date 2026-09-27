import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

up = digitalio.DigitalInOut(board.GP2)
down = digitalio.DigitalInOut(board.GP3)
left = digitalio.DigitalInOut(board.GP4)
right = digitalio.DigitalInOut(board.GP5)
w = digitalio.DigitalInOut(board.GP6)
a = digitalio.DigitalInOut(board.GP8)
s = digitalio.DigitalInOut(board.GP7)
d = digitalio.DigitalInOut(board.GP9)

gp1 = digitalio.DigitalInOut(board.GP1)
gp10 = digitalio.DigitalInOut(board.GP10)
gp13 = digitalio.DigitalInOut(board.GP13)
gp17 = digitalio.DigitalInOut(board.GP17)
gp21 = digitalio.DigitalInOut(board.GP21)

for pin in (up, down, left, right, w, a, s, d, gp1, gp10, gp13, gp17, gp21):
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

SPEED = 8

while True:
    dx = 0
    dy = 0
    if not left.value:
        dx -= SPEED
    if not right.value:
        dx += SPEED
    if not up.value:
        dy -= SPEED
    if not down.value:
        dy += SPEED
    if dx or dy:
        mouse.move(dx, dy)

    if not w.value:
        kbd.press(Keycode.W)
    else:
        kbd.release(Keycode.W)

    if not a.value:
        kbd.press(Keycode.A)
    else:
        kbd.release(Keycode.A)

    if not s.value:
        kbd.press(Keycode.S)
    else:
        kbd.release(Keycode.S)

    if not d.value:
        kbd.press(Keycode.D)
    else:
        kbd.release(Keycode.D)

    if not gp1.value:
        kbd.press(Keycode.C)
    else:
        kbd.release(Keycode.C)

    if not up.value:
        kbd.press(Keycode.E)
    else:
        kbd.release(Keycode.E)

    if not gp10.value:
        kbd.press(Keycode.Q)
    else:
        kbd.release(Keycode.Q)

    if not gp13.value:
        kbd.press(Keycode.LEFT_SHIFT)
    else:
        kbd.release(Keycode.LEFT_SHIFT)

    if not gp17.value:
        mouse.press(Mouse.LEFT_BUTTON)
    else:
        mouse.release(Mouse.LEFT_BUTTON)

    if not gp21.value:
        mouse.press(Mouse.RIGHT_BUTTON)
    else:
        mouse.release(Mouse.RIGHT_BUTTON)

    time.sleep(0.01)