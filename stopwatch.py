import time

class Stopwatch():

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.time = time.time()
        self.paused = False
        
    def get_time(self):
        if not self.paused:
            return time.time() - self.time
        else:
            return self.paused_at - self.time
        
    def pause_timer(self):
        self.paused_at = time.time()
        self.paused = True
        
    def resume_timer(self):
        if self.paused:
            self.time += self.paused_at - time.time()
            self.paused_at = None
    