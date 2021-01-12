import sqlite3
import time


def set_up_db():
    conn = sqlite3.connect('RobertSnippetStoreage.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS snippets (snippet_number INTEGER PRIMARY KEY, snippet TEXT, snippet_language TEXT,snippet_name TEXT, snippet_description TEXT, date_created REAL, times_used INTEGER)")
    conn.commit()
    return conn, cursor


def insert_snippet(snippet, snippet_language, snippet_name, snippet_description):
    try:
        conn, cursor = set_up_db()
        cursor.execute("INSERT INTO snippets (snippet_number, snippet, snippet_language, snippet_name, snippet_description, date_created, times_used) VALUES (?, ?, ?,?, ?, ?, ?)",
                       (None, snippet, snippet_language, snippet_name, snippet_description, str(time.time()), 0))
        conn.commit()
        return True
    except:
        return False

# insert_snippet(
#     """
#     import time
#     time.time()
#     """,
#     "Python",
#     "UNIX epoch time",
#     "get the unix epoch time in python"
# )


def query_snippets_by_name(snippet_name):
    conn, cursor = set_up_db()
    query_res = cursor.execute(
        f"SELECT * FROM snippets WHERE snippet_name LIKE '{snippet_name}%'")
    return cursor.fetchall()


def snippet_used(snippet_number):
    conn, cursor = set_up_db()
    cursor.execute(
        'SELECT * FROM snippets WHERE snippet_number=?', (snippet_number, ))
    res = cursor.fetchone()
    cursor.execute('UPDATE snippets SET times_used=? WHERE snippet_number=?', (int(
        res[6]) + 1, snippet_number,))
    conn.commit()
# print(query_snippets_by_name('UNIX'))

# snippet_used('10')


def sort_by_date_created(ascending=True):
    conn, cursor = set_up_db()
    if ascending:
        cursor.execute("SELECT * FROM snippets ORDER BY date_created ASC")
    else:
        cursor.execute("SELECT * FROM snippets ORDER BY date_created DESC")
    return cursor.fetchall()


def delete_snippet(snippet_number):
    try:
        conn, cursor = set_up_db()

        cursor.execute("DELETE FROM snippets WHERE snippet_number=?",
                       (snippet_number, ))

        conn.commit()
        return True
    except:
        return False


def sort_by_usage(most=True):
    conn, cursor = set_up_db()

    if most:
        cursor.execute("SELECT * FROM snippets ORDER BY times_used ASC")
    else:
        cursor.execute("SELECT * FROM snippets ORDER BY times_used DESC")
    return cursor.fetchall()


# delete_snippet(1)

# print(sort_by_date_created())

def parse_snippet(snippet):
    return {
        "snippet_number": snippet[0],
        "snippet": snippet[1],
        "snippet_language": snippet[2],
        "snippet_name": snippet[3],
        "snippet_description": snippet[4],
        "date_created": snippet[5],
        "times_used": snippet[6]
    }


print(parse_snippet((2, '\n    import time\n    time.time()\n    ', 'Python',
                     'UNIX epoch time', 'get the unix epoch time in python', 1610360369.8318243, 0)))

# sort_by_usage()
