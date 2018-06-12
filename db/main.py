import sqlite3
from person import Person
class db(Person):
    def __init__(self,Person):
        self.Person1=Person
        self.conn = sqlite3.connect('person.db')  # person.db
        self.c = self.conn.cursor()
        self.time = '12'
        self.id = 'Mark'
        self.status = 0

    def commit(self,Person1):
        self.c.execute("INSERT INTO person VALUES (:time,:id,:in_school)",
                  {'time': Person1.time, 'id': Person1.id, 'in_school': Person1.in_school})
        self.conn.commit()
    def get_date(self,colomn,person):
        self.c.execute("SELECT * FROM person WHERE "+colomn+'='+"'"+person+"'") # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
        print(self.c.fetchall())
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


