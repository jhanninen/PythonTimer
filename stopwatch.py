""" This module contains the stopwatch content """

import time


class Stopwatch():
    """ Stopwatch class """

    def __init__(self):
        self.time = time.time()
        self.paused_at = self.time
        self.paused = True

    def reset(self):
        """ Reset stopwatch value to zero """
        self.time = time.time()
        self.paused_at = self.time
        self.paused = True

    def get_time(self):
        """ Return stopwatch value as seconds """
        if not self.paused:
            return time.time() - self.time  # Value is current time - start time

        return self.paused_at - self.time  # Value is pausing time - start time

    def start_or_pause(self):
        """ Start or pause the stopwatch """
        if self.paused:  # Start the stopwatch again
            # Add the time paused to the start time
            self.time = self.time + (time.time() - self.paused_at)
            self.paused = False
        else:
            self.paused_at = time.time()  # Save the pausing time
            self.paused = True
