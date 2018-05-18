import pygame
import playerShip
import enemyShip


def main():
    # Initialize pygame module
    pygame.init()

    # Set basic elements
    gameDisplay = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Pozaziemscy zaborcy')
    myfont = pygame.font.SysFont('monospace', 15)

    # Set timer
    clock = pygame.time.Clock()

    # Set font
    label = myfont.render("Points: 0", 1, (0, 0, 0))

    # Set booleans
    gameExit = False
    bulletDisplay = False
    showEnemy = True

    # Set variables
    points = 0

    # Set starting objects
    entities = []
    entities.append(playerShip.PlayerShip())
    #player = playerShip.PlayerShip()
    entities.append(enemyShip.EnemyShip())
    # enemy = enemyShip.EnemyShip()

    # Main game loop
    while not gameExit:
        # Event-catching loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(-1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_RETURN and not bulletDisplay:
                    bul = entities[0].shoot()
                    bulletDisplay = True
                if event.key == pygame.K_q:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(-1)

        # Fill screen with white color
        gameDisplay.fill((255, 255, 255))

        # Check player condition
        entities[0].draw(gameDisplay)
        # Check enemy condition
        if showEnemy:
            entities[1].draw(gameDisplay)
            if entities[1].check_player(entities[0]):
                del entities[1]
                showEnemy = False
                points -= 10

        # Check bullet condition
        if bulletDisplay:
            bul.move()
            pygame.draw.rect(gameDisplay, (0, 0, 0), [bul.x, bul.y, 2, 10])
            if bul.y == 0:
                del bul
                bulletDisplay = False
            elif showEnemy:
                if entities[1].check_bullet(bul):
                    del bul
                    del entities[1]
                    bulletDisplay = False
                    showEnemy = False
                    points += 10

        # Update display, maintain stable framerate
        label = myfont.render("Points: " + str(points), 1, (0, 0, 0))
        gameDisplay.blit(label, (10, 10))
        pygame.display.update()
        clock.tick(120)
        clock.get_fps()

    # Exit game
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
