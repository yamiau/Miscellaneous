import pygame
import ctypes


# Rule functions
def initialize_grid(size):
    return [[False for i in range(size[0])] for j in range(size[1])]


def run_life(grid):
    next_grid = [[False for i in range(len(grid))] for j in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid)):
            neighbors = count_neighbors(grid, (row, col))
            if grid[row][col]:
                if neighbors < 2 or neighbors > 3:
                    next_grid[row][col] = False
                else:
                    next_grid[row][col] = True
            else:
                if neighbors == 3:
                    next_grid[row][col] = True

    return next_grid


def count_neighbors(grid, pos):
    search = [(pos[0] - 1, pos[1]),
              (pos[0] + 1, pos[1]),
              (pos[0], pos[1] - 1),
              (pos[0], pos[1] + 1),
              (pos[0] - 1, pos[1] - 1),
              (pos[0] - 1, pos[1] + 1),
              (pos[0] + 1, pos[1] - 1),
              (pos[0] + 1, pos[1] + 1)]
    neighbors = 0

    for i in search:
        try:
            if grid[i[0]][i[1]] == True:
                neighbors += 1
        except IndexError:
            pass
        continue
    return neighbors


# System display info extraction
user32 = ctypes.windll.user32
screen_height = user32.GetSystemMetrics(1) * 0.8
screensize = screen_height, screen_height

# Game screen set up
pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game of Life")

# Game mechanics set up
game_over = False
clock = pygame.time.Clock()

# Cell features
total_cell_number = 100
cell_length = screen_height // total_cell_number
cell_margin = 1
color = {True: (128, 128, 128), False: (0, 0, 0)}
grid = initialize_grid((total_cell_number, total_cell_number))
grid[50][50] = True
running = False

# Game main
while not game_over:
    screen.fill(color[True])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = int(pos[0] / (cell_length + cell_margin))
            row = int(pos[1] / (cell_length + cell_margin))
            grid[row][col] = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                running = not running
            elif event.key == pygame.K_ESCAPE:
                grid = initialize_grid((total_cell_number, total_cell_number))

    for row in range(total_cell_number):
        for col in range(total_cell_number):
            current_cell = grid[row][col]
            pygame.draw.rect(screen, color[current_cell],
                             [cell_margin + (cell_margin + cell_length) * col,
                              cell_margin + (cell_margin + cell_length) * row,
                              cell_length, cell_length])
    if running:
        grid = run_life(grid)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
