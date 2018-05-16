import pygame
import playerShip
import bullet
import enemyShip


def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Pozaziemscy zaborcy')

    clock = pygame.time.Clock()
    x = 255


    gameExit = False
    bulletDisplay = False
    showEnemy = True

    player = playerShip.PlayerShip()
    enemy = enemyShip.EnemyShip()

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.addVelocity(-1)
                if event.key == pygame.K_d:
                    player.addVelocity(1)
                if event.key == pygame.K_o:
                    bul = bullet.Bullet(player.s_x)
                    bulletDisplay = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.addVelocity(1)
                if event.key == pygame.K_d:
                    player.addVelocity(-1)
                #if event.key == pygame.K_o:
                    #del bul

        if player.check_walls():
            player.s_x += player.velocity

        gameDisplay.fill((x, x, x))
        pygame.draw.rect(gameDisplay, (0, 0, 0), [player.s_x, player.s_y, 30, 30])

        if showEnemy:
            pygame.draw.rect(gameDisplay, (0, 0, 0), [enemy.s_x, enemy.s_y, 30, 30])

        if bulletDisplay and showEnemy == True:
            bul.move()
            pygame.draw.rect(gameDisplay, (0, 0, 0), [bul.x, bul.y, 2, 10])
            if enemy.check_bullet(bul):
                del enemy
                showEnemy = False

        pygame.display.update()
        clock.tick(120)
        clock.get_fps()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
