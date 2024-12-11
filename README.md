# Final-project
Web application final

# Course Table Application

This project is a web application for displaying course data from a PostgreSQL database. The backend is built with Flask (Python), and the frontend is designed using HTML, CSS, and Bootstrap.

## Features

1. View course details including:
   - Course ID
   - Code
   - Name
   - Description
   - Level (e.g., Undergraduate/Graduate)
   - Credits

2. Fetch and display data dynamically from the database.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL

## Database Setup

1. **Create the Database:**
   ```sql
   CREATE DATABASE testnod;
   ```

2. **Create the Table:**
   ```sql
   CREATE TABLE IF NOT EXISTS test (
       id SERIAL PRIMARY KEY,
       code VARCHAR(10) NOT NULL UNIQUE,
       name VARCHAR(100) NOT NULL,
       description TEXT,
       level VARCHAR(20),
       credits INTEGER
   );
   ```

3. **Insert Sample Data:**
   ```sql
   INSERT INTO test (code, name, description, level, credits) VALUES
   ('MATH202', 'Calculus II', 'Advanced calculus concepts.', 'Undergraduate', 3),
   ('CS101', 'Introduction to Computer Science', 'Basics of programming and problem-solving.', 'Undergraduate', 3),
   ('PHYS401', 'Quantum Physics', 'Introduction to quantum mechanics.', 'Graduate', 3),
   ('HIST204', 'Modern History', 'Key events of the 20th century.', 'Graduate', 5),
   ('ENG303', 'Technical Writing', 'Writing for technical audiences.', 'Undergraduate', 3);
   ```

## Application Setup

1. **Install Dependencies:**
   ```bash
   pip install flask psycopg2
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

3. **Access the Application:**
   Open `http://127.0.0.1:5000` in your browser.

---

This simplified structure focuses on core details for easy understanding and quick setup.
