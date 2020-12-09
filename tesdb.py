import sqlite3
conn = sqlite3.connect('/media/usb/tesdb.db')
c = conn.cursor()

c.execute('PRAGMA table_info(data);')
print(c.fetchone())
