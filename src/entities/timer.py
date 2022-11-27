from datetime import datetime
import helpers

class Timer:
    def __init__(self) -> None:
        self.current_time = 0
        self.session_time = 0
        self.timer_on = False
        self.start = None
        self.stop = None

    def tick(self):
        self.current_time += 1
        return helpers.time_to_string(self.current_time)

    def reset(self):
        new_time = self.current_time
        self.session_time += self.current_time
        self.current_time = 0
        self.start = None
        self.stop = None

        return new_time

    def toggle_timer(self):
        if not self.timer_on:
            self.timer_on = True
            self.start = datetime.now()
        else:
            self.timer_on = False
            self.stop = datetime.now()

    def get_start_stop(self):
        return (self.start,self.stop)

    def get_current_time(self):
        return helpers.time_to_string(self.current_time)

    def get_session_time(self):
        return helpers.time_to_string(self.session_time)
