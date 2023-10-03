#!/usr/bin/python3
"""
This module provides functionality to fetch employee details and their Todo list

Usage:
    python3 2-export_to_JSON.py EMPLOYEE_ID

Returns:
    A JSON file named {EMPLOYEE_ID}.json with the TODO list for the provided employee ID.

Raises:
    ValueError: If the provided EMPLOYEE_ID is not a valid integer.

Dependencies:
    - requests: To make HTTP requests to the API.
    - json: To handle JSON operations.
    - sys: To access command-line arguments.
"""

import json
import requests
import sys


def export_todo_to_json(employee_id):
    """
    Fetches employee details and their TODO list from a provided API.
    Writes the TODO list in a JSON format to a file named after the employee's ID.

    Args:
    - employee_id (int): The ID of the employee for whom the TODO list needs to be fetched.

    Returns:
    None
    """

    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["username"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data in the desired format
    tasks_list = [{
        "task": task["title"],
        "completed": task["completed"],
        "username": employee_name
    } for task in todos_data]
    data = {str(employee_id): tasks_list}

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    # Ensure correct number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py EMPLOYEE_ID")
        sys.exit(1)

    # Fetch and write the TODO list for the provided employee ID
    try:
        employee_id = int(sys.argv[1])
        export_todo_to_json(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")