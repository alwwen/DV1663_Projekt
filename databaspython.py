import mysql.connector

cnx = mysql.connector.connect(user='root', password='qwerty',
                              host='127.0.0.1',
                              database='inlämninguppgift')

genres = input("Enter genres (comma-separated): ").split(",")

# Prepare the SQL query
placeholders = ", ".join(["%s"] * len(genres))
query = "SELECT * FROM steeeeeeam WHERE genre IN ({})".format(placeholders)

# Execute the query
cursor = cnx.cursor()
cursor.execute(query, genres)

# Fetch and display the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
cnx.close()
