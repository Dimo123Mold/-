import pygame

pygame.init()

win_width = 700
win_height = 500
FPS = 20

win = pygame.display.set_mode((win_width, win_height + 50))
clock = pygame.time.Clock()

player_image = "chara.png"
bullet_image = "bullet.png"
main_background_image = pygame.transform.scale(
                    pygame.image.load('fon1.png'),
                    (win_width, win_height)
                    )
dog_image = ["enemy1.png", "enemy2.png", "enemy3.png"]

background_image = pygame.transform.scale(
                    pygame.image.load('fon2.png'),
                    (win_width, win_height)
                    )


bullets = pygame.sprite.Group()
enamys = pygame.sprite.Group()


bac = (150 , 150 , 150)
UI = pygame.Rect(0, win_height,win_width, 50 )
ui_d = pygame.font.Font(None, 50)



bt_start_text = ui_d.render("START", True, (100, 255, 100))