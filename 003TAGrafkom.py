from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut
import random as rd

play = False

pos_x=-1000
pos_y=-500

pos_x_rintangan =1300
pos_y_rintangan =-500

pos_x_rintangan2 =1300
pos_y_rintangan2 =-600

pos_x_awan = 0
pos_y_awan = 0
gerak_awan = 0.1

nyawa = 3
game_over = False
kalah = False
   
 
w, h = 1280, 750
koor_ortoX = (w / 2) / 10
koor_ortoY = (h / 2) / 10

posxjalan = 0
posyjalan= 0
gerakjalan= 0.5

posxlogo=0
posylogo=0
geraklogo=1

def jedagJedug3():
    angka = rd.randrange(-1,1)
    return angka

def logo():
    global posxlogo, posylogo, geraklogo
    
    if posxlogo <= -1300:
        posxlogo = 1300
        
    posxlogo -= geraklogo
    glPushMatrix()
    glTranslated(posxlogo, posylogo + jedagJedug3(), 0)
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(163.4428524560694, 394.4454261478842)
    glVertex2f(0, 426.9669310707358)
    glVertex2f(-166.8193005130736, 393.0293643028359)
    glVertex2f(-300.8361142709363, 302.9824954982162)
    glVertex2f(-398.8539797619667, 152.3688388615044)
    glVertex2f(-426.9669310707358, 0)
    glVertex2f(-398.7926003135174,-152.5294140916617)
    glVertex2f(-305.9235323891064, -297.8448464528702)
    glVertex2f(-174.4728066964634, -389.6921861564855)
    glVertex2f(0, -426.9669310707358)
    glVertex2f(165.7477962833291, -393.4824370352284)
    glVertex2f(305.7996135246314, -297.9720735172149)
    glVertex2f(401.5233195702166, -145.1887876844358)
    glVertex2f(426.9669310707358, 0)
    glVertex2f(399.6153224694756, 150.3607471236408)
    glVertex2f(314.335779991086, 288.9528986623218)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255, 250, 240)
    glVertex2f(129.8507829403749, 313.375878130366)
    glVertex2f(249.7310009257626,229.565010401897)
    glVertex2f(313.5746744431826, 129.3699747702626)
    glVertex2f(339.2133057888595, 0)
    glVertex2f(318.9990668391253, -115.3484381340883)
    glVertex2f(242.9492549985344, -236.7304930081113)
    glVertex2f(131.6819964569384, -312.6108101670849)
    glVertex2f(-8.0193386457255, -339.1184999847273)
    glVertex2f(-138.6137736272673, -309.5995616679956)
    glVertex2f(-243.0477050765364, -236.6294146576781)
    glVertex2f(-316.8295866315521, -121.1803608638221)
    glVertex2f(-339.2133057888595, 0)
    glVertex2f(-316.8783508896266, 121.0527883267339)
    glVertex2f(-239.005893422723, 240.7111333806816)
    glVertex2f(-132.5332766509967, 312.2508565310217)
    glVertex2f(0, 339.2133057888595)
    glEnd()

    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glColor3ub(0, 0, 0)
    glVertex2f(0,0)
    glVertex2f(129.8507829403749, 313.375878130366)
    glVertex2f(0,0)
    glVertex2f(249.7310009257626,229.565010401897)
    glVertex2f(0,0)
    glVertex2f(313.5746744431826, 129.3699747702626)
    glVertex2f(0,0)
    glVertex2f(339.2133057888595, 0)
    glVertex2f(0,0)
    glVertex2f(318.9990668391253, -115.3484381340883)
    glVertex2f(0,0)
    glVertex2f(242.9492549985344, -236.7304930081113)
    glVertex2f(0,0)
    glVertex2f(131.6819964569384, -312.6108101670849)
    glVertex2f(0,0)
    glVertex2f(-8.0193386457255, -339.1184999847273)
    glVertex2f(0,0)
    glVertex2f(-138.6137736272673, -309.5995616679956)
    glVertex2f(0,0)
    glVertex2f(-243.0477050765364, -236.6294146576781)
    glVertex2f(0,0)
    glVertex2f(-316.8295866315521, -121.1803608638221)
    glVertex2f(0,0)
    glVertex2f(-339.2133057888595, 0)
    glVertex2f(0,0)
    glVertex2f(-316.8783508896266, 121.0527883267339)
    glVertex2f(0,0)
    glVertex2f(-239.005893422723, 240.7111333806816)
    glVertex2f(0,0)
    glVertex2f(-132.5332766509967, 312.2508565310217)
    glVertex2f(0,0)
    glVertex2f(0, 339.2133057888595)
    glEnd()
    glPopMatrix()

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def start_game():
    glPushMatrix()
    glBegin(GL_POLYGON)
    # Kiri bawah
    glColor3ub(135, 206, 235)
    glVertex2f(-w,-h)
    # Kanan bawah
    glColor3ub(135, 206, 235)
    glVertex2f(w,-h)
    # Kanan atas
    glColor3ub(255, 255, 0)
    glVertex2f(w, h)
    # Kiri atas
    glColor3ub(135, 206, 235)
    glVertex2f(-w,h)
    glEnd()
    logo()
    glPopMatrix()
    drawTextBold("L E T S P L A Y",1000,700)  

    glRasterPos(-1200,700)
    for c in "CARA BERMAIN":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(-1200,650)
    for c in "1. Gunakan Panah Untuk Menggerakan Sepeda":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(-1200,600)
    for c in "2. Hindari rintangan":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(-1200,550)
    for c in "3. Selamat Bermain":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

