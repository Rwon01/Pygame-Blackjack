from pygame.time import get_ticks

class Timer():
    def __init__(self, duration, func):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.func = func

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                if self.func : self.func()
                self.deactivate()

