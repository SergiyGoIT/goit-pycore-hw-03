from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)
        
        delta = (birthday - today).days
        if 0 <= delta <= 7:
            if birthday.weekday() == 5:  # Субота
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:  # Неділя
                birthday += timedelta(days=1)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

today = datetime.today().date()
users = [
    {"name": "User 1", "birthday": (today - timedelta(days=1)).strftime("%Y.%m.%d")},  # День народження був вчора
    {"name": "User 2", "birthday": today.strftime("%Y.%m.%d")},                        # День народження сьогодні
    {"name": "User 3", "birthday": (today + timedelta(days=7)).strftime("%Y.%m.%d")},  # День народження через 7 днів
    {"name": "User 4", "birthday": (today + timedelta(days=8)).strftime("%Y.%m.%d")},  # День народження через 8 днів
    {"name": "User 5", "birthday": (today + timedelta(days=7)).strftime("%Y.%m.%d")},  # День народження через 7 днів (перевірка на понеділок)
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
