import pygame

class Button:
    def __init__(self, rect, text, algorithm):
            self.rect = pygame.Rect(rect)
            self.text = text
            self.algorithm=algorithm
        
    def draw(self, screen, font):
          pygame.draw.rect(screen, (200,200,200), self.rect)
          pygame.draw.rect(screen, (0,0,0), self.rect, 2)
          label = font.render(self.text, True, (0,0,0))
          screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, pos):
          return self.rect.collidepoint(pos)
    
class Slider:
      def __init__(self, x, y, width, min_val, max_val, start_val):
            self.rect = pygame.Rect(x, y, width, 6)
            self.min = min_val
            self.max = max_val
            self.value = start_val
            
            self.knob_radius = 10
            self.dragging = False
            
      def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._knob_rect().collidepoint(event.pos):
                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x = event.pos[0]
            mouse_x = max(self.rect.left, min(mouse_x, self.rect.right))
            t = (mouse_x - self.rect.left) / self.rect.width
            self.value = int(self.min + t * (self.max - self.min))

      def draw(self, screen):
        # Line
        pygame.draw.rect(screen, "BLACK", self.rect)

        # Knob
        knob_x = self.rect.left + (self.value - self.min) / (self.max - self.min) * self.rect.width
        pygame.draw.circle(screen, "DARKGRAY", (int(knob_x), self.rect.centery), self.knob_radius)

      def _knob_rect(self):
        knob_x = self.rect.left + (self.value - self.min) / (self.max - self.min) * self.rect.width
        return pygame.Rect(
            knob_x - self.knob_radius,
            self.rect.centery - self.knob_radius,
            self.knob_radius * 2,
            self.knob_radius * 2
        )