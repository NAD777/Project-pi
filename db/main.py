import sqlite3
from person import Person
class db:
    def __init__(self):
        self.conn = sqlite3.connect('person.db')  # person.db
        self.cursor = self.conn.cursor()

    def commit(self,Person):
        self.cursor.execute("INSERT INTO person VALUES (:time,:id,:in_school)",
                  {'time': Person.time, 'id': Person.id, 'in_school': Person.in_school})
        self.conn.commit()
    def get_date(self,colomn,person):
        self.cursor.execute("SELECT * FROM person WHERE "+colomn+'='+"'"+person+"'") # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
        print(self.cursor.fetchall())
        self.conn.commit()
    def close(self):
            self.conn.close()

#c.execute("""CREATE TABLE  person (
#    time text,
#    id text,
#    in_school  integer
#)""")

time = '13:12'
id = 'Mark'
status = 0
Person1 = Person(time, id, status)
database = db(Person1)
database.commit(Person1)
database.get_date('id','Ilya')
database.close()


