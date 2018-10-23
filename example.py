import psycopg2

connection = psycopg2.connect(user='postgres', password='Ireland2017', database='learning', host='localhost')
cursor1 = connection.cursor()
#fight_title = input("Enter fight title: ")
#fighter1_r1 = input("Enter f1 r1 score: ")
"""
cursor1.execute("select attr -> 'round1' from books where id = 3")
cursor2 = connection.cursor()
cursor2.execute("select attr -> 'round2' from books where id = 3")
r1 = cursor1.fetchone()
r2 = cursor2.fetchone()
print(int(r1[0]) + int(r2[0]))
"""
cursor1.execute('insert into orders (info) values (%s)',('{"fighter1": "Pacquiao", "score": {"r1": 10, "r2": 10}}',))
connection.commit()