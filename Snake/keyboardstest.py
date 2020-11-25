import keyboard

shot_pressed = 0
was_pressed = False

x = 0

while True:
    print(x)
    if keyboard.is_pressed('z'):
        x = 1
    if keyboard.is_pressed('q'):
        x = 2
    if keyboard.is_pressed('s'):
        x = 3
    if keyboard.is_pressed('d'):
        x = 4
