import pygame
import sys

pygame.init()

width = 800
height = 600
ballPos = [200, 300]
boardPos = [200, 500]

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
ballSpeed = [3, 3]
score = 0
font = pygame.font.Font(None, 36)

# Create a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Block Breaker")

# Game Loop
run = True
while run:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
                sys.exit()
    
    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        boardPos[0] -= 5
    if keys[pygame.K_RIGHT]:
        boardPos[0] += 5

    # Update
    ballPos[0] += ballSpeed[0]
    ballPos[1] += ballSpeed[1]
    
    if ballPos[0] > width or ballPos[0] < 0:
        ballSpeed[0] *= -1
        if ballPos[0] > width:
            ballPos[0] = width
        else:
            ballPos[0] = 0
            
    if ballPos[1] > height: # Collision with floor
        ballSpeed = [3, -3]
        ballPos = [200, 300]
        score -= 10
        
    
    if ballPos[1] < 0: # Collision with ceiling
        ballSpeed[1] *= -1
        ballPos[1] = 0
        
    if ( # Collision with board
        ballPos[0] + 10 >= boardPos[0]
        and ballPos[0] - 10 <= boardPos[0] + 90
        and ballPos[1] + 10 >= boardPos[1]
        and ballPos[1] - 10 <= boardPos[1] + 10
    ):
        ballSpeed[1] *= -1
        score += 10
        
    # Draw
    screen.fill(black)
    pygame.draw.circle(screen, red, (ballPos[0], ballPos[1]), 10)
    pygame.draw.rect(screen, white, (boardPos[0], boardPos[1], 90, 10))
    
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (width - score_text.get_rect().width - 5, 10))

    # Refresh
    pygame.display.flip()
    pygame.time.Clock().tick(80)

pygame.quit()
