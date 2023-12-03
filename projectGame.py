import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Inisialisasi Pygame
pygame.init()
pygame.mixer.init()

width, height = 600, 400
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Pick it Up!")

#sound
bgsound = pygame.mixer.Sound("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/sound/Soundtrack PickItUp.mp3")

# images
mainmenu_pict = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/BGMenu.png")
bg = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/BGPlay.png")
basket = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/Basket.png")
bola = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/ballOri.png")
voli = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/VolleyBall.png")
bomb = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/bomb.png")
gameOver = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/GameOver.png")
RingBasket = pygame.image.load("C:/Aqil/Kuliah/Sem 3/Grafkom/Project_PickitUp/img/Ring.png")

# Inisialisasi OpenGL       
glOrtho(0, width, height, 0, -1, 1)


# Karakter
ring_size = 70
ring_x = width // 2 - ring_size // 2
ring_y = height - ring_size
ring_speed = 10


# ball
ball_types = [
    {'image': basket, 'size': 30, 'speed': 2, 'is_bomb': False},
    {'image': voli, 'size': 30, 'speed': 2, 'is_bomb': False},
    {'image': bola, 'size': 30, 'speed': 2, 'is_bomb': False},
    {'image': bomb, 'size': 30, 'speed': 2, 'is_bomb': True}
]
num_ball = 4    
num_bombs = 2

ball_list = [
    { 
        'type': random.choice(ball_types),
        'x': random.randint(0, width - 30),
        'y': random.randint(-50, 0),  # Koordinat awal di luar layar
    } for i in range(num_ball   - num_bombs)
]

for i in range(num_bombs):
    ball_list.append({
        'type': random.choice(ball_types),
        'x': random.randint(0, width - 30),
        'y': random.randint(-15, 0),
    })


def button_MM():
    glPushMatrix()
    glBegin(GL_QUADS)
    glVertex2f(240, 205)
    glVertex2f(240, 255)
    glVertex2f(360, 255)
    glVertex2f(360, 205)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(240, 135)
    glVertex2f(240, 180)
    glVertex2f(360, 180)
    glVertex2f(360, 135)
    glEnd()
    glPopMatrix()

def draw_background():
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex2f(0, 0)

    glTexCoord(1 , 0)
    glVertex2f(width, 0)

    glTexCoord(1, 1)
    glVertex2f(width, height)

    glTexCoord(0, 1)
    glVertex2f(0, height)
    glEnd()

def draw_Ball():
    for ball in ball_list:
      image = ball['type']['image']
      size = ball['type']['size']
      glBegin(GL_QUADS)
      glTexCoord(0, 1)
      glVertex2f(ball['x'], ball['y'])

      glTexCoord(1, 1)
      glVertex2f(ball['x'] + size, ball['y'])

      glTexCoord(1, 0)
      glVertex2f(ball['x'] + size, ball['y'] + size)

      glTexCoord(0, 0)
      glVertex2f(ball['x'], ball['y'] +  size)             
      glEnd()


def draw_ring():
    glBegin(GL_QUADS)
    glVertex2f(ring_x, ring_y)
    glVertex2f(ring_x + ring_size, ring_y)
    glVertex2f(ring_x + ring_size, ring_y + ring_size)
    glVertex2f(ring_x, ring_size + ring_size)
    glEnd()


def draw_text(text, x, y): 
    render_text = font.render(text, True, (255, 255, 255))
    pygame.display.get_surface().blit(render_text, (x, y))


# Skor
score = 0
font = pygame.font.SysFont(None, 30)
# nyawa
lives = 10


def resetgame():
    global ring_x, ball_list, ring_speed, lives, score
    score = 0
    lives = 10
    for ball in ball_list:
        ball['type']['speed'] = 2
    ring_x = width // 2 - ring_size // 2
    # Tambahan: Atur ulang posisi makanan jika ada
    ball_list = [
      { 
          'type': random.choice(ball_types),
          'x': random.randint(0, width - 30),
          'y': random.randint(-15, 0),  # Koordinat awal di luar layar
      } for _ in range(num_ball - num_bombs)
    ]

    for _ in range(num_bombs):
        ball_list.append({
            'type': random.choice(ball_types),
            'x': random.randint(0, width - 30),
            'y': random.randint(400, 450),
      })

