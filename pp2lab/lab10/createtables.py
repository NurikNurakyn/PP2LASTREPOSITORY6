import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="postgres",
    password="Fdrj19525"
)

cur = conn.cursor()

create_user_scores_table = """
CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    username VARCHAR (255),
    level INTEGER DEFAULT 1,
    score INTEGER DEFAULT 0
);
"""
cur.execute(create_user_scores_table)

conn.commit()
cur.close()
conn.close()
#
