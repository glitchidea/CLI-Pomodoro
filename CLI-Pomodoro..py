import time
import os
import sqlite3

conn = sqlite3.connect('Timer_Lesson.db')
cursor = conn.cursor()

# Create the database table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        done BOOLEAN NOT NULL
    )
''')
conn.commit()

def insert_task_to_db(name, done=False):
    cursor.execute('INSERT INTO tasks (name, done) VALUES (?, ?)', (name, done))
    conn.commit()

def get_all_tasks_from_db():
    cursor.execute('SELECT * FROM tasks')
    return cursor.fetchall()

def update_task_status_in_db(task_id, done):
    cursor.execute('UPDATE tasks SET done=? WHERE id=?', (done, task_id))
    conn.commit()

def delete_task_from_db(task_id):
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()

def main():
    minutes = 25
    sets = 4
    break_time = 5
    sound_file = r'C:\Windows\Media\Alarm09.wav'

    tasks = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Pomodoro Duration: {minutes} minutes\nPomodoro Set Count: {sets}\n")
        print("To-Do List:\n")
        for index, task in enumerate(tasks):
            if task["done"]:
                print(f"{index + 1}. [X] {task['name']}")
            else:
                print(f"{index + 1}. [ ] {task['name']}")
        print("\n")

        choice = input("Select an action:\n1. Add new task\n2. Task completed\n3. Delete task\n4. Start Pomodoro\n5. Settings\n6. Exit\n:")
        if choice == "1":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pomodoro is ongoing, you can add a new task. Press 'q' or 'Q' to finish adding tasks.")
                task_name = input("Enter the name of the new task: ")
                if task_name.lower() == 'q':
                    break
                elif task_name.lower() == 'c':
                    continue
                else:
                    tasks.append({"name": task_name, "done": False})
                    insert_task_to_db(task_name, False)
                    print("Task added successfully.")

        elif choice == "2":
            try:
                task_index = int(input("Enter the number of the completed task: "))
                update_task_status_in_db(task_index, True)

            except:
                print("Invalid input.")
                time.sleep(2)

        elif choice == "3":
            try:
                task_index = int(input("Enter the number of the task to delete: ")) - 1
                delete_task_from_db(task_index)
            except:
                print("Invalid input.")
                time.sleep(2)

        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pomodoro started! To-Do list:")
            for index, task in enumerate(tasks):
                if task["done"]:
                    print(f"{index + 1}. [X] {task['name']} ")
                else:
                    print(f"{index + 1}. [ ] {task['name']} ")

            for i in range(sets):
                for j in range(minutes):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Pomodoro started! Working time...\n")
                    print(f"Set: {i + 1}/{sets}")
                    print(f"Minute: {j + 1}/{minutes}")
                    print("\nTo-Do List:")
                    for index, task in enumerate(tasks):
                        if task["done"]:
                            print(f"{index + 1}. [X] {task['name']} ")
                        else:
                            print(f"{index + 1}. [ ] {task['name']} ")
                    time.sleep(60)
                start_file = "art.txt"
                with open(start_file) as f:
                    art = f.read()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{art}\nPomodoro is over!\n")

                sound_file = "alarm.wav"
                os.system(f'start "" "{sound_file}"')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Break time...\n")
                time.sleep(break_time * 60)

        elif choice == "5":
            try:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Settings\n")
                    print(f"1. Pomodoro Duration: {minutes} minutes")
                    print(f"2. Pomodoro Set Count: {sets}")
                    print(f"3. Break Duration: {break_time} minutes")
                    print(f"4. Sound File: {sound_file}")
                    print("5. Back")
                    sub_choice = input("Select an action: ")
                    if sub_choice == "1":
                        minutes = int(input("Enter the new Pomodoro duration in minutes: "))
                    elif sub_choice == "2":
                        sets = int(input("Enter the new Pomodoro set count: "))
                    elif sub_choice == "3":
                        break_time = int(input("Enter the new break duration in minutes: "))
                    elif sub_choice == "4":
                        sound_file = input("Enter the path of the new sound file: ")
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid selection, please try again.")
                        time.sleep(2)
            except:
                print("Invalid input.")
                time.sleep(2)

        elif choice == "6":
            subprocess.run(["python", "Lain.py"])  # IF 6 IS PRESSED, IT WILL RETURN TO THE MAIN MENU
        else:
            print("Invalid selection, please try again.")
            time.sleep(2)

if __name__ == '__main__':
    main()
