import os
import datetime


def write():
    dt_now = datetime.datetime.now()
    os.environ["PAST_DATETIME"] = dt_now.strftime("%Y-%m-%d %H:%M:%S")


def load():
    PAST_DATETIME = datetime.datetime(2018, 12, 25, 0, 0, 0).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    datetime_str = os.environ.get("PAST_DATETIME", PAST_DATETIME)
    datetime_dt = datetime.datetime.strptime(
        datetime_str, "%Y-%m-%d %H:%M:%S"
    )  # noqa #501
    return datetime_dt
