from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

def db_create():
    conn = sqlite3.connect("notes.db")
    my_cursor = conn.cursor()

    my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      content TEXT NOT NULL
                      )
                """)
    
    conn.commit()
    conn.close()

db_create()

@app.route("/", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        note = request.form["note"]

        conn = sqlite3.connect("notes.db")
        my_cursor = conn.cursor()

        my_cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()
        conn.close()

        return redirect("/")
    
    conn = sqlite3.connect("notes.db")
    my_cursor = conn.cursor()

    my_cursor.execute("SELECT * FROM notes")
    my_notes = my_cursor.fetchall()

    conn.close()
    return render_template("index.html", notes=my_notes)

@app.route("/delete/<int:id>")
def delete_note(id):
    conn = sqlite3.connect("notes.db")
    my_cursor = conn.cursor()

    my_cursor.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")