from otree.api import Currency as c, currency_range, expect
from . import app
from otree.api import Bot
from .app import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield app.Contribute, dict(contribution=c(1))
        yield app.Results
