import mysql.connector
from mysql.connector import Error

# Database connection details
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # replace with your username
            password='your_password',  # replace with your password
            database='gym_management'  # replace with your database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Task 1: Add a Member
def add_member(connection, id, name, age):
    try:
        cursor = connection.cursor()
        sql_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(sql_query, (id, name, age))
        connection.commit()
        print(f"Member {name} added successfully.")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# Task 2: Add a Workout Session
def add_workout_session(connection, member_id, session_date, session_time, activity):
    try:
        cursor = connection.cursor()
        sql_query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_query, (member_id, session_date, session_time, activity))
        connection.commit()
        print(f"Workout session added for member ID {member_id}.")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# Task 3: Update Member Information
def update_member_age(connection, member_id, new_age):
    try:
        cursor = connection.cursor()
        # Check if member exists
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        if cursor.fetchone() is None:
            print(f"No member found with ID {member_id}.")
            return

        sql_query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(sql_query, (new_age, member_id))
        connection.commit()
        print(f"Updated age for member ID {member_id}.")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# Task 4: Delete a Workout Session
def delete_workout_session(connection, session_id):
    try:
        cursor = connection.cursor()
        sql_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(sql_query, (session_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"No workout session found with ID {session_id}.")
        else:
            print(f"Deleted workout session with ID {session_id}.")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# Advanced Task: Get Members in Age Range
def get_members_in_age_range(connection, start_age, end_age):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(sql_query, (start_age, end_age))
        members = cursor.fetchall()
        print(f"Members between ages {start_age} and {end_age}:")
        for member in members:
            print(member)
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# Main execution
if __name__ == "__main__":
    conn = create_connection()

    # Add Members
    add_member(conn, 1, 'Jane Doe', 28)
    add_member(conn, 2, 'John Smith', 35)

    # Add Workout Session
    add_workout_session(conn, 1, '2024-10-01', 'Morning', 'Yoga')
    add_workout_session(conn, 2, '2024-10-02', 'Evening', 'Weightlifting')

    # Update Member Age
    update_member_age(conn, 1, 29)

    # Delete Workout Session
    delete_workout_session(conn, 1)

    # Get Members in Age Range
    get_members_in_age_range(conn, 25, 30)

    # Close the connection
    if conn.is_connected():
        conn.close()
        print("Connection closed.")
