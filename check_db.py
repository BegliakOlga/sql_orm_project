import os

import psycopg
from dotenv import load_dotenv
from psycopg import connect


def main():
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        print('Укажите адрес базы данных')

    with psycopg.connect(db_url, connect_timeout=10) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT current_database(), current_user')
            database_name, database_user = cursor.fetchone()

    print(f'Успешное подключение к БД {database_name} (пользователь: {database_user})')
if __name__ == '__main__':
    main()