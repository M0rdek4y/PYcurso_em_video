# resolução 1

import pygame
pygame.init()
pygame.mixer.music.load('wakawaka.mp3')
pygame.mixer.music.get_volume()
pygame.mixer.music.play()
pygame.event.wait()
input()
