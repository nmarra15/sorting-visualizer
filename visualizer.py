from algorithms import selection_sort, insertion_sort, merge_sort, bubble_sort, quick_sort
import pygame
import random

class Visualizer:
    #Screen settings
    WIDTH, HEIGHT = 800, 600

    # Constructor
    def __init__(self, array_length):
        self.width = Visualizer.WIDTH
        self.height = Visualizer.HEIGHT
        self.array = []
        self.array_len = array_length 
        self.generate_new_array()
        
    # Creates random array
    def generate_new_array(self):
        self.array = [random.randint(10, self.height-300) for _ in range(self.array_len)] 
        # -300 leaves room for buttons

    # Multitasks with sorting algorithm to properly highlight array
    def run_algorithm(self, sorting_algorithm, screen):
        for array_state, highlight_index in sorting_algorithm(self.array):
            #Check user has quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                
            self.draw_array(screen, highlight_index)
            pygame.display.flip()
            pygame.event.pump()
            #Time delay
            pygame.time.delay(30)
        #self.draw_sorted_array(screen)
        pygame.display.flip()
        pygame.event.pump()
    
    #Draws current array
    def draw_array(self, screen, highlight_index=None):
        screen.fill("white")
        bar_width = self.width // len(self.array)
        for i, val in enumerate(self.array):
            x = i * bar_width
            y = self.height - val 
            color = "RED" if highlight_index == i else "BLUE"
            #Filled bar
            pygame.draw.rect(screen, color, (x, y, bar_width, val))
            #Border
            pygame.draw.rect(screen, "BLACK", (x, y, bar_width, val), width=1)

    #Draws fully sorted array
    def animate_sorted_array(self, screen):
        screen.fill("white")
        bar_width = self.width // len(self.array)
        for i, val in enumerate(self.array):
            x = i * bar_width
            y = self.height - val
            pygame.draw.rect(screen, "GREEN", (x, y, bar_width, val))
            pygame.draw.rect(screen, "BLACK", (x, y, bar_width, val), 1)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(30)

    def draw_sorted_array(self, screen):
        screen.fill("white")
        bar_width = self.width // len(self.array)
        for i, val in enumerate(self.array):
            x = i * bar_width
            y = self.height - val
            pygame.draw.rect(screen, "GREEN", (x, y, bar_width, val))
            pygame.draw.rect(screen, "BLACK", (x, y, bar_width, val), 1)

