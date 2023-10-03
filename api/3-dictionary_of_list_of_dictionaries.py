#!/usr/bin/python3
import json
import requests

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Fetch all users
users_response = requests.get(f"{BASE_URL}/users")
users = users_response.json()

# Dictionary to hold all the data
all_data = {}

# Loop through each user and fetch their tasks
for user in users:
    user_id = user["id"]
    username = user["username"]

    # Fetch tasks for this user
    todos_response = requests.get(f"{BASE_URL}/todos?userId={user_id}")
    todos_data = todos_response.json()

    # Format tasks for this user
    tasks_list = [{
        "username": username,
        "task": task["title"],
        "completed": task["completed"]
    } for task in todos_data]

    all_data[str(user_id)] = tasks_list

# Write the data to the JSON file
filename = "todo_all_employees.json"
with open(filename, 'w') as file:
    json.dump(all_data, file)

filename