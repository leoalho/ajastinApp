#from time import time
class TimerService:

    def __init__(self, connection) -> None:
        self._current_time = 0
        self._session_time = 0
        self._connection = connection
        self._timer = False

    def tick(self):
        self._current_time += 1
        return self.time_to_string(self._current_time)

    def reset(self):
        self._session_time += self._current_time
        self._current_time = 0

    def toggle_timer(self):
        if not self._timer:
            self._timer = True
        else:
            self._timer = False
            self.reset()

    def get_timer(self):
        return self._timer

    def get_current_time(self):
        return self.time_to_string(self._current_time)

    def get_session_time(self):
        return self.time_to_string(self._session_time)

    def time_to_string(self, time):
        remaining = time
        result = ""
        if remaining>3600:
            hours = remaining//3600
            remaining -= hours*3600
            result += f"{hours} h "
        if remaining>60:
            minutes = remaining//60
            remaining -= minutes*60
            result += f"{minutes} m "
        result += f"{remaining} s"
        return result
