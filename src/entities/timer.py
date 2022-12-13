from datetime import datetime
from utils import helpers

class Timer:
    """Luokka kuvaamaan ajastinta
    """

    def __init__(self) -> None:
        """Luokan konstruktori.
        Current_time: tämänhetkinen aika,
        session_time: koko istunnon aika,
        timer_on: onko ajastin päällä?,
        self.start: aikaleima, jolloin ajastin laitettiin päälle,
        self.stop: aikaleima, jolloin ajastin laitettiin pois päältä
        """

        self.current_time = 0
        self.session_time = 0
        self.timer_on = False
        self.start = None
        self.stop = None

    def tick(self):
        """Lisää nykyistä aikaa yhdellä

        Returns:
            Palauttaa tämänhetkisen ajan muotoiltuna
        """
        self.current_time += 1
        return helpers.time_to_string(self.current_time)

    def reset(self):
        """Pistää ajastimen pois päältä, nollaa nykyisen ajan,
        lisää nykyisen ajan session aikaan.

        Returns:
            Palauttaa nykyajan kokonaislukuna ennen ajastimen ollausta
        """
        self.timer_on = False
        new_time = self.current_time
        self.session_time += self.current_time
        self.current_time = 0
        self.start = None
        self.stop = None

        return new_time

    def toggle_timer(self):
        """Laittaa ajastimen päälle mikäli ajastin on pois päältä sekä sama toisin päin.
        """
        if not self.timer_on:
            self.timer_on = True
            self.start = datetime.now()
        else:
            self.timer_on = False
            self.stop = datetime.now()

    def get_start_stop(self):
        """Returns:
            Palauttaa tuplena ajanoton alku- ja loppuhetken datetime-oliona
        """
        return (self.start,self.stop)

    def get_current_time(self):
        """Palauttaa merkkijonona tämänhetkisen ajan
        """

        return helpers.time_to_string(self.current_time)

    def get_session_time(self):
        """Returns:
            Palauttaa merkkijonona nykysessin ajan
        """

        return helpers.time_to_string(self.session_time)
