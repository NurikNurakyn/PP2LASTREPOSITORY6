import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    dbname="PhoneBook",
    user="postgres",
    password="Fdrj19525",
    port="5432"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(20),
        phone VARCHAR(15)
    );
""")
conn.commit()

def insert_from_csv(path):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row['username'], row['phone']))
    conn.commit()
    print("📥 Data from CSV has been inserted.")


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    print("User has been added.")


def update_user():
    username = input("Enter the username to update: ")
    new_phone = input("Enter the new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
    conn.commit()
    print("🔄 Phone number has been updated.")

def query_users():
    print("1 - All records")
    print("2 - By username")
    print("3 - By phone")
    print("4 - Sort by phone")
    print("5 - Sort by username")
    choice = input("Choose an option: ")

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
    elif choice == "2":
        name = input("Enter username: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
    elif choice == "3":
        phone = input("Enter phone number: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    elif choice == "4":
        sorts = input("Sort by phone(asc\desc): ")
        order = "asc"
        order = "sorts"
        cur.execute("SELECT * FROM phonebook ORDER BY phone {order}")
    elif choice == "5":
        sorts = input("Sort by username(asc\desc): ")
        order = "asc"
        order = "sorts"
        cur.execute("SELECT * FROM phonebook ORDER BY username {order}")
    for row in cur.fetchall():
        print(row)


def delete_user():
    username_or_phone = input("Enter username or phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (username_or_phone, username_or_phone))
    conn.commit()
    print("Record has been deleted.")


def main():
    while True:
        print("\nMenu:")
        print("1. Load from CSV")
        print("2. Add manually")
        print("3. Update user")
        print("4. Search")
        print("5. Delete")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("phonebook.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("Good bye!")
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
