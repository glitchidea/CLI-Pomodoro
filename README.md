# CLI-Pomodoro

**CLI-Pomodoro** is a console-based productivity tool designed to help users manage tasks and enhance focus. With a user-friendly interface, this application allows users to add, complete, and delete tasks, track work sessions, and take scheduled breaks using the Pomodoro technique.

## Features

- **Task Management**: Easily add, complete, and delete tasks.
- **Pomodoro Technique**: Customize work durations and breaks to improve focus.
- **Customizable Settings**: Adjust work time, break time, and notification sounds.
- **Database Integration**: Permanently store tasks using SQLite.

## Getting Started

### Requirements

- Python 3.x
- `sqlite3` (comes pre-installed with Python)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/glitchidea/CLI-Pomodoro.git
   cd CLI-Pomodoro
   ```

2. Run the application:
   ```bash
   python CLI-Pomodoro.py
   ```

### Usage

1. **Start the Application**: Run the script to open the CLI interface.
2. **Main Menu Options**:
   - **1. Add New Task**: Enter the name of the task to add it to the list.
   - **2. Complete Task**: Enter the number of the completed task.
   - **3. Delete Task**: Enter the number of the task you want to delete.
   - **4. Start Pomodoro**: Begin a work session based on your set duration.
   - **5. Settings**: Adjust Pomodoro duration, break time, and notification sound.
   - **6. Exit**: Close the application.

### Database Management

The application uses SQLite to store tasks. The `Timer_Lesson.db` database file is created upon the first run.

## Code Overview

- **Database Functions**: Functions for adding, updating, deleting, and retrieving tasks from the SQLite database.
- **Main Functionality**: The main loop that processes user input and manages the Pomodoro timer.
