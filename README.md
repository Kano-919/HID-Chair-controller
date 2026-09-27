# HID-Chair-controller

Chair-mounted keyboard/mouse rig for PC.
Spring-return pedal, two Sanwa arcade joysticks on the armrests,
printed stick heads with three keyboard switches.

Three Raspberry Pi Picos, CircuitPython + Adafruit HID.
Inputs are active-low: switch between the GP pin and GND.

## Sticks
- Right Sanwa (look) → pico-mouse GP2 / GP3 / GP4 / GP5 (up / down / left / right)
- Left Sanwa (move) → pico-keyboard GP6 / GP8 / GP7 / GP9 (W / A / S / D)

## pico-mouse
| Pin | What it does |
| --- | --- |
| GP2 | Mouse up |
| GP3 | Mouse down |
| GP4 | Mouse left |
| GP5 | Mouse right |

## pico-pedal
| Pin | What it does |
| --- | --- |
| GP2 | Left Ctrl |
| GP6 | Space |

## pico-keyboard
| Pin | What it does |
| --- | --- |
| GP2 | Mouse up + E |
| GP3 | Mouse down |
| GP4 | Mouse left |
| GP5 | Mouse right |
| GP6 | W (left Sanwa up) |
| GP7 | S (left Sanwa down) |
| GP8 | A (left Sanwa left) |
| GP9 | D (left Sanwa right) |
| GP1 | C |
| GP10 | Q |
| GP13 | Left Shift |
| GP17 | Mouse left click |
| GP21 | Mouse right click |

## Notes
Some printed parts took a few prototypes (fit, layer-line friction, material).
Personal project, summer 2026.
