import helpers

class Timer:
    def __init__(self) -> None:
        self._current_time = 0
        self._session_time = 0
        self._timer_on = False

    def tick(self):
        self._current_time += 1
        return helpers.time_to_string(self._current_time)

    def reset(self):
        new_time = self._current_time
        self._session_time += self._current_time
        self._current_time = 0
        return new_time

    def toggle_timer(self):
        if not self._timer_on:
            self._timer_on = True
        else:
            self._timer_on = False

    def get_current_time(self):
        return helpers.time_to_string(self._current_time)

    def get_session_time(self):
        return helpers.time_to_string(self._session_time)

    def get_timer(self):
        return self._timer_on