def endgame():
    glPushMatrix()
    glBegin(GL_POLYGON)
    # Kiri bawah
    glColor3ub(135, 206, 235)
    glVertex2f(-w,-h)
    # Kanan bawah
    glColor3ub(135, 206, 235)
    glVertex2f(w,-h)
    # Kanan atas
    glColor3ub(255, 255, 0)
    glVertex2f(w, h)
    # Kiri atas
    glColor3ub(135, 206, 235)
    glVertex2f(-w,h)
    glEnd()
    logo()
    glPopMatrix()

    glRasterPos(-1200,700)
    for c in "GAME OVER BESTIE":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(-1200,650)
    for c in "Tutup tampilan ini dan mulailagi ya":
        glutBitmapCharacter( glut.GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    
def jedagJedug():
    angka = rd.randrange(-1,1)
    return angka

def jedagJedug2():
    angka = rd.randrange(-1,1)
    return angka

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(- koor_ortoX, koor_ortoX, - koor_ortoY, koor_ortoY)

def background():
    glBegin(GL_POLYGON)
    # Kiri bawah
    glColor3ub(135, 206, 235)
    glVertex2f(-w,-h)
    # Kanan bawah
    glColor3ub(135, 206, 235)
    glVertex2f(w,-h)
    # Kanan atas
    glColor3ub(255, 255, 0)
    glVertex2f(w, h)
    # Kiri atas
    glColor3ub(135, 206, 235)
    glVertex2f(-w,h)
    glEnd()

def background1() :
    glColor(0,255,255)
    glBegin(GL_POLYGON)
    # Kiri bawah
    
    glVertex2f(-w,-h)
    # Kanan bawah
    
    glVertex2f(w,-h)
    # Kanan atas
    
    glVertex2f(w, h)
    # Kiri atas

    glVertex2f(-w,h)
    glEnd()

def fullmatahari() :
    matahari1()
    matahari2()
    matahari3()
    matahari4()
    
def matahari1():
    glColor3ub(255,128,0)
    glBegin(GL_POLYGON)
    glVertex2f(900, 500)
    glVertex2f(1100, 500)
    glVertex2f(1100, 300)
    glVertex2f(900, 300)
    glEnd()

def matahari2 ():
    glColor3ub(255,153,51)
    glBegin(GL_POLYGON)
    glVertex2f(920, 480)
    glVertex2f(1080, 480)
    glVertex2f(1080, 320)
    glVertex2f(920, 320)
    glEnd()

def matahari3():
    glColor3ub(255,255,102)
    glBegin(GL_POLYGON)
    glVertex2f(940, 460)
    glVertex2f(1060, 460)
    glVertex2f(1060, 340)
    glVertex2f(940, 340)
    glEnd()

def matahari4 ():
    glColor3ub(255,255,153)
    glBegin(GL_POLYGON)
    glVertex2f(960, 440)
    glVertex2f(1040, 440)
    glVertex2f(1040, 360)
    glVertex2f(960, 360)
    glEnd()

def fullawan1(): 
    global pos_x_awan,pos_y_awan, gerak_awan
    if pos_x_awan <= -1300:
        pos_x_awan = 1300
    pos_x_awan -= gerak_awan

    glPushMatrix()
    glTranslated(pos_x_awan, pos_y_awan, 0)  
    awan1()
    awan2()
    glPopMatrix()

def awan1() :
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(440, 540)
    glVertex2f(450, 540)
    glVertex2f(450, 560)
    glVertex2f(440, 560)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(450, 560)
    glVertex2f(460, 560)
    glVertex2f(460, 570)
    glVertex2f(450, 570)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(460, 570)
    glVertex2f(470.5, 570)
    glVertex2f(470.5, 580)
    glVertex2f(460, 580)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(470.5, 580)
    glVertex2f(480.5, 580)
    glVertex2f(480.5, 600)
    glVertex2f(470.5, 590)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(480.5, 590)
    glVertex2f(500.5, 590)
    glVertex2f(500.5, 600)
    glVertex2f(480.5, 600)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(500.5, 590)
    glVertex2f(510.5, 590)
    glVertex2f(510.5, 580)
    glVertex2f(500.5, 580)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(510.5, 580)
    glVertex2f(520.5, 580)
    glVertex2f(520.5, 570)
    glVertex2f(510.5, 570)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(520.5, 570)
    glVertex2f(540, 570)
    glVertex2f(540, 560)
    glVertex2f(520.5, 560)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(540, 560)
    glVertex2f(550, 560)
    glVertex2f(550, 540)
    glVertex2f(540, 540)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(540, 540)
    glVertex2f(540, 530)
    glVertex2f(530, 530)
    glVertex2f(530, 540)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(530, 530)
    glVertex2f(530, 520)
    glVertex2f(460, 520)
    glVertex2f(460, 530)
    glEnd()

    glColor3b(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(460, 530)
    glVertex2f(460, 540)
    glVertex2f(450, 540)
    glVertex2f(450, 530)
    glEnd()

def awan2():
    glColor(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(450, 540)
    glVertex2f(450, 560)
    glVertex2f(460, 560)
    glVertex2f(460, 560)
    glVertex2f(460, 570)
    glVertex2f(470.5, 570)
    glVertex2f(470.5, 580)
    glVertex2f(480.5, 580)
    glVertex2f(480.5, 590)
    glVertex2f(500.5, 590)
    glVertex2f(500.5, 580)
    glVertex2f(510.5, 580)
    glVertex2f(510.5, 570)
    glVertex2f(520.5, 570)
    glVertex2f(520.5, 560)
    glVertex2f(540, 560)
    glVertex2f(540, 540)
    glVertex2f(530, 540)
    glVertex2f(530, 530)
    glVertex2f(460, 530)
    glVertex2f(460, 540)
    glVertex2f(450, 540)
    glEnd()

def kgedung():
    gedung2()
    gedung()
    gedung3()
    gedung5()
    gedung6()
    gedung4()
    gedung7()
    gedung8()
    gedung9()

def gedung():
    glColor3ub(153, 76, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1000 , -300)
    glVertex2f(1000 , 0)
    glVertex2f(800 ,0)
    glVertex2f(800 , -300)
    glEnd()

def gedung7():
    glColor3ub(255, 153, 51)
    glBegin(GL_POLYGON)
    glVertex2f(-1000 , -300)
    glVertex2f(-1000 , 500)
    glVertex2f(-800 ,500)
    glVertex2f(-800 , -300)
    glEnd()

def gedung2():
    glColor3ub(0, 0, 153)
    glBegin(GL_POLYGON)
    glVertex2f(900 , 0)
    glVertex2f(900 , 100)
    glVertex2f(600 ,200)
    glVertex2f(600 , -300)
    glVertex2f(800 , -300)
    glEnd()

def gedung3():
    glColor3ub(64, 64, 64)
    glBegin(GL_POLYGON)
    glVertex2f(300 , -300)
    glVertex2f(300 , 100)
    glVertex2f(100 ,100)
    glVertex2f(100 , -300)
    glEnd()

def gedung4():
    glColor3ub(255, 0, 127)
    glBegin(GL_POLYGON)
    glVertex2f(0 , -300)
    glVertex2f(0 , 0)
    glVertex2f(-400 ,0)
    glVertex2f(-400 , -300)
    glEnd()

def gedung5():
    glColor3ub(150, 100, 120)
    glBegin(GL_POLYGON)
    glVertex2f(0 , 0)
    glVertex2f(0 , 200)
    glVertex2f(-200 ,365)
    glVertex2f(-200 , 0)
    glEnd()

def gedung6():
    glColor3ub(200, 200, 200)
    glBegin(GL_POLYGON)
    glVertex2f(-200 , 0)
    glVertex2f(-200 , 400)
    glVertex2f(-600 ,400)
    glVertex2f(-600 , -300)
    glVertex2f(-400 , -300)
    glVertex2f(-400 , 0)
    glEnd()

def gedung8():
    glColor3ub(130, 220, 80)
    glBegin(GL_POLYGON)
    glVertex2f(1300 , -300)
    glVertex2f(1300 , 100)
    glVertex2f(1200 , 200)
    glVertex2f(1100 ,100)
    glVertex2f(1100 , -300)
    glEnd()

def gedung9():
    glColor3ub(190, 20, 280)
    glBegin(GL_POLYGON)
    glVertex2f(320 , -300)
    glVertex2f(320 , 100)
    glVertex2f(360 , 100)
    glVertex2f(360 , 250)
    glVertex2f(530 , 250)
    glVertex2f(530 , 100)
    glVertex2f(570 ,100)
    glVertex2f(570 , -300)
    glEnd()

def jendela(): 
    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-500 , 300)
    glVertex2f(-300 , 300)
    glVertex2f(-300 ,200)
    glVertex2f(-500 , 200)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-500 , 100)
    glVertex2f(-300 , 100)
    glVertex2f(-300 ,0)
    glVertex2f(-500 , 0)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-500 , -100)
    glVertex2f(-400 , -100)
    glVertex2f(-400 ,-200)
    glVertex2f(-500 , -200)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-300 , -100)
    glVertex2f(-100 , -100)
    glVertex2f(-100 ,-250)
    glVertex2f(-300 , -250)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-170 , 300)
    glVertex2f(-65 , 200)
    glVertex2f(-170 ,200)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-170 , 120)
    glVertex2f(-65 , 120)
    glVertex2f(-65 ,20)
    glVertex2f(-170 , 20)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(130 , 40)
    glVertex2f(260 , 40)
    glVertex2f(260 ,-30)
    glVertex2f(130 , -30)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(130 , -100)
    glVertex2f(260 , -100)
    glVertex2f(260 ,-170)
    glVertex2f(130 , -170)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(640 , 140)
    glVertex2f(840 ,85)
    glVertex2f(640 ,85)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(640 , 35)
    glVertex2f(800 , 35)
    glVertex2f(800 ,-40)
    glVertex2f(640 , -40)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(640 , -100)
    glVertex2f(800 , -100)
    glVertex2f(800 ,-190)
    glVertex2f(640 , -190)
    glEnd()
    
    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(850 , -60)
    glVertex2f(960 , -60)
    glVertex2f(960 ,-220)
    glVertex2f(850 , -220)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-950 , 400)
    glVertex2f(-850 , 400)
    glVertex2f(-850 , 300)
    glVertex2f(-950 ,300)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-950 , 200)
    glVertex2f(-850 , 200)
    glVertex2f(-850 , 100)
    glVertex2f(-950 ,100)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-950 , 0)
    glVertex2f(-850 , 0)
    glVertex2f(-850 , -100)
    glVertex2f(-950 ,-100)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-950 , -200)
    glVertex2f(-850 , -200)
    glVertex2f(-850 , -300)
    glVertex2f(-950 ,-300)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(340 , -290)
    glVertex2f(340 , -100)
    glVertex2f(550 ,-100)
    glVertex2f(550 , -290)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(340 , -80)
    glVertex2f(340 , 80)
    glVertex2f(550 ,80)
    glVertex2f(550 , -80)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(370 , 110)
    glVertex2f(370 ,210)
    glVertex2f(520 , 210)
    glVertex2f(520 , 110)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(1260 , -80)
    glVertex2f(1260 ,80)
    glVertex2f(1120 , 80)
    glVertex2f(1120 , -80)
    glEnd()

    glColor3ub(248, 248, 255)
    glBegin(GL_POLYGON)
    glVertex2f(1260 , -290)
    glVertex2f(1260 ,-100)
    glVertex2f(1120 , -100)
    glVertex2f(1120 , -290)
    glEnd()

