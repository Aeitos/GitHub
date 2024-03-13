import datetime

MAX_LEVEL = 200
XP_PER_LEVEL = 80000

END_SEASON_TIME = datetime.datetime.combine(datetime.date(2024, 5, 24), datetime.time(7, 00))
START_SEASON_TIME = datetime.datetime.combine(datetime.date(2024, 3, 8), datetime.time(7, 00))
CURRENT_DAY = datetime.date.today()


def get_left_xp(current_level, current_xp):
    """
    Return the amount of xp left to get to the max level.

    :param int current_level: Current level in game.
    :param int current_xp: Current xp on the current level

    :return: Xp left to the max level
    :rtype: int
    """
    return ((MAX_LEVEL - current_level) * XP_PER_LEVEL) - current_xp


def get_time_left():
    """
    Return the number of day left before end of season.

    :return: Day left until end of season.
    :rtype: str
    """
    delta = END_SEASON_TIME - datetime.datetime.now()
    return delta.__str__()[:-10]


def get_day_left():
    """
    Convert the time left into day left.
    :return: Days left.
    :rtype: float
    """
    delta = END_SEASON_TIME - datetime.datetime.now()

    return delta.days + (delta.seconds / 86400.0)


def get_xp_per_day_left(total_xp_left):
    """
    Return the xp per day to make to get to the max level befor end of season.

    :param int total_xp_left: Left xp to max level.

    :return: Xp per day.
    :rtype: int
    """
    return round(total_xp_left / get_day_left())


def get_xp_made_per_day(current_level, current_xp):
    """
    Return the xp made by day since start of the season.

    :return: Xp made per day
    :rtype: int
    """
    delta = datetime.datetime.now() - START_SEASON_TIME
    return round((current_level * XP_PER_LEVEL + current_xp) / (delta.days + (delta.seconds / 86400.0)))
