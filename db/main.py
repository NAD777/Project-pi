import sqlite3
from person import Person

def commit(Person1):
    c.execute("INSERT INTO person VALUES (:time,:id,:in_school)",
              {'time': Person1.time, 'id': Person1.id, 'in_school': Person1.in_school})

    conn.commit()
def get_date(colomn,person):
    c.execute("SELECT * FROM person WHERE "+colomn+'='+"'"+person+"'") # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
    print(c.fetchall())
    conn.commit()

conn = sqlite3.connect('person.db') #person.db

c = conn.cursor()

#c.execute("""CREATE TABLE  person (
#    time text,
#    id text,
#    in_school  integer
#)""")
time = '12'
id='Mark'
status = 0
Person1 = Person(time, id, status)
#commit(Person1)

get_date('id','Ilya')



conn.close()