def trotoar():
    glColor3ub(207, 207, 207)
    glBegin(GL_POLYGON)
    glVertex2f(-1280 , -750)
    glVertex2f(1280 , -750)
    glVertex2f(1280 ,-300)
    glVertex2f(-1280 , -300)
    glEnd()

def jalan():
    global posxjalan,posyjalan, gerakjalan
    if posxjalan <= -1300:
        posxjalan = -600
    posxjalan -= gerakjalan

    glPushMatrix()
    glTranslated(posxjalan, posyjalan, 0)     
    
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-995 , -450)
    glVertex2f(-995 , -600)
    glVertex2f(-610 , -600)
    glVertex2f(-610 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-455 , -450)
    glVertex2f(-455 , -600)
    glVertex2f(-275 , -600)
    glVertex2f(-275 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-150 , -450)
    glVertex2f(-150 , -600)
    glVertex2f(270 , -600)
    glVertex2f(270 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(465 , -450)
    glVertex2f(465 , -600)
    glVertex2f(910 , -600)
    glVertex2f(910 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1065 , -450)
    glVertex2f(1065 , -600)
    glVertex2f(1180 , -600)
    glVertex2f(1180 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1250 , -450)
    glVertex2f(1250 , -600)
    glVertex2f(1500 , -600)
    glVertex2f(1500 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1550 , -450)
    glVertex2f(1550 , -600)
    glVertex2f(1800 , -600)
    glVertex2f(1800 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(1850 , -450)
    glVertex2f(1850 , -600)
    glVertex2f(2000 , -600)
    glVertex2f(2000 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(2050 , -450)
    glVertex2f(2050 , -600)
    glVertex2f(2400 , -600)
    glVertex2f(2400 ,-450)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(2450 , -450)
    glVertex2f(2450 , -600)
    glVertex2f(2600 , -600)
    glVertex2f(2600 ,-450)
    glEnd()
    glPopMatrix()

def aktor():
    global pos_x, pos_y,nyawa,game_over,pos_x_rintangan, pos_y_rintangan,pos_x_rintangan2, pos_y_rintangan2
    glPushMatrix()
    
    if pos_y >= -250:
        pos_x=0
        pos_y = -500
        nyawa -= 1
    if pos_y<= -700:
        pos_y = -500
        nyawa -= 1
       
    #Collision dengan rintangan
    if pos_x==pos_x_rintangan and pos_y-170<=pos_y_rintangan<=pos_y+170:
        pos_x=0
        pos_y=-500
        nyawa -= 1
        print("rintangan1 pada objek posisi x=",pos_x_rintangan,"dan posisi y=",pos_y_rintangan)
        if nyawa <= 0 :
            game_over = True


    #Collision dengan rintangan
    if pos_x==pos_x_rintangan2 and pos_y-150<=pos_y_rintangan2<=pos_y+150:
        pos_x=0
        pos_y=-500
        nyawa -= 1
        print("rintangan2 pada objek posisi x=",pos_x_rintangan,"dan posisi y=",pos_y_rintangan)
        if nyawa <= 0 :
            game_over = True


    glTranslated(pos_x, pos_y, 0)
    # glScaled(5,5,0)

#Rodadepan
    glColor3ub(128, 128, 128)
    glBegin(GL_POLYGON)
    glVertex2f(43.6277811,-2.120677)
    glVertex2f(52.295670,0.244208)
    glVertex2f(58.48701952,-0.168548)
    glVertex2f(61.2566486,3.09392)
    glVertex2f(65.1396114,0.766414)
    glVertex2f(71.35235050,-3.3129)
    glVertex2f(76.72997808,-13.486)
    glVertex2f(78.72997808,-24.2809)
    glVertex2f(76.4002009,-34.5780)
    glVertex2f(68.4401299080,-41.9483)
    glVertex2f(61.83909390,-46.2196)
    glVertex2f(49.80191207,-46.4138)
    glVertex2f(38.15302642,-40.5893)
    glVertex2f(31.45146078,-31.5380)
    glVertex2f(32.32858,-23.3892)
    glVertex2f(32.32858,-17.0974)
    glVertex2f(34.658367,-9.719848)
    glVertex2f(38.54132261,-5.254442)
    glVertex2f(40,-10)
    glVertex2f(37.642810,-14.8214)
    glVertex2f(36.4056935,-20.5921)
    glVertex2f(36.61091855,-27.2041)
    glVertex2f(39.31791499,-32.0468)
    glVertex2f(45.27880,-37.0468)
    glVertex2f(52.295670,-39.8325)
    glVertex2f(61.37631587,-37.7294)
    glVertex2f(67.27524,-33.211)
    glVertex2f(70.575758,-24.8634)
    glVertex2f(70.38161003,-16.7091)
    glVertex2f(67.663536,-10.10814)
    glVertex2f(62.2273900,-5.25442)
    glVertex2f(53.74031837,-3.4706)
    glVertex2f(45.79475,-5.947241)
    glEnd()

#banbelakang
    glColor3ub(128, 128, 128)
    glBegin(GL_POLYGON)
    glVertex2f(-20.6590627,-2.5418)
    glVertex2f(-24.167494039,-0.2717)
    glVertex2f(-30.963695,2.31733)
    glVertex2f(-37.17643405,1.92903)
    glVertex2f(-42.6125806,1.15244)
    glVertex2f(-48.63117160,-2.7305)
    glVertex2f(-55.038058,-8.7491)
    glVertex2f(-60,-20)
    glVertex2f(-59.30931677,-26.804881)
    glVertex2f(-56.397095,-35.153)
    glVertex2f(-52.125837293,-41.171)
    glVertex2f(-43.971617,-45.831)
    glVertex2f(-32.711027,-47.190)
    glVertex2f(-23.97436,-44.278)
    glVertex2f(-16.2084398,-38.842)
    glVertex2f(-10.959282,-28.648)
    glVertex2f(0,-10)
    glVertex2f(-23.58606,-36.512)
    glVertex2f(-34.0700645,-39.230)
    glVertex2f(-43.38917,-36.9005)
    glVertex2f(-48.63117160,-32.241)
    glVertex2f(-51.73754,-25.639)
    glVertex2f(-52.31998538,-18.8448)
    glVertex2f(-50.3785044,-14.185)
    glVertex2f(-47.466283,-8.9432)
    glVertex2f(-39.70035,-4.8661)
    glVertex2f(-33.248139,-5.4311)
    glVertex2f(-25.9217968,-7.3917)
    glEnd()


#Banbelakang2
    glColor3ub(128, 128, 128)
    glBegin(GL_POLYGON)
    glVertex2f(-16.4283073,-7.2886)
    glVertex2f(-13.539112,-11.622)
    glVertex2f(-19.833549,-11.725)
    glEnd()


#Lungguhan
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-2.4977713822098, 17.1672297309584)
    glVertex2f(3.1776321708057, 17.4767971974865)
    glVertex2f(4.3127128814088, 21.191606795824)
    glVertex2f(2.0425514,23.87452)
    glVertex2f(-2.4977777,24.70003)
    glVertex2f(-6.2125898,24.8032)
    glVertex2f(-8.8954,26.971099)
    glVertex2f(-12.3254,29.69272)
    glVertex2f(-17.150631,29.4467)
    glVertex2f(-21.27819,27.0733)
    glVertex2f(-22.82603501,22.9458)
    glVertex2f(-22.033046629,18.4149)
    glVertex2f(-19.3843404011,16.6491)
    glEnd()


#Gagang lungguan
    glColor3ub(104, 27, 148)
    glBegin(GL_POLYGON)
    glVertex2f(-10.133768,16.8576)
    glVertex2f(-8.689120,10.56812)
    glVertex2f(-34.07064,-17.8741)
    glVertex2f(-36.34246,-19.361)
    glVertex2f(-37.3757,-21.425)
    glVertex2f(-36.962949,-24.005)
    glVertex2f(-34.073652,-25.140)
    glVertex2f(-31.80349,-23.695)
    glVertex2f(-31.287545,-20.496)
    glVertex2f(-5.79982435,6.125990)
    glVertex2f(2.7648755,-10.5906)
    glVertex2f(7.717955,-10.7070)
    glVertex2f(7.67177566,-8.943256)
    glVertex2f(-4.8711219,16.4449)
    glEnd()

#rangka2
    glColor3ub(104, 27, 148)
    glBegin(GL_POLYGON)
    glVertex2f(7.7488856,-7.77836)
    glVertex2f(15.82599561,-5.8368)
    glVertex2f(18.932365,-2.73051)
    glVertex2f(23.786067,1.54074)
    glVertex2f(27.08658,4.452961)
    glVertex2f(29.4163621,8.530071)
    glVertex2f(31.55199,12.80132)
    glVertex2f(34.172990502,16.00477)
    glVertex2f(33.205676,21.50117)
    glVertex2f(30,20)
    glVertex2f(28.0462186,17.8895)
    glVertex2f(27.669029,14.1603)
    glVertex2f(24.7568079,9.11251)
    glVertex2f(21.067994,5.22955)
    glVertex2f(17.573328,1.15244)
    glVertex2f(12.913774,-1.95392)
    glVertex2f(2.37649599,-4.915249)
    glEnd()


#rabgka depan
    glColor3ub(33, 3, 50)
    glBegin(GL_POLYGON)
    glVertex2f(28.6396698,41.92354)
    glVertex2f(37.37643,-0.30366)
    glVertex2f(38.54132261,-5.254442)
    glVertex2f(42.35988,-11.6613)
    glVertex2f(49.0253196,-20.10677)
    glVertex2f(51.5492449,-22.9219)
    glVertex2f(54.84976,-25.0575)
    glVertex2f(56.985391,-20.3979)
    glVertex2f(52.90828,-18.0682)
    glVertex2f(49.996060,-14.9618)
    glVertex2f(45.9189501907,-7.584219)
    glVertex2f(43.58917,-3.89540)
    glVertex2f(41.976754,1.172910)
    glVertex2f(34.7554347,41.632321)
    glEnd()

#setir
    glColor3ub(16, 1, 24)
    glBegin(GL_POLYGON)
    glVertex2f(15.82599,50.36898)
    glVertex2f(15.82599,43.96209)
    glVertex2f(34.7554347,41.632321)
    glVertex2f(34.54713544,50.80689)
    glEnd()

#rangkaneh
    glColor3ub(33, 3, 50)
    glBegin(GL_POLYGON)
    glVertex2f(35.43495311,7.17103)
    glVertex2f(16.990884180,-10.4964)
    glVertex2f(21.2621422,-14.5735)
    glVertex2f(36.01739,2.89977)
    glEnd()


#keranjang
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(35.2694595,44.71873)
    glVertex2f(55.820505298,43.865024)
    glVertex2f(59.12102058,42.50698)
    glVertex2f(60.091761,38.42887)
    glVertex2f(54.267318,19.59651)
    glVertex2f(51.937541,17.46088)
    glVertex2f(39.190647,16.94085)
    glEnd()


#Slebordepan1
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(41.976754,1.172910)
    glVertex2f(46.30724637,4.84125)
    glVertex2f(52.19248103,5.71323)
    glVertex2f(57.4551279,5.30647)
    glVertex2f(61.2566486,3.09392)
    glVertex2f(58.48701952,-0.168548)
    glVertex2f(52.295670,0.244208)
    glVertex2f(43.6277811,-2.120677)
    glEnd()


#Slebordepan2
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(37.37643,-0.30366)
    glVertex2f(38.54132261,-5.254442)
    glVertex2f(34.658367,-9.719848)
    glVertex2f(32.32858,-17.0974)
    glVertex2f(32.32858,-23.3892)
    glVertex2f(31.451460,-31.5380)
    glVertex2f(26.8924369,-27.3873)
    glVertex2f(27.0865850699,-15.7384)
    glVertex2f(30.9695469,-7.39007)
    glEnd()




#sleborbelakang1
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-18.149928,2.3573)
    glVertex2f(-28.82866,6.68859)
    glVertex2f(-37.272516,7.77701)
    glVertex2f(-49.796616,4.64710)
    glVertex2f(-56.785391,-1.5656)
    glVertex2f(-61.444945,-9.7198)
    glVertex2f(-62.99813055,-16.126)
    glVertex2f(-60,-20)
    glVertex2f(-55.038058,-8.7491)
    glVertex2f(-48.63117160,-2.7305)
    glVertex2f(-42.6125806,1.15244)
    glVertex2f(-37.17643405,1.92903)
    glVertex2f(-30.963695,2.31733)
    glVertex2f(-24.167494039,-0.2717)
    glVertex2f(-20.6590627,-2.5418)
    glEnd()


#sleorbelakang2
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(-12.907922,-2.7305)
    glVertex2f(-7.7604183,-11.0034)
    glVertex2f(-13.539112,-11.622)
    glVertex2f(-16.4283073,-7.2886)
    glEnd()




#pancalan
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-26.334466,-21.941)
    glVertex2f(-24.5568794,-15.941)
    glVertex2f(-19.833549,-11.725)
    glVertex2f(-13.539112,-11.622)
    glVertex2f(-7.7604183,-11.0034)
    glVertex2f(2.76487554,-10.59065)
    glVertex2f(10.9168188,-11.4163)
    glVertex2f(15.35395,-12.8448)
    glVertex2f(19.378329,-15.8533)
    glVertex2f(21.65043843,-19.3155)
    glVertex2f(19.514509,-27.7756)
    glVertex2f(14.27281086,-32.8234)
    glVertex2f(6.50688710,-33.4059)
    glVertex2f(2.6239252,-31.85273)
    glVertex2f(-0.094148094,-28.8581)
    glVertex2f(-3.3232846,-25.5530)
    glVertex2f(-14.4677134,-24.005)
    glEnd()


