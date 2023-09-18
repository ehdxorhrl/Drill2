from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x=0
y=90
r=270

import math


while(1):
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)
    
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)
        
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
    while(r>-90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        r=r-3
        x = 255*math.cos(r/360*2*math.pi)+400
        y = 255*math.sin(r/360*2*math.pi)+345
        delay(0.01)
        
    r=270
    
close_canvas()
