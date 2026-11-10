# Student Gradebook

A command-line gradebook for managing students, recording grades by subject,
and reporting class performance. It runs on Python 3.10 or later with the
standard library.

## Run the program

From the project directory on Windows:

~~~powershell
py main.py
~~~

On macOS or Linux, use python3 main.py.

## Menu options

| Option | What it does |
| --- | --- |
| 1. Add Student | Enter a name and a unique ID. IDs are text, so leading zeros are kept. |
| 2. View Students | List students and their IDs. |
| 3. Remove Student | Delete a student and their grades by ID. |
| 4. Exit | Close the program and save your changes. |
| 5. Record Grade | Enter the student ID, subject, and score from 0 to 100. |
| 6. Student Report | View the student's scores, average, and letter grade. |
| 7. Class Summary | View the class average, top students, subject averages, and letter-grade counts. |
| 8. Search Students by Name | Enter part of a name. Matching ignores letter case. |

The class average gives equal weight to each student with recorded grades.
A subject average uses all scores for that subject. The summary includes all
students tied for the highest average. Students without grades are excluded
from averages and letter-grade counts.

The program loads data from data/gradebook.json when it starts and saves on
exit. A missing file starts a new gradebook. If the file is invalid, the
program reports the problem and leaves it available for recovery.

## Code style

For development, install Ruff and run its lint check:

~~~powershell
py -m pip install ruff
py -m ruff check .
~~~