def is_button_clicked(x, y, button_x, button_y, button_width, button_height):
    return (
        x >= button_x and
        x <= button_width and
        y >= button_y and
        y <= button_height
    )

clock = pygame.time.Clock()

run = True
show_menu = True
paused = False
start = False
gameover = False

while run:
    # Set frame rate
    clock.tick(60)

    if show_menu:
        screen.blit(mainmenu_pict,(0,0))
    
    if gameover:
        screen.blit(gameOver, (0,0))

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN and show_menu == True:
            if is_button_clicked(event.pos[0], event.pos[1], 240, 135, 360, 180):
                show_menu = False  # Klik tombol "Start", jadi sembunyikan menu
                volume = 0.2  # Ini akan mengatur volume ke 50%
                bgsound.set_volume(volume)
                bgsound.play()
                start = True
            
            elif is_button_clicked(event.pos[0], event.pos[1], 240, 205, 360, 255):
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONDOWN and gameover == True:
            if is_button_clicked(event.pos[0], event.pos[1], 240, 135, 360, 180):
                gameover = False  # Klik tombol "Start", jadi sembunyikan menu
                volume = 0.2  # Ini akan mengatur volume ke 50%
                bgsound.set_volume(volume)
                bgsound.play()
                start = True
            
            elif is_button_clicked(event.pos[0], event.pos[1], 240, 205, 360, 255):
                pygame.quit()
                quit()
            
    
    if start:

        if keys[pygame.K_LEFT] and ring_x > 0:
            ring_x -= ring_speed
        if keys[pygame.K_RIGHT] and ring_x < width - ring_size:
            ring_x += ring_speed
        

        screen.blit(bg,(0,0))
        pygame.time.wait(10)

        screen.blit(RingBasket,(ring_x,ring_y))
        for ball in ball_list:
          screen.blit(ball['type']['image'], (ball['x'], ball['y']))


        # Deteksi makanan oleh burung
        for ball in ball_list:
          ball['y'] += ball['type']['speed']
          size = ball['type']['size']
          if ball['y'] > height:
            if not ball['type']['is_bomb'] :
                ball['x'] = random.randint(0, width - 30)
                ball['y'] = random.randint(-15, 0)
                ball['type'] = random.choice(ball_types)
                if ball['type']['speed'] -2 <= 4:
                    ball['type']['speed'] = 2
                else:
                    ball['type']['speed'] -= 2
                lives -= 1
                if lives == 0:
                    print(f"Game Over. Skor Anda: {score}")
                    start = False
                    gameover = True
                    resetgame()
            else:
                ball['x'] = random.randint(0, width - 30)
                ball['y'] = random.randint(-15, 0)
                ball['type'] = random.choice(ball_types)

          elif (
                ring_x < ball['x'] + size
                and ring_x + ring_size > ball['x']
                and ring_y < ball['y'] + size
                and ring_y + ring_size > ball['y']
                ):
              if ball['type']['is_bomb']:
                  if ball['type']['speed'] -2 <= 4:
                      ball['type']['speed'] = 2

                  else:
                      ball['type']['speed'] -= 2

                  ball['x'] = random.randint(0, width - 30)
                  ball['y'] = random.randint(-15, 0)
                  ball['type'] = random.choice(ball_types)
                  lives -= 1
                  if lives == 0:
                    print(f"Game Over. Skor Anda: {score}")
                    start = False
                    gameover = True
                    resetgame()
              else:
                  score += 1
                  if score % 10 == 0:
                      for ball in ball_list:
                          ball['type']['speed'] += 1
                  ball['x'] = random.randint(0, width - 30)
                  ball['y'] = random.randint(-15, 0)
                  ball['type'] = random.choice(ball_types)
              
            
    glClear(GL_COLOR_BUFFER_BIT)

    if start == True:
        for ball in ball_list:
            draw_text(f"Skor  : {score}", 10, 10)
            draw_text(f"Nyawa : {lives}", 10, 30)
            draw_text(f"Speed : {ball['type']['speed']}", 10, 50)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(pygame.display.get_surface(), 'RGBA'))
    draw_background()

    glDisable(GL_TEXTURE_2D)

    pygame.display.flip()