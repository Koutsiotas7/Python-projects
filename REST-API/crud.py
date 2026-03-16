from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS posts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT
                   )
                   """)
    
    conn.commit()
    conn.close()

create_db()

@app.route("/posts", methods = ["GET"])
def get_posts():
    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    conn.close()

    results = []

    for post in posts:
        results.append({
            "id": post[0],
            "title": post[1],
            "content": post[2]
        })
    
    return jsonify(results)

@app.route("/posts/<int:id>", methods = ["GET"])
def get_post(id):
    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts WHERE id=?", (id,))
    post = cursor.fetchone()

    conn.close()

    if post:
        return jsonify({
            "id": post[0],
            "title": post[1],
            "content": post[2]
        })
    
    return jsonify({"error": "Post is not found!"})

@app.route("/posts", methods = ["POST"])
def new_post():
    data = request.get_json()
    title = data["title"]
    content = data["content"]

    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                   (title, content)
                   )

    conn.commit()
    conn.close()

    return jsonify({"message": "New post is created!"})

@app.route("/posts/<int:id>", methods = ["PUT"])
def update_post(id):
    data = request.get_json()
    title = data["title"]
    content = data["content"]

    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE posts SET title=?, content=? WHERE id=?",
                   (title, content, id)
                   )
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Post not found"}), 404

    conn.commit()
    conn.close()

    return jsonify({"message": "This post was updated!"})

@app.route("/posts/<int:id>", methods = ["DELETE"])
def delete_post(id):
    conn = sqlite3.connect("posts.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts WHERE id=?", (id,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "This post has been deleted!"})