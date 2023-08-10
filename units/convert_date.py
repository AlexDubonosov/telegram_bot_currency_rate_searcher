import datetime
import calendar


# Конвертирование дат из формата г/м/д в секунды с 'начала эпохи'
# Выбор интервала для графика в зависимости от промежутка
def convert_date(date_period: str) -> tuple:
    date_period = date_period.split()

    y, m, d = date_period[0].split('-')
    st = datetime.datetime(int(y), int(m), int(d))
    start_time = str(calendar.timegm(st.timetuple()))

    y, m, d = date_period[1].split('-')
    et = datetime.datetime(int(y), int(m), int(d))
    end_time = str(calendar.timegm(et.timetuple()))

    if int(start_time) - int(end_time) > 604_800:
        interval = "1d"
    else:
        interval = '60m'

    return interval, start_time, end_time
