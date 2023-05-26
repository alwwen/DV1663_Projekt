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
        print("Games matching with the genre {}:".format(genres_input))
        for table in matching_genre:
            print(table[1])  
    else:
        print("No games found for that genre.")
    print("\n")

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
        print("\nYou have spent",round(row[0], 2), "USD\n")

def addGame():
    gamename = input("what game would you like to add?\n")
    cursor.callproc("AddGameToList", [gamename])
    for result in cursor.stored_results():
        output = result.fetchall()

    if output[0][0] == "game found and added.":
        print("Game successfully added to wishlist.")
    elif output[0][0] == "game already exists.":
        print("That game is already in your wishlist.")
    else:
        print("Game not found in steam.")

def showSpecificGame():
    game = input("What game would you like to check out? ")
    query = "SELECT steamdb.name, steamdb.all_reviews, steamdb.original_price from steamdb where steamdb.name = '{}';".format(game)
    cursor.execute(query)
    answers = cursor.fetchall()
    for row in answers:
        print(row[0], row[1], row[2])

def main_loop():
    choice = 0
    while choice != -1:
        print("1. Search for games with specific genre\n" +
              "2. Show your Wishlist\n" +
              "3. Add game to Wishlist\n" +
              "4. Show your played/bought games\n" +
              "5. Show how much money you have spent\n" +
              "6. Search if a specific games exists\n" +
              "To exit the program type -1")
        choice = int(input("Which option do you want to use? \n"+":"))
        if(choice == 1):
            findgenre()
        if(choice == 2):
            showWishlist()
        if(choice ==3):
            addGame()
        if(choice == 4):
            showPlayedGames()
        if(choice == 5):
            showMoneySpent()
        if(choice == 6):
            showSpecificGame()


    print("Have a good day!")



main_loop()





#end conection
cursor.close()
connection.close()