import time

class Stopwatch():

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.time = time.time()
        self.paused_at = self.time
        self.paused = True
        
    def get_time(self):
        if not self.paused:
            return time.time() - self.time
        else:
            return self.paused_at - self.time
        
    def start_or_pause(self):
        if self.paused:
            self.time += self.paused_at - time.time()
            self.paused_at = None
        else:
            self.paused_at = time.time()
            self.paused = True