#pancalan2
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(4.209523725,-41.9601)
    glVertex2f(15.25076,-42.0633)
    glVertex2f(15.86989298,-36.3879)
    glVertex2f(11.741332078,-36.3879)
    glVertex2f(11.53595376,-27.372)
    glVertex2f(11.32957545,-22.3478)
    glVertex2f(8.440279,-21.83827)
    glVertex2f(7.6147658577,-26.63816)
    glVertex2f(7.30519839,-36.28475)
    glVertex2f(3.59466569,-35.92984)
    glEnd()


#Jeruji depan1
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(49.819130,-22.6637)
    glVertex2f(36.1981619338053,-24.0052)
    glVertex2f(36.5077294,-21.127)
    glEnd()


#Jeruji depan2
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(50.851022,-25.3467)
    glVertex2f(42.595889575,-35.8719)
    glVertex2f(40.22253899,-34.0145)
    glEnd()


#Jeruji depan3
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(53.74031837,-26.2913)
    glVertex2f(55.288155703,-39.0708)
    glVertex2f(52.39885934,-38.6681)
    glEnd()


#Jeruji depan4
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(56.62961472,-25.3543)
    glVertex2f(64.059233921,-35.2688)
    glVertex2f(67.15490858,-33.395)
    glEnd()


#Jeruji depan5
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(57.8678845,-22.3542)
    glVertex2f(70.8697181849,-24.2116)
    glVertex2f(70,-20)
    glEnd()


