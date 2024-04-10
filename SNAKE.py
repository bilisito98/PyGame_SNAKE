import pygame, sys, time, random

speed = 15

frame_size_x = 800
frame_size_y = 600
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Error " + check_errors[1])
else:
    print("Game Succesfullt init")

    #init

pygame.display.set_caption("SNAKE GAME")
game_window = pygame.display.set_mode(frame_size_x, frame_size_y)


black = pygame.color(0,0,0)
white = pygame.color(255,255,255)
red = pygame.color(255,0,0)
green = pygame.color(0,255,0)
blue = pygame.color(0,0,255)

fps_controller = pygame.time.Clock()

square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, directiion
    direction = "RIGHT"
    Head_Pos = [120, 60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0

init_vars()

def show_score():
    print("showing score")

#game loop

while True:
    for event in pygame.evvent.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygmae.KEYDOWN:
            if ( event.key == pygame.K_UP or event.key == ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif ( event.key == pygame.K_DOWN or event.key == ord("s")
                  and direction != "UP"):
                  direction = "DOWN"
            elif ( event.key == pygame.K_LEFT or event.key == ord("a")
                  and direction != "RIGHT"):
                  direction = "LEFT"
            elif ( event.key == pygame.K_LEFT or event.key == ord("d")
                  and direction != "LEFT"):
                  direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size
    
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    #eating apple
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # spawn food
    if not food_spawn:
        food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
            random.randrange(1,(frame_size_y // square_size)) * square_size]
        food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            square_size -2, square_size -2 ))
        
    pygame.draw.rect(game_window,red, pygame.Rect(food_pos[0], 
                    food_pos[1], square_size, square_size))
    
    # game over condiditons

    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()

    show_score(1,white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)