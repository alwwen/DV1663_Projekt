import mysql.connector

def get_matching_genre(genres):
    #establish conection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="qwerty",
        database="inlämninguppgift")
    cursor = connection.cursor()

    #we select every genre and loop throue it to execute the command
    query = "select * from steeeeeeam where genre LIKE '%{}%'".format(genres[0])
    for genre in genres[1:]:
        query += " AND genre LIKE '%{}%'".format(genre)

    cursor.execute(query)
    matching_genre = cursor.fetchall()

    #end conection
    cursor.close()
    connection.close()

    #return the result
    return matching_genre
def findgenre():
    # Prompt the user to enter genres
    genres_input = input("Enter genres (separated by commas): ")
    genres = [genre.strip() for genre in genres_input.split(",")]

    # Get matching genres
    matching_genre = get_matching_genre(genres)

    # Print the matching tables
    if matching_genre:
        print("Matching Tables:")
        for table in matching_genre:
            print(table[0])
    else:
        print("No matching tables found.")

findgenre()
