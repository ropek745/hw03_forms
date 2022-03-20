import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    current_time = datetime.datetime.now()
    year = int(current_time.strftime('%Y'))
    return {
        'year': year
    }
