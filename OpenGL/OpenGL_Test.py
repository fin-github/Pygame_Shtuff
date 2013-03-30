import pygame, sys
from pygame.locals import *
from OpenGLLibrary import *
import math

pygame.init()

Screen = (800,600)
Window = glLibWindow(Screen,fullscreen=False,caption="Lighting Test")
View3D = glLibView3D((0,0,Screen[0],Screen[1]),45)
View3D.set_view()

Camera = glLibCamera([0,0.5,6],[0,0,0])

glLibLighting(True)
Sun = glLibLight([0,100,0],Camera)
Sun.enable()

glLibColorMaterial(True) 

drawing = 0
Objects = [glLibObjCube(),
           glLibObjTeapot(),
           glLibObjSphere(64),
           glLibObjCylinder(0.5,1.0,64),
           glLibObjCone(0.5,1.8,64),]

default_coordinates = [6, 90, 90]
sphere_coordinates = default_coordinates
camera_pos = [0, 6, 0]
x, y, z = 0, 6, 0
r = 6
theta = 0
phi = 0
negative = False

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_RETURN:
                drawing += 1
                drawing = drawing % 5
            if event.key == K_1: glLibColor((255,255,255))
            if event.key == K_2: glLibColor((255,0,0))
            if event.key == K_3: glLibColor((255,128,0))
            if event.key == K_4: glLibColor((255,255,0))
            if event.key == K_5: glLibColor((0,255,0))
            if event.key == K_6: glLibColor((0,0,255))
            if event.key == K_7: glLibColor((128,0,255))
    
    if key[K_LEFT]:
##        y = camera_pos[1]
##        x = camera_pos[0] - .03
        theta += 0.5
    elif key[K_RIGHT]:
##        y = camera_pos[1]
##        x = camera_pos[0] + .03
##        if(negative): x -= .06
        theta -= 0.5
    elif key[K_UP]:
##        x = camera_pos[0]
##        y = camera_pos[1] + .03
##        if(negative): y -= .06
        phi -= .25
    elif key[K_DOWN]:
##        x = camera_pos[0]
##        y = camera_pos[1] - .03
##        if(negative): y += .06
        phi += .25
    elif key[K_SPACE]:
        phi, theta = 0, 0
        negative = False

##    if (((x**2) + (y**2)) >= 36):
##        new_x = math.fabs(x) - .06
##        new_y = math.fabs(y) - .06
##        x = math.copysign(new_x, x)
##        y = math.copysign(new_y, y)
##        negative = not negative
##    r = 6*(math.sin(math.radians(sphere_coordinates[2])))
##    z = 6*(math.cos(math.radians(sphere_coordinates[2])))
##    x = r*(math.cos(math.radians(sphere_coordinates[1])))
##    y = r*(math.sin(math.radians(sphere_coordinates[1])))
    x = 6*math.sin(math.radians(theta))*math.cos(math.radians(phi))
    y = 6*math.sin(math.radians(theta))*math.sin(math.radians(phi))
    z = 6*math.cos(math.radians(theta))
    
##    z = (36 - (x**2) - (y**2))**.5
##    if(negative):
##        z *= -1
    camera_pos = [x, y, z]
    Camera.set_target_pos([x, y, z])

    Camera.update()
            
    Window.clear()
    Camera.set_camera()
    Sun.draw()
    Objects[drawing].draw()
    Window.flip()
