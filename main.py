import pygame
from algorithms import *
from visualizer import Visualizer
from button import *

#TODO: fix white space when array size is less than 25
#TODO: add more sorting algorithms?
#TODO: speed up slower algorithms   

#Start pygame stuff
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()
running = True

#States
MENU = "menu"
SORTING = "sorting"
DONE = "done"

#Visualizer/Slider object
visualizer = None
size_slider = Slider(
    x=100,
    y=520,
    width=300,
    min_val=10,
    max_val=100,
    start_val=100
)

#Font
font = pygame.font.SysFont(None, 32)

#Buttons
buttons = [
    Button((100, 150, 200, 50), "Bubble Sort", bubble_sort),
    Button((100, 220, 200, 50), "Selection Sort", selection_sort),
    Button((100, 290, 200, 50), "Merge Sort", merge_sort),
    Button((100, 360, 200, 50), "Quick Sort", quick_sort),
    Button((100, 430, 200, 50), "Insertion Sort", insertion_sort)
]

back_button = Button((500, 150, 200, 50), "Back to Menu", None)

#Main loop logic
state = MENU
animation_done = False

while running:
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            size_slider.handle_event(event) 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == MENU: 
                for button in buttons:
                    if button.is_clicked(event.pos):
                        state = SORTING
                        animation_done = False
                        visualizer = Visualizer(size_slider.value)
                        visualizer.run_algorithm(button.algorithm, screen)
                        state = DONE

            elif state == DONE:
                if back_button.is_clicked(event.pos):
                    state = MENU             

    if state == MENU:
        for button in buttons:
            button.draw(screen, font)

        size_slider.draw(screen)
        label = font.render(f"Array Size: {size_slider.value}", True, (0,0,0))
        screen.blit(label, (100, 490))               

    elif state == DONE:
        if not animation_done:
            visualizer.animate_sorted_array(screen)
            animation_done = True
        else:
            visualizer.draw_sorted_array(screen)
        back_button.draw(screen, font)
     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
