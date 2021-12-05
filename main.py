""" My integration project, which is themed around an old game of a series
I played years ago, but started playing recently again """
__author__ = "Darren Fulton"

import math


def main():
    """ Starting menu where the user picks a choice """
    print("Hello! Welcome to my integration project.")
    print(
        "This is themed around the game Fate"
        "\ndeveloped by WildTangent Games.")
    print("An old rouge-like with randomly generated dungeon levels.")

    # The end parameter allows the print statement have a string at the end

    print("And don't worry!", end=' ')
    print("You can google 'Fate WildTangent' related searches.")
    print("Pick an option: ")
    # Created a list with the use of brackets
    options = ["Quiz", "Name Generator", "Stat Bonuses", "Quit from program"]
    # The range function displays the different choices
    # And the len function displays the number of items
    # in the list as a value
    for option_number in range(len(options)):
        print(
            str(option_number + 1) + ".", options[option_number])
    option_choice = get_good_int_input("")
    # Used the == operator to ensure the correct answer is the exact integer
    if option_choice == 1:
        quiz()
    elif option_choice == 2:
        name_generator()
    elif option_choice == 3:
        stat_bonuses()
    elif option_choice == 4:
        quit()


def continue_key():
    """ A function that waits for the user to press enter """
    input("Press Enter to continue~")


def answer_listing(the_list):
    """ A function dedicated for listing the answers """
    for number_choice in range(len(the_list)):
        print(
            str(number_choice + 1) + ".", the_list[number_choice])


# A function definition from professor
def get_good_int_input(prompt):
    """ Checks the input is an integer
    :param prompt: The prompt typed and used in the function
    :return good_int: The input that must be an integer
    """
    input_is_valid = True
    while input_is_valid:
        # Used a try-except statement since human error is expected
        try:
            good_int = int(input(prompt))
            input_is_valid = False
            return good_int
        except ValueError:
            print("You didn't type a number. Try again.")


def strength(percentage_strength, flat_strength):
    """ Returns the result of strength_num
    :param percentage_strength: The percentage increase on strength
    :param flat_strength: The flat increase on strength
    :return strength_num: The final value of the character's strength
    """
    # A formula I found on a page from
    #  someone who used to modify the game,
    # @ https://web.archive.org/web/20111204005055/http://www.surdin.net
    # /fate_tutorials/formulae-of-fate.html
    strength_num = math.ceil((1 + (int(percentage_strength) / 100)) * 25 + int(
            flat_strength))
    # The math.ceil method is to make sure the value is rounded up

    # The 25 represents the character base strength stat and x and y
    # being the different possible bonuses from items, which stacks
    # in-game

    # I used the formula so it accurately calculates how an item makes
    # your character stronger, through the strength stat

    # Unfortunately, the references or "notes"
    # on the page leads to dead links

    # Used the return statement to ensure
    # the value from the calculation comes back
    return strength_num


def quiz():
    """ Starts up a quiz on the game """
    points = 0
    print("The quiz consists of three simple questions.")
    print("First question: \n")
    print("What is the best way to earn money in the game?")
    question_one = ["Fishing", "Dungeon Crawling", "Quests"]
    answer_listing(question_one)
    num1 = get_good_int_input("")
    # Used the % operator to dictate if the number was odd
    if num1 % 2 == 1 and num1 == 1:
        print(
            "\n Correct! The developers not only allowed the player to get "
            "fish, but to also get rare loot, or even joke items.")
        points += 1
        continue_key()
    else:
        print("\n Wrong answer. The correct answer was Fishing.")
        continue_key()
    print("Second question: \n")
    print("The easiest build to go for is...")
    # Hint:
    question_two = ["Balanced", "Attack Speed", "Pure Strength", "Pure Magic"]
    answer_listing(question_two)
    num2 = get_good_int_input("")
    if num2 == 4:
        print("\n Correct! The main reason why straight magic is the easiest, "
              "it's because only magic has AOE or area of effect.")
        points += 1
        continue_key()
    else:
        print("\n Wrong answer. The correct answer was Pure Magic.")
        continue_key()
    print("Third and final question: \n")
    print("Does the retirement feature break the game?")
    #
    question_three = ["Yes, since it simply passes down gear and makes it "
                      "stronger",
                      "Yes, since it passes down gear, makes it stronger, "
                      "and it can be done infinitely", "No, it doesn't"]
    answer_listing(question_three)
    num3 = get_good_int_input("")
    if num3 == 2:
        print("\n Correct! You can keep on retiring and pass down the gear "
              "to your descendant every time. "
              "If you do that with gear that does "
              "not have requirements, the game becomes a breeze.")
        points += 1
        continue_key()
    else:
        print("\n Wrong answer. The correct answer was number 2.")
        continue_key()
    print("\n Adding up all the points, you got", points, "out of 3.")
    print("Hopefully you got the score you wanted.")
    continue_key()
    shameless_plug()


