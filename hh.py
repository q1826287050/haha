import sqlite3
conn = sqlite3.connect('moblie.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS moblie(item TEXT,quantity INT,price REAL)')
conn.commit()
conn.close()

def insert_item(item,quantity,price):
    conn = sqlite3.connect('moblie.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO moblie VALUES(?,?,?)',(item,quantity,price)
    conn.commit()
    conn.close()
def view_all():
    conn = sqlite3.connect('mobile.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM moblie')
    rows = cur.fetchall()
    conn.close()
    return rows
def search(item):
    conn = sqlite3.connect('moblie.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM moblie WHERE item LIKE ?',(item + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows
def update_one(item,quantitiy,price):
    conn = sqlite3.connect('moblie.db')
    cur = conn.cursor()
    cur.execute('UPDATE moblie SET quantity=?,price=? WHERE item=?',(quantitiy,price,item))
    conn.commit()
    conn.close()
    
def remove_one(item):
    conn = sqlite3.connect('moblie.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM moblie WHERE item=?',(item,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print(search('iPhone'))

conn.close