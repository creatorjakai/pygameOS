#Importeren van Libraries
import pygame
import time

#Initializeren van onderdelen
pygame.init()

#Laad belangerijke afbeeldingen
image_os = pygame.image.load("Assets/OS/osicon.png")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

#Inializeren van belangerijke variabelen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygameOS v26.0")
pygame.display.set_icon(image_os)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 15)
running = True

def bootmessage():
        global loadingtext
        screen.fill((0,0,0))
        version_pygame = font.render((pygame.version.ver), True ,(255, 255, 255))
        loading_text = font.render(str(loadingtext), True, (255, 255, 255))
        screen.blit(loading_text, (5,(SCREEN_HEIGHT - 20)))
        screen.blit(version_pygame, (5, 5))
        pygame.display.flip()

def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.flip()
    
        clock.tick(60)

#Laden van onderdelen in het algemeen
#Laden van afbeeldingen
loadingtext = str("Loading:")
bootmessage()
#image_terminal = pygame.image.load("Assets/OS/terminalicon.png")
time.sleep(1)

#Als het script voorbij is sluit dan pygame af
pygame.display.quit()
pygame.quit()
