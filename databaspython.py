import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Qwerty123",
    database="projekt")
cursor = connection.cursor()

def get_matching_genre(genres):
    #we select every genre and loop throue it to execute the command
    query = "select * from steamDB where genre LIKE '%{}%'".format(genres[0])
    for genre in genres[1:]:
        query += " AND genre LIKE '%{}%'".format(genre)

    cursor.execute(query)
    matching_genre = cursor.fetchall()

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
            print(table[1])
    else:
        print("No matching tables found.")

def showWishlist():
    query = "SELECT wishlist.gameId, steamdb.name, steamdb.all_reviews ,steamdb.original_price from wishlist left join steamdb on wishlist.gameId = steamdb.gameId;"
    cursor.execute(query)
    answers = cursor.fetchall()
    for row in answers:
        print(row[1], row[2])
    

def showPlayedGames():
    query = "SELECT playednotfinished.gameId, steamdb.name, steamdb.genre from playednotfinished left join steamdb on playednotfinished.gameId = steamdb.gameId;"
    cursor.execute(query)
    answers = cursor.fetchall()
    for row in answers:
        print(row[1], row[2])


def showMoneySpent():
    query = "SELECT SUM(steamdb.original_price) from playednotfinished left join steamdb on playednotfinished.gameId = steamdb.gameId;"
    cursor.execute(query)
    answers = cursor.fetchall()
    for row in answers:
        print(row[0])


def main_loop():
    choice = 0
    while choice != -1:
        print("1. Search for games with specific genre\n" +
              "2. Show your Wishlist\n" +
              "3. Show your played/bought games\n" +
              "4. Show how much money you have spent\n" +
              "To exit the program type -1")
        choice = int(input("Which option do you want to use? "))
        if(choice == 1):
            findgenre()
        if(choice == 2):
            showWishlist()
        if(choice == 3):
            showPlayedGames()
        if(choice == 4):
            showMoneySpent()

    print("Have a good day!")
    


main_loop()





#end conection
cursor.close()
connection.close()