
def twelve_date_from_list(dates):
    """
    Функция для сокращения кол-ва значений в списке до +- 12 штук.

    :param dates:
    :return:
    """
    shift = len(dates) // 12
    if len(dates) > 12:
        new_dates = [dates[count] for count in range(0, len(dates), shift)]
        return new_dates
    else:
        return dates
