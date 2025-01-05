import requests
from datetime import datetime

# Define the API endpoint
API_URL = "http://localhost:8000/api/v1/users"

# Define the data to be populated
users = [
    {
        'id': 1,
        'username': 'teste',
        'password': '123',
        'email': 'first_user@example.com',
        'coins': 2000,
        'points': 100,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    },
    {
        'id': 2,
        'username': 'second_user',
        'password': 'hashed_password_2',
        'email': 'second_user@example.com',
        'coins': 1500,
        'points': 80,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    },
    {
        'id': 3,
        'username': 'third_user',
        'password': 'hashed_password_3',
        'email': 'third_user@example.com',
        'coins': 1000,
        'points': 60,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    }
]

# Function to populate the API
def populate_api():
    for user in users:
        response = requests.post(API_URL, json=user)
        if response.status_code == 201:
            print(f"User {user['username']} created successfully.")
        else:
            print(f"Failed to create user {user['username']}. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    populate_api()