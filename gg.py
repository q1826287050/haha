import sqlite3
conn = sqlite3.connect('moblie.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS moblie(item TEXT,quantity INT,price REAL)')
conn.commit()
def insert_item(item,quantity,price):
    cur.execute('INSERT INTO moblie VALUES(?,?,?)',(item,quantity,price))
    conn.commit()
def view_all():
    cur.execute('SELECT * FROM moblie')
    rows = cur.fetchall()
    return rows
def search(item):
    cur.execute('SELECT * FROM moblie WHERE item LIKE ?',(item + '%',))
    rows = cur.fetchall()
    return rows
def update_one(item,quantitiy,price):
    cur.execute('UPDATE moblie SET quantity=?,price=? WHERE item=?',(quantitiy,price,item))
    conn.commit()
    
def remove_one(item):
    cur.execute('DELETE FROM moblie WHERE item=?',(item,))
    conn.commit()

if __name__ == '__main__':
    print(search('iPhone'))

conn.close