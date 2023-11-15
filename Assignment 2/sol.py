from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

class Game:
    def __init__(self):
        self.W_Width, self.W_Height = 800, 1000
        self.z = 250
        self.bounce_bar = 250
        self.bar_color = (1, 1, 1)
        self.end_bar_color = (1, 0, 0)
        # some colors for the that contrasts with black background
        #self.shape_color = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0),(1, 0, 1), (0, 1, 1), (1, 1, 1)]######
        self.game_paused = False
        self.game_end = False
        self.end_message = False
        self.score = 0
        self.speed_begin = 500
        self.speed = 500
        self.t = time.time()
        self.start_time = time.time()
       
        self.diamond_shape = AABB(random.randint(-self.W_Width//2, self.W_Width//2-100), self.W_Height//2, 20, 50, (1, 1, 1))
        #diamond shape done
        
        self.game_bar = AABB(-self.bounce_bar//2, -self.W_Height//2+20, self.bounce_bar, 20, self.bar_color)
        #game_bar done
        
        self.resume = AABB(-self.W_Width//2, self.W_Height//2-100, 100, 100, (0, 1, 1))
        # again play button done
        
        self.play_pause = AABB(-50, self.W_Height//2-100, 100, 100, (1, 0.5, 0))
        #in game play/pause button
        
        self.exit = AABB(self.W_Width//2-100, self.W_Height//2-100, 100, 100, (1, 0, 0))
        #game exit button
        
        glutInit()
        glutInitWindowSize(self.W_Width, self.W_Height)
        glutInitWindowPosition(0, 0)
        glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) 
        glutCreateWindow(b"Assignment2_Catch The Diamon")
        glClearColor(0,0,0,0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(2*math.atan(self.W_Height/(2*self.z))*(180/math.pi), self.W_Width/self.W_Height,	1,	1000.0)
        glutDisplayFunc(self.screen)
        glutIdleFunc(self.animate)
        glutMouseFunc(self.mouseListener)
        glutSpecialFunc(self.specialKeyListener)
        glutMainLoop()
    def screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0,0,0,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0,0,self.z,	0,0,0,	0,1,0)
        glMatrixMode(GL_MODELVIEW)
        # top bar for controls
        self.resume.drawRefreshButton()
        self.play_pause.drawPlayButton() if self.game_paused else self.play_pause.drawPauseButton()
        self.exit.drawCrossButton()
        self.diamond_shape.drawDiamond()
        self.game_bar.drawCatcher()
        if(time.time() - self.start_time >= 10 and not self.game_paused and not self.game_end):
            self.speed += 50
            print("speed increased to: ", self.speed)
            self.start_time = time.time()
        glutSwapBuffers()
    def animate(self):
        if(not self.game_paused and not self.game_end):
            deltaTime = time.time()-self.t
            self.diamond_shape.y -= int(self.speed*deltaTime)
            self.t = time.time()
        if(self.diamond_shape.y < -self.W_Height//2):
            self.game_end = True
            self.game_bar.color = self.end_bar_color
            self.end_message = True
            if self.end_message:
                print("Game Over!")
                print("Score: ", self.score)
            self.end_message = False
            self.diamond_shape.y = self.W_Height//2
        if(Game.hasCollided(self.diamond_shape, self.game_bar) and self.diamond_shape.y > -self.W_Height//2):
            self.diamond_shape.x = random.randint(-self.W_Width//2, self.W_Width//2-100)
            self.diamond_shape.y = self.W_Height//2
            self.diamond_shape.color = (random.random(), random.random(), random.random())
            self.score += 1
            print("Score: ", self.score)
        glutPostRedisplay()
    def mouseListener(self, button, state, x, y):
        x, y = self.convertCoordinate(x, y)
        if button==GLUT_LEFT_BUTTON and state == GLUT_UP:
            if(self.resume.x <= x <= self.resume.x+self.resume.w and self.resume.y <= y <= self.resume.y+self.resume.h):
                print("Starting Over!")
                self.diamond_shape.y = self.W_Height//2
                self.game_bar.color = self.bar_color
                self.game_end = False
                self.score = 0
                self.speed = self.speed_begin
                self.t = time.time()
                self.start_time = time.time()
            if(self.play_pause.x <= x <= self.play_pause.x+self.play_pause.w and self.play_pause.y <= y <= self.play_pause.y+self.play_pause.h):
                self.game_paused = not self.game_paused
                if(self.game_paused):
                    self.pause_time_start = time.time()
                    print("Game paused")
                else:
                    self.start_time += time.time() - self.pause_time_start
                    self.t += time.time() - self.pause_time_start
                    print("Game resumed")
            if(self.exit.x <= x <= self.exit.x+self.exit.w and self.exit.y <= y <= self.exit.y+self.exit.h):
                print("Goodbye!")
                print("Score: ", self.score)
                glutLeaveMainLoop()
    def specialKeyListener(self, key, x, y):
        if key==GLUT_KEY_LEFT and not self.game_end and not self.game_paused and (self.game_bar.x-10)>-self.W_Width//2:
            self.game_bar.x -= 10
        if key==GLUT_KEY_RIGHT and not self.game_end and not self.game_paused and (self.game_bar.x+10)<self.W_Width//2-self.bounce_bar:
            self.game_bar.x += 10

    def convertCoordinate(self, x, y):
        return x - self.W_Width//2, self.W_Height//2 - y
    @staticmethod
    def hasCollided(resume, play_pause):
        return not (resume.x > play_pause.x+play_pause.w or resume.x+resume.w < play_pause.x or resume.y > play_pause.y+play_pause.h or resume.y+resume.h < play_pause.y)

class AABB:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def drawDiamond(self):
        v1 = (self.x+self.w, self.y+self.h//2)
        v2 = (self.x+self.w//2, self.y+self.h)
        v3 = (self.x, self.y+self.h//2)
        v4 = (self.x+self.w//2, self.y)
        self._drawQuad(v1, v2, v3, v4)
    def drawCatcher(self):
        v1 = (self.x+self.w, self.y+self.h)
        v2 = (self.x, self.y+self.h)
        v3 = (self.x+self.h, self.y)
        v4 = (self.x+self.w-self.h, self.y)
        self._drawQuad(v1, v2, v3, v4)
    def drawPauseButton(self):
        Line(self.x+self.w//3, self.y+self.h//4, self.x+self.w//3, self.y+self.h-self.h//4, 1, self.color).draw()
        Line(self.x+self.w-self.w//3, self.y+self.h//4, self.x+self.w-self.w//3, self.y+self.h-self.h//4, 1, self.color).draw()
    def drawPlayButton(self):
        v1 = (self.x+self.w-self.w//3, self.y+self.h//2)
        v2 = (self.x+self.w//3, self.y+self.h//4)
        v3 = (self.x+self.w//3, self.y+self.h-self.h//4)
        self._drawTriangle(v1, v2, v3)
    def drawCrossButton(self):
        Line(self.x+self.w//3, self.y+self.h//4, self.x+self.w-self.w//3, self.y+self.h-self.h//4, 1, self.color).draw()
        Line(self.x+self.w-self.w//3, self.y+self.h//4, self.x+self.w//3, self.y+self.h-self.h//4, 1, self.color).draw()
    def drawRefreshButton(self):
        tip = self.w//6
        Arc(self.x+self.w//2, self.y+self.h//2, self.h//3, 1, 4, 1, self.color, True).draw()
        Line(self.x+self.w//2, self.y+(5*self.h)//6, self.x+self.w//2+(tip*866)//1000, self.y+(5*self.h)//6-tip//2, 1, self.color).draw()
        Line(self.x+self.w//2, self.y+(5*self.h)//6, self.x+self.w//2+(tip*866)//1000, self.y+(5*self.h)//6+tip//2, 1, self.color).draw()


    def drawBoundary(self):
        # for testing
        v1 = (self.x, self.y)
        v2 = (self.x+self.w, self.y)
        v3 = (self.x+self.w, self.y+self.h)
        v4 = (self.x, self.y+self.h)
        self._drawQuad(v1, v2, v3, v4)
    def _drawQuad(self, v1, v2, v3, v4):
        Line(*v1, *v2, 1, self.color).draw()
        Line(*v2, *v3, 1, self.color).draw()
        Line(*v3, *v4, 1, self.color).draw()
        Line(*v4, *v1, 1, self.color).draw()
    def _drawTriangle(self, v1, v2, v3):
        Line(*v1, *v2, 1, self.color).draw()
        Line(*v2, *v3, 1, self.color).draw()
        Line(*v3, *v1, 1, self.color).draw()


class Point:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def draw(self):
        glColor3f(*self.color)
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()
class Line:
    def __init__(self, x1, y1, x2, y2, thickness, color):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.thickness = thickness
        self.color = color
    def draw(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        zone = Line.findZone(dx, dy)
        convertedX1, convertedY1 = Line.convertZoneZToZone0(self.x1, self.y1, zone)
        convertedX2, convertedY2 = Line.convertZoneZToZone0(self.x2, self.y2, zone)
        self._drawLine0(convertedX1, convertedY1, convertedX2, convertedY2, zone)
    def _drawLine0(self, x1, y1, x2, y2, zone):
        # considering line of this segment is in zone 0
        dx = x2 - x1
        dy = y2 - y1
        delE = 2*dy
        delNE = 2*(dy - dx)
        d = 2*dy - dx
        y = y1
        Point(*Line.convertZone0ToZoneZ(x1, y1, zone), self.thickness, self.color).draw()
        for x in range(x1, x2):
            if d < 0:
                d += delE
            else:
                d += delNE
                y+=1
            Point(*Line.convertZone0ToZoneZ(x, y, zone), self.thickness, self.color).draw()

    @staticmethod
    def findZone(x, y):
        if(x >= 0 and y >=0):
            return 0 if x > y else 1
        elif(x < 0 and y >= 0):
            return 2 if -x < y else 3
        elif(x < 0 and y < 0):
            return 4 if x < y else 5
        elif(x >= 0 and y < 0):
            return 6 if x < -y else 7

    @staticmethod
    def convertZoneZToZone0(x, y, zone):
        return [
            [x, y],
            [y, x],
            [y, -x],
            [-x, y],
            [-x, -y],
            [-y, -x],
            [-y, x],
            [x, -y]
        ][zone]
    @staticmethod
    def convertZone0ToZoneZ(x, y, zone):
        return [
            [x, y],
            [y, x], 
            [-y, x], 
            [-x, y], 
            [-x, -y], 
            [-y, -x], 
            [y, -x], 
            [x, -y]
        ][zone]
class Arc:
    def __init__(self, x, y, r, start_zone, finish_zone, thickness, color, is_clockwise = False):
        self.x = x
        self.y = y
        self.r = r
        self.start_zone = start_zone
        self.finish_zone = finish_zone
        self.is_clockwise = is_clockwise
        self.thickness = thickness
        self.color = color
    def draw(self):
        x = 0
        y = self.r
        d = 5-4*self.r
        self._draw8way(x, y)
        while y > x:
            if d < 0:
                # select E
                d += 8*x + 12
                x += 1
            else:
                # select SE
                d += 8*(x-y) + 20
                x += 1
                y -= 1
            self._draw8way(x, y)
    def _draw8way(self, x, y):
        zone = self.start_zone
        while(zone != self.finish_zone):
            pixel = Arc.goToZone(x, y, zone)
            Point(pixel[0]+self.x, pixel[1]+self.y, 1, self.color).draw()
            zone = (zone+1)%8 if not self.is_clockwise else (zone+7)%8
        pixel = Arc.goToZone(x, y, zone)
        Point(pixel[0]+self.x, pixel[1]+self.y, 1, self.color).draw()
    @staticmethod
    def goToZone(x, y, zone):
        x = abs(x)
        y = abs(y)
        if x < y: x, y = y, x
        return [
            [x, y], 
            [y, x], 
            [-y, x], 
            [-x, y], 
            [-x, -y], 
            [-y, -x], 
            [y, -x], 
            [x, -y]
        ][zone]
            


if __name__ == "__main__":
    myGame = Game()