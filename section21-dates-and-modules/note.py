from time import gmtime, time, strftime, strptime, sleep, perf_counter
from calendar import timegm
from datetime import date, time as datetime_time, datetime, timedelta, timezone

format = '%Y-%m-%d %H %M'
target = gmtime(time())
time_string = strftime(format, target)
time_convert = strptime(time_string, format)
time_struct = timegm(time_convert)
print(f'target: {target}')
print(f'time_string: {time_string}')
print(f'time_convert: {time_convert}')
print(f'time_struct: {time_struct}')


# start = perf_counter()
# sleep(2)
# end = perf_counter()
# elapsed = end - start
# print(f'elapsed: {elapsed}')

now_epoch = time()
now_struct = gmtime(now_epoch)
now_re_epoch = timegm(now_struct)
# print(f'now_epoch: {now_epoch}')
# print(f'now_struct: {now_struct}')
# print(f'now_re_epoch: {now_re_epoch}')

date_1 = date(year=2024, month=1, day=1)
date_1_epoch = timegm(time_convert)
date_1_struct = gmtime(date_1_epoch)

# print(f'date_1: {date_1}')
# print(f'date_1_epoch: {date_1_epoch}')
# print(f'date_1_struct: {date_1_struct}')

# print(date.today())
# print(datetime.utcnow())
# print(datetime_time(12, 1))


date_2 = date(2023, 12, 3)

# print(f'date_2: {date_2}')
# print(f'date_2.isoformat: {date_2.isoformat()}')

# ---------------------------------------------------------


def get_first_last_of_month(dt, month):
    start = date(dt.year, month, 1)

    if (start.month == 12):
        year_of_end = start.year + 1
        month_of_end = 1
    else:
        year_of_end = start.year
        month_of_end = start.month + 1

    end = date(year_of_end, month_of_end, 1) + timedelta(days=-1)

    return start, end


start_month, end_month = get_first_last_of_month(date.today(), 12)

# print(f'start: {start_month}')
# print(f'end: {end_month}')

# ---------------------------------------------------------

tz_FROM = timezone(timedelta(hours=-7), 'FROM')
tz_TO = timezone(timedelta(hours=5), 'TO')
time_str = '2022-01-15T12:00:30'

target = datetime.fromisoformat(time_str)

tz_added_target = datetime(
    target.year,
    target.month,
    target.day,
    target.hour,
    target.minute,
    target.second,
    target.microsecond,
    tz_FROM
)

tz_replaced_target = tz_added_target.replace(tzinfo=tz_TO)


# print(f'target: {target}')
# print(f'tz_added_target: {tz_added_target.astimezone(tz_FROM)}')
# print(f'tz_replaced_target: {tz_added_target.astimezone(tz_TO)}')


def convert_to_utc(dt_str):
    utc_time = datetime.fromisoformat(dt_str).astimezone(
        timezone.utc).replace(tzinfo=None)
    return utc_time


time = convert_to_utc('2022-01-15T12:00:30+07:00')

# print(f'time: {time}')
# print(datetime.fromisoformat(
#     '2022-01-15T12:00:30').replace(tzinfo=timezone.utc).astimezone(tz_TO))
