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
    CREATE TABLE IF NOT EXISTS phonebook1 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        surname VARCHAR(255),
        phone VARCHAR(255)
    );
""")
conn.commit()

cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], surnames TEXT[], phones TEXT[], OUT invalid_records TEXT)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT := 1;
        total INT := array_length(names, 1);
        bad_entries TEXT := '';
    BEGIN
        WHILE i <= total LOOP
            IF phones[i] ~ '^\d{11,12}$' THEN
                INSERT INTO phonebook1(name, surname, phone) VALUES (names[i], surnames[i], phones[i]);
            ELSE
                bad_entries := bad_entries || '(' || names[i] || ', ' || surnames[i] || ', ' || phones[i] || '), ';
            END IF;
            i := i + 1;
        END LOOP;
        invalid_records := TRIM(TRAILING ', ' FROM bad_entries);
    END;
    $$;
""")
conn.commit()

def insert_many_users():
    names = []
    surnames = []
    phones = []
    n = int(input("How many users to insert: "))
    for _ in range(n):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone = input("Enter phone: ")
        names.append(name)
        surnames.append(surname)
        phones.append(phone)
    cur.callproc("insert_many_users", (names, surnames, phones))
    result = cur.fetchone()
    if result and result[0]:
        print("Invalid records:")
        print(result[0])
    else:
        print("All records inserted successfully.")
    conn.commit()

def insert_from_csv(path):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook1 (name, surname, phone) VALUES (%s, %s ,%s)",
                        (row['name'], row['surname'], row['phone']))
    conn.commit()
    print("Data loaded from CSV.")

def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook1 (name, surname, phone) VALUES (%s, %s, %s)",
                (name, surname, phone))
    conn.commit()
    print("User added.")

def update_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE phonebook1 SET phone = %s WHERE name = %s AND surname = %s",
                (new_phone, name, surname))
    conn.commit()
    print("Phone number updated.")

def insert_or_update_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.execute("SELECT * FROM phonebook1 WHERE name = %s OR surname = %s", (name, surname))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE phonebook1 SET phone = %s WHERE name = %s AND surname = %s",(phone, name, surname))
        conn.commit()
        print("Phone number updated.")
    else:
        cur.execute("INSERT INTO phonebook1 (name, surname, phone) VALUES (%s,%s, %s)",(name, surname, phone))
        conn.commit()
        print("User inserted.")

def pagination_query():
    try:
        limit = int(input("Enter limit (how many records to display): "))
        offset = int(input("Enter offset (how many records to skip): "))
        cur.execute("SELECT * FROM phonebook1 ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found for the given limit and offset.")
    except ValueError:
        print("Limit and offset must be integers.")

def search_by_pattern(pattern):
    print("1 - Search by name pattern")
    print("2 - Search by surname pattern")
    print("3 - Search by phone pattern")
    print("4 - Search by common pattern")

    pattern1 = f"%{pattern}%"
    choice = input("Choose what to look for using a pattern: ")
    if choice == "1":
        print("\nSearching in names:")
        cur.execute("SELECT * FROM phonebook1 WHERE name ILIKE %s", (pattern1,))
        name_results = cur.fetchall()
        if name_results:
            for row in name_results:
                print(row)
        else:
            print("No matches found in names.")
    elif choice == "2":
        print("\nSearching in surnames:")
        cur.execute("SELECT * FROM phonebook1 WHERE surname ILIKE %s", (pattern1,))
        surname_results = cur.fetchall()
        if surname_results:
            for row in surname_results:
                print(row)
        else:
            print("No matches found in surnames.")
    elif choice == "3":
        print("\nSearching in phones:")
        cur.execute("SELECT * FROM phonebook1 WHERE phone ILIKE %s", (pattern1,))
        name_results = cur.fetchall()
        if name_results:
            for row in name_results:
                print(row)
        else:
            print("No matches found in phones.")
    elif choice == "4":
        print("\nSearching by pattern:")
        cur.execute("SELECT * FROM phonebook1 WHERE name ILIKE %s or surname ILIKE %s or phone ILIKE %s", (pattern1, pattern1, pattern1))
        name_results = cur.fetchall()
        if name_results:
            for row in name_results:
                print(row)
        else:
            print("No matches found.")

def query_users():
    print("1 - Show all records")
    print("2 - Search by name")
    print("3 - Search by surname")
    print("4 - Search by phone")
    print("5 - Sort by phone")
    print("6 - Sort by name")
    print("7 - Sort by surname")
    choice = input("Choose an option: ")

    if choice == "1":
        cur.execute("SELECT * FROM phonebook1")
    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook1 WHERE name = %s", (name,))
    elif choice == "3":
        surname = input("Enter surname: ")
        cur.execute("SELECT * FROM phonebook1 WHERE surname = %s", (surname,))
    elif choice == "4":
        phone = input("Enter phone number: ")
        cur.execute("SELECT * FROM phonebook1 WHERE phone = %s", (phone,))
    elif choice in ["5", "6", "7"]:
        order = input("Sort order (asc/desc): ").lower()
        if order not in ['asc', 'desc']:
            print("Invalid sort order. Use 'asc' or 'desc'.")
            return
        column = "phone" if choice == "5" else "name" if choice == "6" else "surname"
        cur.execute(f"SELECT * FROM phonebook1 ORDER BY {column} {order}")
    else:
        print("Invalid choice.")
        return

    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No results found.")

def delete_user():
    print("1 - Delete by name")
    print("2 - Delete by surname")
    print("3 - Delete by phone number")
    print("4 - Delete by fullname")
    print("5 - Delete all records")
    choice = input("Choose delete method: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook1 WHERE name = %s", (name,))
    elif choice == "2":
        surname = input("Enter surname: ")
        cur.execute("DELETE FROM phonebook1 WHERE name = %s", (surname,))
    elif choice == "3":
        phone = input("Enter phone number: ")
        cur.execute("DELETE FROM phonebook1 WHERE phone = %s", (phone,))
    elif choice == "4":
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        cur.execute("DELETE FROM phonebook1 WHERE name = %s and surname = %s", (name, surname))
    elif choice == "5":
        cur.execute("TRUNCATE TABLE phonebook1 RESTART IDENTITY;")
    else:
        print("Invalid choice.")
        return

    conn.commit()
    print("Record deleted.")

def main():
    while True:
        print("\nPhonebook Menu")
        print("1. Load from CSV")
        print("2. Add user manually")
        print("3. Update user phone")
        print("4. Search / Sort users")
        print("5. Delete user")
        print("6. Search by pattern")
        print("7. Insert / Update user")
        print("8. Show records with pagination")
        print("9. Insert many users manually")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_csv("phonebook2.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            pattern = input("Enter a part of name, surname, or phone number: ")
            search_by_pattern(pattern)
        elif choice == "7":
            insert_or_update_user()
        elif choice == "8":
            pagination_query()
        elif choice == "9":
            insert_many_users()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
