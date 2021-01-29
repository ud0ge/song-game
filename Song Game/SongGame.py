# MODULES
import random
import time

userPointsTotal = 0
userFailsTotal = 0

i = 1
songs = [
    ("Wellerman", "Longest Johns"),
    ("Thriller", "Michael Jackson"),
    ("Blinding Lights", "The Weekend"),
    ("Levitating", "Dua Lipa"),
    ("Adore Yoy", "Harry Styles"),
    ("Say So", "Doja Cat"),
    ("Still Standing", "Elton John"),
    ("Nevermind", "Dennis Lloyd"),
    ("Africa", "Toto"),
    ("Smile", "Katy Perry"),
    ("Therefore Iam", "Billie Eillish"),
    ("Blue Monday", "New Order")
]

# LOGGING IN
loggedIn = False
while loggedIn == False:
    password = input("Please enter the password to continue!\n")
    if password == "csproject":
        loggedIn = True
    else:
        print("Incorrect password, please try again.")


# FUNCTION

def round():
    userFails = 0
    userPoints = 0
    randomSong = random.choice(songs)

    randomSongName = randomSong[0]
    randomSongArtist = randomSong[1]

    randomSongNameCharacter = randomSong[0][0]
    randomSongArtistCharacter = randomSong[1][0]

    print(f"\n\n\nThe first letter of the song is:\n{randomSongNameCharacter} {'_ '*len(randomSongName)} \nThe first letter of the song artist is:\n{randomSongArtistCharacter} {'_ '*len(randomSongArtist)}\nYou have 2 guesses! Please enter the song name!\n")
    time.sleep(2)
    try1 = input("")

    if try1.lower() == randomSongName.lower() or try1.lower() == randomSongArtist.lower():
        userPoints += 3
        print(f"\n✔️  Well done! The song is {randomSongName} by {randomSongArtist}")
    else:
        try2 = input("This is your last try, please enter the song name!\n")
        if try2.lower() == randomSongName.lower() or try2.lower() == randomSongArtist.lower():
            print(f"✔️  Well done! The song is {randomSongName} by {randomSongArtist}")
            userPoints += 1
        else:
            print(f"Better luck next time! The song was\n{randomSongName} by {randomSongArtist}")
            userFails = userFails + 1
    return (userFails, userPoints)

while userFailsTotal < 2:
    point1, point2 = round()
    userFailsTotal += point1
    userPointsTotal += point2
else:
    print(f"\n\nSorry you got 2 questions incorrect! Better luck next time!\n Your total score was {userPointsTotal}")
    dataFile = open('data.txt', 'a')
    dataFile.write(f"Points = {userPointsTotal}")