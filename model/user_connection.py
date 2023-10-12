import psycopg
from dotenv import load_dotenv
import os

load_dotenv()
DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

class UserConnection():
  conn = None
  def __init__(self):
    try:
      self.conn = psycopg.connect("dbname=" + DBNAME + " user=" + USER + " password=" + PASSWORD + " host= " + HOST + " port=" + PORT)
    except psycopg.OperationalError as err:
      print(err)
      self.conn.close()

  def read_all(self):
    with self.conn.cursor() as cur:
      data = cur.execute("""
        SELECT * FROM "user"
      """)
      return data.fetchall()
    
  def read_one(self, id):
    with self.conn.cursor() as cur:
      data = cur.execute("""
        SELECT * FROM "user" WHERE id = %s
      """, (id,))
      return data.fetchone()

  def write(self, data):
    with self.conn.cursor() as cur:
      cur.execute("""
        INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
      """, data)
    self.conn.commit()

  def update(self, data):
    with self.conn.cursor() as cur:
      cur.execute("""
        UPDATE "user" SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s
      """, data)
    self.conn.commit()

  def delete(self, id):
    with self.conn.cursor() as cur:
      cur.execute("""
        DELETE FROM "user" WHERE id = %s
      """, (id,))
    self.conn.commit()

  def __def__(self):
    self.conn.close()