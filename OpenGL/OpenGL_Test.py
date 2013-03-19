import pygame, sys
from pygame.locals import *
from OpenGLLibrary import *
import math

pygame.init()

Screen = (800,600)
Window = glLibWindow(Screen,caption="Lighting Test")
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
           glLibObjCone(0.5,1.8,64)]
           #,glLibObjFromFile("ExamplesData\UberBall.obj")]

default_coordinates = [6, 90, 90]
sphere_coordinates = default_coordinates
camera_pos = [0, 0, 6]
x, y = 0, 0

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
    
    if   key[K_LEFT]:
        sphere_coordinates[2] += 1
        y = camera_pos[1]
        x = camera_pos[0] - .1
    elif key[K_RIGHT]:
        sphere_coordinates[2] -= 1
        y = camera_pos[1]
        x = camera_pos[0] + .1
    elif key[K_UP]:
        sphere_coordinates[1] -= 1
        x = camera_pos[0]
        y = camera_pos[1] + .1
    elif key[K_DOWN]:
        sphere_coordinates[1] += 1
        x = camera_pos[0]
        y = camera_pos[1] - .1
    elif key[K_SPACE]:
        sphere_coordinates = default_coordinates
        x, y = 0, 0

    print (x**2) + (y**2)
    if (((x**2) + (y**2)) >= 36):
        print "Greater"
        x -= .2
        y -= .2
##    r = 6*(math.sin(math.radians(sphere_coordinates[2])))
##    z = 6*(math.cos(math.radians(sphere_coordinates[2])))
##    x = r*(math.cos(math.radians(sphere_coordinates[1])))
##    y = r*(math.sin(math.radians(sphere_coordinates[1])))
    #print sphere_coordinates, " ", r, " ", [x, y, z]
    z = (36 - (x**2) - (y**2))**.5
    camera_pos = [x, y, z]
    Camera.set_target_pos([x, y, z])

    Camera.update()
            
    Window.clear()
    Camera.set_camera()
    Sun.draw()
    Objects[drawing].draw()
    Window.flip()
