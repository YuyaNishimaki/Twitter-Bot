import datetime
import pathlib


def write():
    path = pathlib.Path("exexcution_datetime.txt")
    dt_now = datetime.datetime.now()
    path.write_text(dt_now.strftime("%Y-%m-%d %H:%M:%S"))


def load():
    path = pathlib.Path("exexcution_datetime.txt")
    try:
        datetime_str = path.read_text()
        datetime_dt = datetime.datetime.strptime(
            datetime_str, "%Y-%m-%d %H:%M:%S"
        )  # noqa #501
        return datetime_dt
    except FileNotFoundError:
        return datetime.datetime(2018, 12, 18, 0, 0, 0)


def delete():
    path = pathlib.Path("exexcution_datetime.txt")
    path.unlink()
