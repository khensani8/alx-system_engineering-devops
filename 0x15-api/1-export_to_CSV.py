#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import riequests
import csv
import sys

def get_employee_todo_progress(employee_id):
    try:
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        csv_filename = f'{employee_id}.csv'
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in tasks_data:
                csv_writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

