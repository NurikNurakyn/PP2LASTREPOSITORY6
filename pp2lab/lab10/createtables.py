import psycopg2

# Подключение к базе
conn = psycopg2.connect(
    host="localhost",         # Или '127.0.0.1'
    database="PhoneBook",     # Название базы данных
    user="postgres",          # Имя пользователя
    password="Fdrj19525"  # Твой пароль
)

cur = conn.cursor()

# SQL-команды для создания таблиц
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL
);
"""

create_user_scores_table = """
CREATE TABLE IF NOT EXISTS user_scores (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    level INTEGER DEFAULT 1,
    score INTEGER DEFAULT 0,
    PRIMARY KEY (user_id)
);
"""

# Выполнение
cur.execute(create_users_table)
cur.execute(create_user_scores_table)

# Сохранение и завершение
conn.commit()
cur.close()
conn.close()

print("✅ Таблицы успешно созданы.")