#Jeruji depan6
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(56.985391554,-20.3979)
    glVertex2f(66.94853027,-11.8289)
    glVertex2f(65.1943146,-9.146002)
    glEnd()


#Jeruji depan7
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(53.53394005,-18.020272)
    glVertex2f(51.88291357,-4.91524)
    glVertex2f(55.49453414,-5.01843)
    glEnd()


#jerujibelakang1
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-35.235536766,-17.813)
    glVertex2f(-32.62900479,-5.0184)
    glVertex2f(-36.343814389,-4.9152)
    glEnd()


#jerujibelakang2
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-37.891651721,-19.461)
    glVertex2f(-48.62332389,-11.2097)
    glVertex2f(-46.559540784,-9.0428)
    glEnd()


#jerujibelakang3
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-39.129921588,-22.354)
    glVertex2f(-52.9572684,-21.6318)
    glVertex2f(-52.7508901,-24.314)
    glEnd()


#jerujibelakang4
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-37.582084255,-25.140)
    glVertex2f(-49.2424588,-34.0145)
    glVertex2f(-46.559540784,-36.183)
    glEnd()


#jerujibelakang5
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-34.7959770566,-25.965)
    glVertex2f(-36.5501927003,-39.896)
    glVertex2f(-33.041761,-39.689)
    glEnd()


