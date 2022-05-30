import sqlite3

connection = sqlite3.connect('database.db')

with open('url-shortner.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()




# import sqlite3

# connection = sqlite3.connect('database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO urlshortener (original_url, short_url) VALUES (?, ?)",
#             ('https://www.youtube.com/watch?v=tPxUSWTvZAs', 'https://www.youtube.com/watch?v=t')
#             )

# cur.execute("INSERT INTO urlshortener (original_url, short_url) VALUES (?, ?)",
#             ('https://gist.github.com/getfutureproof-admin/dfe45adba508f931bf83d144cbbf6bbe', 'https://gist.github.com/getfp-admin/d144cbbf6bbe')
#             )

# connection.commit()
# connection.close()