import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="library_db",
        user="postgres",
        password="newpassword123", 
        cursor_factory=RealDictCursor
    )
    

    # Ensure required tables exist
    _init_db(conn)

    return conn


def _init_db(conn):
    """Create required tables if they do not exist."""
    create_students = """
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        department TEXT,
        year INTEGER
    );
    """
    cur = conn.cursor()
    cur.execute(create_students)
    conn.commit()
    cur.close()

    # Create books table and seed with sample data if empty
    create_books = """
    CREATE TABLE IF NOT EXISTS books (
        book_id SERIAL PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER,
        available BOOLEAN DEFAULT TRUE
    );
    """
    cur = conn.cursor()
    cur.execute(create_books)

    # Insert sample books if table is empty
    cur.execute("SELECT COUNT(*) FROM books;")
    row = cur.fetchone()
    if row is None:
        count = 0
    elif isinstance(row, dict):
        # RealDictCursor returns a mapping, take the first value
        count = list(row.values())[0]
    else:
        count = row[0]
    if count == 0:
        sample_books = [
            ("Introduction to Algorithms", "Cormen et al.", 2009, True),
            ("Clean Code", "Robert C. Martin", 2008, True),
            ("Effective Python", "Brett Slatkin", 2015, True)
        ]
        insert_q = "INSERT INTO books (title, author, year, available) VALUES (%s, %s, %s, %s)"
        for b in sample_books:
            cur.execute(insert_q, b)

    conn.commit()
    cur.close()