#jerujibelakang6
    glColor3ub(192, 192, 192)
    glBegin(GL_POLYGON)
    glVertex2f(-31.803491,-24.521)
    glVertex2f(-23.44516995,-35.768)
    glVertex2f(-21.27819768,-33.085)
    glEnd()
    glPopMatrix()

def Rintangan():
    global pos_x_rintangan, pos_y_rintangan
    
    if pos_x_rintangan <= -1300:
        pos_x_rintangan = 1300
        pos_y_rintangan = rd.randrange(-700,-250)
  
    glPushMatrix()
    # glScaled(2,2,0)
    glTranslated(pos_x_rintangan, pos_y_rintangan+jedagJedug(), 0)
    pos_x_rintangan-=rd.randrange(3,5)


    # glScaled(0.5,0.5,0)
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0, 74.3491451531488)

    glColor3ub(139, 0, 0)
    glVertex2f(23.31764158,83.42883)

    glColor3ub(139, 0, 0)
    glVertex2f(30.7912386027,67.673443)

    glColor3ub(139, 0, 0)
    glVertex2f(49.9236029,63.58709)

    glColor3ub(139, 0, 0)
    glVertex2f(60,60)
    
    glColor3ub(139, 0, 0)
    glVertex2f(56.361936,48.488426)

    glColor3ub(0, 0, 0)
    glVertex2f(47.6688604, 32.9226006)

    glColor3ub(0, 0, 0)
    glVertex2f(67.87966025,30.333926)

    glColor3ub(0, 0, 0)
    glVertex2f(73.05034899,13.836252)

    glColor3ub(0, 0, 0)
    glVertex2f(74.17795539,-5.042451)

    glColor3ub(139, 0, 0)
    glVertex2f(80,-20)

    glColor3ub(139, 0, 0)
    glVertex2f(69.750063,-25.74342)

    glColor3ub(139, 0, 0)
    glVertex2f(47.380784,-57.29621)

    glColor3ub(139, 0, 0)
    glVertex2f(40,-80)

    glColor3ub(139, 0, 0)
    glVertex2f(37.297044996,-87.4806)

    glColor3ub(0, 0, 0)
    glVertex2f(28.7409736,-68.56932)

    glColor3ub(0, 0, 0)
    glVertex2f(13.0519613688182,-73.19454)

    glColor3ub(0, 0, 0)
    glVertex2f(-10.6458122322,-73.58302)

    glColor3ub(0, 0, 0)
    glVertex2f(-12.75823817,-57.26703)

    glColor3ub(139, 0, 0)
    glVertex2f(-15.01298066,-40.131)

    glColor3ub(139, 0, 0)
    glVertex2f(-25.83574459,-42.3857)

    glColor3ub(139, 0, 0)
    glVertex2f(-40.717044996,-32.915)

    glColor3ub(139, 0, 0)
    glVertex2f(-61.00972736,-30.210)

    glColor3ub(139, 0, 0)
    glVertex2f(-72.4675986,-16.6205)

    glColor3ub(139, 0, 0)
    glVertex2f(-73.69878468,9.812467)

    glColor3ub(139, 0, 0)
    glVertex2f(-103.849834,6.881)

    glColor3ub(139, 0, 0)
    glVertex2f(-88.5175856,32.9226)

    glColor3ub(139, 0, 0)
    glVertex2f(-69.5777488,46.90204)

    glColor3ub(139, 0, 0)
    glVertex2f(-56.951198907,52.313)

    glColor3ub(139, 0, 0)
    glVertex2f(-12.1324153,73.35257)
    glEnd()
    glPopMatrix()

