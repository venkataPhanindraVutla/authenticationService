# Welcome to Auth Service

## Project Setup

1. **Clone the project on your local machine**
   - Clone this repository:
      ```bash
      git clone https://github.com/venkatPhanindraVutla/Auth_Service
      ```

2. **Install dependencies**
   - Make sure you have Python 3.9+ installed.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Environment Setup**
   - Create a .env file in the root directory and add the following environment variables:
     ```plaintext
     MYSQL_USER=your_user
     MYSQL_PASSWORD=your_password
     MYSQL_SERVER=your_mysql_server
     MYSQL_PORT=3306
     MYSQL_DB=your_database
     SECRET_KEY=your_secret
     PROJECT_NAME=AuthService
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     REFRESH_TOKEN_EXPIRE_MINUTES=1440
     ```

4. **Database Setup**
   - Ensure you have MySQL installed and running on your machine.
   - Create the database manually or let the application handle it.
   - Run the following commands to initialize the database:
     ```bash
     python main.py
     ```

5. **Run the Application**
   - Start the FastAPI server:
     ```bash
     uvicorn app.main:app --reload
     ```
   - The application will be available at `http://127.0.0.1:8000`.

6. **Access API Documentation**
   - Open your browser and navigate to:
     - Swagger UI: `http://127.0.0.1:8000/docs`
     - ReDoc: `http://127.0.0.1:8000/redoc`

---

## Database Design

### Tables:
- **User**
- **Role**
- **User_Roles** (Join Table)

### User Model:
- Manages user credentials and associations with roles.
- **Fields:**
  - `email`: The email address of the user.
  - `password`: The encrypted password of the user.
- **Associations:**
  - A User belongs to many Roles through the `User_Roles` table.

### Role Model:
- Defines the various roles available in the system.
- **Fields:**
  - `name`: The name of the role (e.g., ADMIN, CUSTOMER, AIRLINE_BUSINESS).
- **Associations:**
  - A Role belongs to many Users through the `User_Roles` table.

### User_Roles Table:
- A join table that establishes a many-to-many relationship between Users and Roles.

---

## Seeding Data

- The initial roles (ADMIN, CUSTOMER, AIRLINE_BUSINESS) can be seeded into the database using a script or manually via SQL commands.

---

## Example Environment Variables

For reference, here is an example .env file:
```plaintext
MYSQL_USER=root
MYSQL_PASSWORD=Phani123
MYSQL_SERVER=localhost
MYSQL_PORT=3306
MYSQL_DB=data
SECRET_KEY=143LoveYou
PROJECT_NAME=AuthService
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=1440
```

---

## Features

- **User Authentication:**
  - Signup and Signin functionality with hashed passwords.
  - JWT-based authentication for secure access.

- **Role Management:**
  - Assign roles to users.
  - Check if a user is an admin.

- **API Documentation:**
  - Interactive API documentation available via Swagger UI and ReDoc.

