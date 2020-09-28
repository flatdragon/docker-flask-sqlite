from flask import Flask
import os
import socket
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
  connection = sqlite3.connect("visits.db")
  cursor = connection.cursor()

  cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'visits'")

  tableExists = cursor.fetchone()[0]

  if not tableExists == 1:
    cursor.execute("CREATE TABLE visits (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, amount INTEGER DEFAULT 0)")
    cursor.execute("INSERT INTO visits DEFAULT VALUES")
    connection.commit()

  cursor.execute("SELECT amount FROM visits LIMIT 1")
  visits = cursor.fetchone()[0]
  visits += 1
  cursor.execute("UPDATE visits SET amount = amount + 1")
  connection.commit()
  connection.close()

  html = "<h1>Hello, {name}!</h1>" \
         "<b>Hostname:</b> {hostname}<br/>" \
         "<b>Amount of page visits:</b> {visits}"

  return html.format(
    name = os.getenv("NAME", "world"),
    hostname = socket.gethostname(),
    visits = visits
  )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