def Rintangan2():
    global pos_x_rintangan2, pos_y_rintangan2
    
    if pos_x_rintangan2 <= -1300:
        pos_x_rintangan2 = 1300
        pos_y_rintangan2 = rd.randrange(-700,-250)
    pos_x_rintangan2 -= rd.randrange(4,5)

    glPushMatrix()
    glTranslated(pos_x_rintangan2, pos_y_rintangan2+jedagJedug2(), 0)


    # glScaled(0.5,0.5,0)
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0, 74.3491451531488)

    glColor3ub(139, 0, 0)
    glVertex2f(23.31764158,83.42883)

    glColor3ub(139, 0, 0)
    glVertex2f(30.7912386027,67.673443)

    glColor3ub(139, 0, 0)
    glVertex2f(49.9236029,63.58709)

    glColor3ub(139, 0, 0)
    glVertex2f(60,60)
    
    glColor3ub(139, 0, 0)
    glVertex2f(56.361936,48.488426)

    glColor3ub(0, 0, 0)
    glVertex2f(47.6688604, 32.9226006)

    glColor3ub(0, 0, 0)
    glVertex2f(67.87966025,30.333926)

    glColor3ub(0, 0, 0)
    glVertex2f(73.05034899,13.836252)

    glColor3ub(0, 0, 0)
    glVertex2f(74.17795539,-5.042451)

    glColor3ub(139, 0, 0)
    glVertex2f(80,-20)

    glColor3ub(139, 0, 0)
    glVertex2f(69.750063,-25.74342)

    glColor3ub(139, 0, 0)
    glVertex2f(47.380784,-57.29621)

    glColor3ub(139, 0, 0)
    glVertex2f(40,-80)

    glColor3ub(139, 0, 0)
    glVertex2f(37.297044996,-87.4806)

    glColor3ub(0, 0, 0)
    glVertex2f(28.7409736,-68.56932)

    glColor3ub(0, 0, 0)
    glVertex2f(13.0519613688182,-73.19454)

    glColor3ub(0, 0, 0)
    glVertex2f(-10.6458122322,-73.58302)

    glColor3ub(0, 0, 0)
    glVertex2f(-12.75823817,-57.26703)

    glColor3ub(139, 0, 0)
    glVertex2f(-15.01298066,-40.131)

    glColor3ub(139, 0, 0)
    glVertex2f(-25.83574459,-42.3857)

    glColor3ub(139, 0, 0)
    glVertex2f(-40.717044996,-32.915)

    glColor3ub(139, 0, 0)
    glVertex2f(-61.00972736,-30.210)

    glColor3ub(139, 0, 0)
    glVertex2f(-72.4675986,-16.6205)

    glColor3ub(139, 0, 0)
    glVertex2f(-73.69878468,9.812467)

    glColor3ub(139, 0, 0)
    glVertex2f(-103.849834,6.881)

    glColor3ub(139, 0, 0)
    glVertex2f(-88.5175856,32.9226)

    glColor3ub(139, 0, 0)
    glVertex2f(-69.5777488,46.90204)

    glColor3ub(139, 0, 0)
    glVertex2f(-56.951198907,52.313)

    glColor3ub(139, 0, 0)
    glVertex2f(-12.1324153,73.35257)
    glEnd()
    glPopMatrix()

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()

