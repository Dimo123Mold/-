from objects import *

finish = True
pause = False
game = False

player = Player(player_image, 350, 250, 100, 100, 5)

for i in range (15):
    e = Enamy(dog_image[0], 100, 100, 50, 50, 2 )
    e.spawn()
    enamys.add(e)


def callback_start():
    global finish, game, player, enamy
    finish = False
    game = True
    player = Player(player_image, 350, 250, 100, 100, 5)
    enamys.empty()
    for i in range (15):
        e = Enamy(dog_image[0], 100, 100, 50, 50, 2 )
        e.spawn()
        enamys.add(e)

bt_start = Button(win_width / 2, 100, 150, 50, (50, 50, 100), bt_start_text, callback_start)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    if finish:
        win.blit(main_background_image, (0, 0))
        bt_start.update()
        bt_start.draw()
    if game:
        win.blit(background_image, (0, 0))
        for enamy in enamys:
            dx = enamy.rect.centerx - player.rect.centerx
            dy = player.rect.centery - enamy.rect.centery
            ang = -math.atan2(dy, dx) - math.pi
            enamy.update(ang)
            enamy.draw()
            if player.hitbox.colliderect(enamy.hitbox):
                player.hp -= enamy.damage
                enamy.spawn()
        colllade = pygame.sprite.groupcollide(enamys, bullets, False, True)

        for enamy in colllade:
            enamy.hp -= 1
            if enamy.hp <= 0:
                enamy.spawn()


        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)

        pygame.draw.rect(win, bac, UI)

        hel = ui_d.render(f"HP: {player.hp}/100",
                          True,
                          (255, 50, 50))
        win.blit(hel, (0, win_height + 5))

        if player.hp <= 0:
            game = False
            finish = True
            lose_text = ui_d.render(f"Dead", True, (0, 0, 0))

    pygame.display.update()
    clock.tick(FPS)