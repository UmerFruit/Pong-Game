import pygame
from Paddle import *
pygame.init()
winHeight, winWidth = 500, 700
padHeight, padWidth = 100, 20
WIN = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("PONG")
FPS = 60
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
ball_rad = 13
scoreFont = pygame.font.SysFont("comicsans",50)

def padMove(keys, left_P, right_P):
    if keys[pygame.K_w]:
        if left_P.y > 0:
            left_P.move(up=True)
    if keys[pygame.K_s]:
        if left_P.y + padHeight < winHeight:
            left_P.move(up=False)
    if keys[pygame.K_UP]:
        if right_P.y > 0:
            right_P.move(up=True)
    if keys[pygame.K_DOWN]:
        if right_P.y + padHeight < winHeight:
            right_P.move(up=False)

def draw(WIN, paddles, ball,left_S,right_S):
    WIN.fill(BLACK)

    left_score_text = scoreFont.render(f"{left_S}",1,WHITE)
    right_score_text = scoreFont.render(f"{right_S}",1,WHITE)
    WIN.blit(left_score_text,(winWidth//4-left_score_text.get_width()//2,20))
    WIN.blit(right_score_text,(winWidth*(3/4)-right_score_text.get_width()//2,20))


    for paddle in paddles:
        paddle.draw(WIN)
    for i in range(10, winHeight, winHeight//20):
        pygame.draw.rect(WIN, WHITE, (winWidth//2, i, 5, 10))
    
    
    ball.draw(WIN)
    pygame.display.update()


def collision(ball, lp, rp):
    if ball.y+ball.rad >= winHeight:
        ball.y_vel *= -1
    elif ball.y - ball.rad <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= lp.y and ball.y <= lp.y + lp.height:
            if ball.x - ball.rad <= lp.x + lp.width:
                ball.x_vel *= -1

                middle_y = lp.y + lp.height/2
                diffinY = middle_y - ball.y
                reductionFactor = (lp.height/2)/ball.maxv
                y_vel = diffinY/reductionFactor
                ball.y_vel = -1*y_vel
    else:
        if ball.y >= rp.y and ball.y <= rp.y + rp.height:
            if ball.x + ball.rad >= rp.x:
                ball.x_vel *= -1

                middle_y = rp.y + rp.height/2
                diffinY = middle_y - ball.y
                reductionFactor = (rp.height/2)/ball.maxv
                y_vel = diffinY/reductionFactor
                ball.y_vel = -1*y_vel


def main():
    run = True
    clock = pygame.time.Clock()
    left_P = Paddle(10, winHeight//2-padHeight//2, padWidth, padHeight)
    right_P = Paddle(winWidth - 10 - padWidth, winHeight //
                     2-padHeight//2, padWidth, padHeight)
    ball = Ball(winWidth//2, winHeight//2, ball_rad)

    left_score = 0
    right_score = 0
    winning_score = 5

    while (run):
        clock.tick(FPS)
        draw(WIN, [left_P, right_P], ball,left_score,right_score)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
                break
        keys = pygame.key.get_pressed()
        padMove(keys, left_P, right_P)
        ball.move()
        collision(ball, left_P, right_P)

        if ball.x < 0:
            right_score += 1
            ball.reset()
            left_P.reset()
            right_P.reset()
        elif ball.x >winWidth:
            left_score += 1
            ball.reset()
            left_P.reset()
            right_P.reset()
        won = False
        if left_score>=winning_score:
            won = True
            win_text = "Left Player Won!"
        elif right_score>=winning_score:
            won = True
            win_text = "Right Player Won!"

        if won == True:
            text = scoreFont.render(win_text,1,WHITE)
            WIN.blit(text,(winWidth//2 - text.get_width()//2,winHeight//2-  text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            left_P.reset()
            right_P.reset()
            ball.reset()
            left_score = 0
            right_score = 0
    pygame.quit()

if __name__ == "__main__":
    main()
