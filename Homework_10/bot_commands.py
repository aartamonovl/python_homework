from telegram import Update
from telegram.ext import CallbackContext
from log_commands import *
from datetime import datetime


def hi_command(name):
    return (f'Hi {name}!')


def calcrun(usrerexp):
    return eval(usrerexp)


def days2NY():
    now = datetime.today()
    NY = datetime(now.year + 1, 1, 1)
    d = NY-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    return ('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))