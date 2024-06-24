# Event Management API

This document provides a comprehensive guide to setting up, configuring, and using the backend API for an event management system. The API is built using Flask, SQLAlchemy, and Flask-Login, and allows for user authentication and event management.

## Table of Contents

- [Feature](@)
- [Installation](@)
- [Configuration](@)
- [Usage](@)
  - [Running the Application](@)
  - [Running with Docker(Optional)](@)
- [API Endpoints](@)
  - [Authentication](@)
    - [Sign Up](@)
    - [Login](@)
    - [Logout](@)
- [Example Requests](@)
  - [Using `curl` for API Requests](@)
    - [Sign Up:](@)
    - [Login:](@)
    - [Logout:](@)
- [Contributing](@)
- [License](@)

## Features

- User authentication (signup, login, logout)
- Secure password hashing with bcrypt.
- Session management with Flask-Login
- CORS support for cross-origin requests.
- Database migrations with Flask-Migrate

## Installation 

1. **Clone the repository**:

- Use the following command to clone the repository to your local machine:
  
```bash
git clone https://github.com/Dinah-Ngatia5/event-management-api.git
cd event-management-api
```

2. **Create a virtual environment**:

- A virtual environment is necessary to manage dependencies and isolate them from the global Python environment. Create and activate a virtual environment with these commands:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies**:

- Install the required dependencies listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt

```

4. **Set up the database**:

- Initialize and set up the database with Flask-Migrate commands. Run the following commands to create the database, apply migrations, and set it up:

```csharp
flask db init
flask db migrate
flask db upgrade
```

5. **Seed the database**:

- If you have a `seed.py` file to populate the database with initial data, run this command:

```bash
python seed.py
```

## Configuration

Configuration settings are managed in the `server/config.py` file. Here are the key settings:

- `SQLALCHEMY_DATABASE_URI`: The URI of the database to connect to.
- `SECRET_KEY`: A secret key used for session management and other security-related features.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Set this to `False` to disable modification tracking and save resources.

## Usage

1. **Run the application**:

- Start the Flask application with the following command:

```bash
flask run #or  Option 2: python manage.py
```

- The server will start and listen for requests at `http://localhost:5000`.

2. Run with Docker (optional):

- If you prefer using Docker, you can build and run the application using these commands:

```bash
docker build -t event-management-api .
docker run -p 5000:5000 event-management-api

```

## API Endpoints

### Authentication

#### Signup

- URL: `/signup`
- Method: `POST`
- Data Params:
  - The request body should include a JSON object with the following fields:
  
```json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
}

```

- Success Response:
  - Code: 200
  - Content: `{ "message": "User registered successfully" }`
  
- Error Response
  - Code: 400
  - Content: `{ "message": "Error message here" }`

#### Login

- URL: `/login`
- Method: `POST`
- Data Params:
  - The request body should include a JSON object with the following fields:
  
```json
{
    "email": "your_email@example.com",
    "password": "your_password"
}

```

- Success Response:
  - Code: 200
  - Content: `{ "message": "Login successful" }`
  
- Error Response:
  - Code: 401
  - Content: `{ "message": "Invalid credentials" }`


#### Logout

- URL: `/logout`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{ "message": "Logged out successfully" }`


## Example Requests

### Using `curl` for API Requests

#### Sign Up:

Use this `curl` command to send a signup request to the API:

```bash
curl -X POST http://localhost:5000/signup \
-H "Content-Type: application/json" \
-d '{
    "username": "dainah-5",
    "email": "dinahngatia86@gmail.com",
    "password": "aldfwieo234"
}'
```

#### Login:

Use this `curl` command to send a login request to the API:

```bash
curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{
    "email": "dinahngatia86@gmail.com",
    "password": "aldfwieo234"
}'

```

#### Logout:

Use this `curl` command to send a logout request to the API:

```bash
curl -X GET http://localhost:5000/logout

```

## Contributing

Please feel to send me a [pull request](@) or open an [issue](@) incase of any bugs.

## License 

See [MIT Licensed](@)