def name_generator():
    """ A example about the name the final boss has in-game """
    print(
        "The game loves the idea of having the boss "
        "be randomized, both in enemy type and name for each game session.")
    wacky_name = str(input("For example, type a wacky name: "))
    print(wacky_name + " the...")
    wacky_title = str(input("Type a weird title: "))
    level_number = get_good_int_input("Lastly, type in a number between 40 "
                                      "and 52: ")

    # Used the if statement to only have the integer be between 40 and 52

    # The greater than or equal to (>=) and the less than or equal to(<=)
    # operators were used to limit the value to be 40 through 52

    # The game usually has the boss appear within level 40 through 52

    if 40 <= level_number <= 52:
        print(
            "So, when playing, you must defeat " + wacky_name + " the " +
            wacky_title +
            "\n down at level " + str(
                level_number) + ", in order to beat the game. \n")
    else:  # Used the operator * to print the statement twice
        print(
            (wacky_name + " the " + wacky_title + " is disappointed..." + "\n")
            * 2)
        print("You are not in the 40 to 52 level range.")
    print("You will encounter enemies besides the final boss with "
          "special names as well.")
    continue_key()
    shameless_plug()


def stat_bonuses():
    """ An example regarding enhancements by using the strength stat """
    print("Let me tell you about what stats do, gameplay-wise.")
    print("For this example, the game gives the player a base stat of 25 "
          "strength.")
    x = get_good_int_input("Enter a number for damage bonus %: \n")
    print("So, you get a sword with a damage bonus enhancement of " + str(
        x) + "% \n")
    y = get_good_int_input("Now enter a number "
                           "to be your added damage bonus: ")
    print("And it also has additional damage bonus of", y, "\n")
    added_strength = strength(x, y)
    print("The weapon ends giving the player a total of:")
    # the sep= statement is the syntax at the end of a print statement
    print(added_strength + 25, "strength", sep='~ ')
    # The != statement is not equal to,
    # so the value cannot be exactly zero
    if 0 < added_strength != 0:
        # Used the // operator does floor division
        # It simply rounds the value that results from the division
        print("Your strength could have been", int(25 // 4) - added_strength,
              "instead if they were penalties,")
        print("or negative bonuses.")
        # Added a print statement to make use of the ** operator,
        # which is raises the variable to the power of an integer
        while True:
            # Made use of the NOT operator
            if not added_strength ** 2 == 2147483647:
                # 2147483647 is the biggest integer in
                # 32-bit systems
                # https://en.wikipedia.org/wiki/2,147,483,647
                print("And with the help of RNG, imagine getting",
                      added_strength ** 2,
                      "of additional strength! \n")
                # The break keyword stops the loop from going
                # infinitely
                break
            else:
                break
    # Utilized elif for the additional if statement
    # Added the OR operator
    elif added_strength == 0 or added_strength < 0:
        print("It would be great if you didn't have terrible luck.\n")
    print(
        "Keep in mind that a base stat in Fate "
        "is merely the attribute without bonuses, "
        "meaning only the points invested.")
    continue_key()
    shameless_plug()


def shameless_plug():
    """ A footnote for the program """
    print("\n" + "The last thing I want to state is the fact "
                 "I grew up with this game.")
    print("And me being me, I believe you should give it a try.")
    print("GOG.com is my recommended site for old and DRM-free games.")


main()
