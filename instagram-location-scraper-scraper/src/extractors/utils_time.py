thonfrom datetime import datetime

def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')

def get_current_date():
    return datetime.now()