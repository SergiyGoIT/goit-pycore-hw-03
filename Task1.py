from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()
    delta = today - input_date
    return delta.days

print(get_days_from_today("2025-3-15"))