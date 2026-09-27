import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

ctrl = digitalio.DigitalInOut(board.GP2)
space = digitalio.DigitalInOut(board.GP6)

for pin in (ctrl, space):
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

while True:
    if not ctrl.value:
        kbd.press(Keycode.LEFT_CONTROL)
    else:
        kbd.release(Keycode.LEFT_CONTROL)

    if not space.value:
        kbd.press(Keycode.SPACE)
    else:
        kbd.release(Keycode.SPACE)

    time.sleep(0.01)