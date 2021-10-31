import math

""" Darren Fulton
My integration project is themed around an old game on a series I played
years ago, but started playing recently
"""

print("Hello! Welcome to my integration project.")

print("This is themed around the game Fate \ndeveloped by WildTangent Games.")

print("An old rouge-like with randomly generated dungeon levels.")

# The end parameter allows
# the print statement have
# a string at the end

print("And don't worry!", end=' ')

print("You can just google the elements regarding the game.")

num1 = int(input(
    "A question! What is the best way to making money in this game?"
    " \n 1)Fishing \n or \n 2)Dungeon crawling "))

# To make it easy to provide a response,
# the user has to input that one correct integer as the answer

# In other words,
# I used if statements to place different responses instead a score system,
# since I do not have the experience for that

# I used the "Python Booleans" section on w3schools

# Used the == operator to ensure the correct answer is the exact integer
if num1 == 1:
    print(
        "Correct! The developers not only allowed the player to get fish,"
        "but to also get rare loot, or even joke items.")
else:
    print("\n Terrible choice.... \n")

print(
    "Another thing to note, the game loves the idea of the boss"
    " being randomized for each game session.")

num2 = input("For example, type a wacky name: ")
num3 = input("Type a weird title (do not use 'the'): ")
num4 = int(input("Lastly, type in a number between 40 and 52: "))

# Used the if statement to only have the integer be between 40 and 52

# The greater than or equal to (>=) and the less than or equal to(<=)
# operators were used to limit the value to be 40 through 52

# The game usually has the boss appear within level 40 through 52

if 40 <= num4 <= 52:
    print(
        "So, when playing, you must defeat " + num2 + " the " + num3 +
        "\n down at level " + str(
            num4) + ", in order to beat the game. \n")
else:  # Used the operator * to print the statement twice
    print((num2 + " the " + num3 + " is disappointed..." + "\n") * 2)

print(
    "So, at this point, you know about fishing in the game"
    " and the weird boss names.")

print("Now let me tell you about what stats do, gameplay-wise.")

print("For example, the game gives the player a base stat of 25 strength.")


def strength(percent_strength,
             flat_strength):
    """Returns the result of strength_num

    :param percent_strength:
    :param flat_strength:
    :return:
    """
    # A formula I found on a page from
    #  someone who used to modify the game,
    # @ https://web.archive.org/web/20111204005055/http://www.surdin.net
    # /fate_tutorials/formulae-of-fate.html
    strength_num = math.floor(
        1 + (int(percent_strength) / 100) * 25 + int(flat_strength))
    return strength_num


# Imported the math module to make use of the math.floor function

# Used the return statement to ensure the value from the calculation comes back

# The 25 represents the character base strength stat and x and y
#  being the different possible bonuses from items, which stacks

# I used the formula so it accurately calculates how an item makes
# your character stronger, through the strength stat

# Unfortunately, the references or "notes" on the page leads to dead links

x = input("Enter a number for damage bonus %: \n")

print("So, you get a sword with a damage bonus enhancement of " + str(
    x) + "% \n")

y = input("Now enter a number to be your added damage bonus: ")

print("And it also has additional damage bonus of", y, "\n")

added_strength = strength(x, y)

print("The weapon ends giving the player a total of:")

print(added_strength + 25, "strength", sep='~ ')

if added_strength != 0 and added_strength > 0:
    # The != statement is not equal to,
    # so the value cannot be exactly zero
    print("Your strength could have been", 25 - added_strength,
          "instead if they were penalties,")
    print("or negative bonuses.")

    # Added a print statement to make use of the ** operator,
    # which is raises the variable to the power of an integer, 10 in this case
    while True:
        # Made use of the NOT operator
        if not added_strength ** 2 == 2147483647:
            # 2147483647 is the biggest integer
            
            print("And with the help of RNG, imagine getting",
                  added_strength ** 2,
                  "of additional strength! \n")
            break
        else:
            break


# Utilized elif for the additional if statement,
# so it can use another expression to evaluate

# Added the OR operator
elif added_strength == 0 or added_strength < 0:
    # to be make the condition to become false, or not be greater than zero
    print("It would be great if you didn't have terrible luck. \n")

print(
    "Keep in mind that a base stat in Fate "
    "is merely the attribute without bonuses, "
    "meaning only the points invested.")
