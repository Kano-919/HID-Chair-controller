import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

up = digitalio.DigitalInOut(board.GP2)
down = digitalio.DigitalInOut(board.GP3)
left = digitalio.DigitalInOut(board.GP4)
right = digitalio.DigitalInOut(board.GP5)

for pin in (up, down, left, right):
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

SPEED = 15

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
    time.sleep(0.01)