host = "157.230.209.171"
username = "jemison_1754"
user = username
password = "hzNzYToJR6PjEUBbSLLL6wGpLn5yMHqk"


def get_db_url(database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url