#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def get_employee_todo_progress(employee_id):
    try:
        """Fetch user information"""
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        """Fetch tasks information"""
        tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        """Count completed tasks"""
        completed_tasks = [task for task in tasks_data if task.get('completed')]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(tasks_data)

        """Display progress information"""
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        
        """Display titles of completed tasks"""
        for task in completed_tasks:
            print(f"{' ' * 5}{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