def play_game():
    global nyawa
    background1()
    kgedung()
    fullmatahari()
    fullawan1()
    jendela()
    trotoar()
    jalan()
    aktor()
    Rintangan()
    Rintangan2()
    drawTextBold("nyawa : "+str(nyawa),1000,700) 
    if nyawa <= 0:
        endgame()

def mySpecialKeyboard(key, x, y):
    global pos_x, pos_y, gerak,game_over,nyawa,play
    gerak = 50

    if key == GLUT_KEY_UP:
        pos_y += gerak
        print("posisi x,y adalah",pos_x,pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= gerak
        print("posisi x,y adalah",pos_x,pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x += gerak
        print("posisi x,y adalah",pos_x,pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x -= gerak
        print("posisi x,y adalah",pos_x,pos_y)
    
def mouse_play_game(button, state, x, y):
    global play
    if button == GLUT_LEFT_BUTTON:
        play = True

def mykeyBoard(key,x,y):
    global play,nyawa,game_over
    if ord(key) == ord(b'\r'):
        play = False
        game_over = False
        nyawa = 3

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1280, w, -750, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if play == False:
        start_game()
    else:
        play_game()
    glutSwapBuffers()
   
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(50,0)
glutCreateWindow("RICLE")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard)
glutKeyboardFunc(mykeyBoard)
glutMouseFunc(mouse_play_game)
glutMainLoop()
