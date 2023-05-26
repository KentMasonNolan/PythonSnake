import pygame

def main():
    pygame.init()

    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("hello")

    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        win.fill((30, 30, 30))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()