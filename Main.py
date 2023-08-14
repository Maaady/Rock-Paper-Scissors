while True:
    import datetime, random
    from colorama import Fore
    import colorama
    import fontstyle, winsound

    def red(r):
        print(fontstyle.apply(r, "red"))

    def cyan(c):
        print(colorama.Style.BRIGHT+Fore.CYAN,c)

    def green(g):
        print(fontstyle.apply(g, "green"))

    def blue(b):
        print(Fore.BLUE ,b)

    def lightblue(lb):

        print(colorama.Style.BRIGHT+Fore.LIGHTBLUE_EX,lb)

    def lightgreen(lg):
        print(fontstyle.apply(lg, "light green"))

    def white(w):
        print(colorama.Style.BRIGHT+Fore.YELLOW ,w)

    print(Fore.CYAN,"- "*4," [+] Follow me on Instagram @saadkhan041 ","- "*4)
    print(Fore.LIGHTYELLOW_EX,"\n","- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
    print(Fore.LIGHTRED_EX,"\n","- "*4,"[+] Github: https://github.com/Saadkhan041/ ", "- "*3)
    def game():
        red("Lets Play Rock, paper, scissosrs")
        cyan("1) Rock")
        green("2) Paper")
        blue("3) Scissors")
        user_input = input(white("Enter your choice: ")).lower()
        my_list = ["rock", "r", "paper", "p", "scissors", "scissor", "s"]
        new = ["rock", "paper", "scissors"]
        user_scores = 0
        computer_scores = 0
        total = 10
        computer = random.choice(new)
        if user_input == computer:
            lightblue("Compter:")
            lightgreen(computer)
            lightblue("You:")
            lightgreen(user_input)
            lightgreen("It a tie :-\ ")
            print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
        elif user_input == "rock":
            if computer == "paper":
                red("Compter:")
                white(computer)
                lightblue("You:")
                red(user_input)
                white("Computer won!")
                computer_scores += 1
                cyan("Computer scores: ")
                cyan(computer_scores)
            else:
                white("Compter:")
                cyan(computer)
                blue("You:")
                green(user_input)
                red("Computer wins!")
                lightblue("You Won!")
                user_scores += 1
                cyan("Your scores: ")
                cyan(user_scores)
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())

        elif user_input == "paper":
            if computer == "scissors":
                white("Compter:")
                cyan(computer)
                blue("You:")
                green(user_input)
                red("Computer wins!")
                computer_scores += 1
                cyan("Computer scores: ")
                cyan(computer_scores)
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
            else:
                white("Compter:")
                cyan(computer)
                blue("You:")
                green(user_input)
                red("Computer wins!")
                red("You wins!")
                user_scores += 1
                cyan(("Your Scores scores: ", user_scores))
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
        elif user_input == "rock":
            if computer == "scissors":
                lightblue("Compter:")
                lightgreen(computer)
                lightblue("You:")
                lightgreen(user_input)
                lightblue("Computer wins!")
                computer_scores += 1
                cyan(("Computer scores: ", computer_scores))
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
            else:
                white("Compter:")
                cyan(computer)
                blue("You:")
                green(user_input)
                red("Computer wins!")
                blue("You wins!")
                user_scores += 1
                green(("Your Scores scores: ", user_scores))
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
        else:
            if user_input.isnumeric():
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Dont type numbers :-( \n Type Rock, Ppaer, Scissors")
                print(colorama.Style.BRIGHT + Fore.LIGHTGREEN_EX, "Time:", datetime.datetime.now())
                winsound.Beep(500,500)
            elif user_input not in my_list:
                print(colorama.Style.BRIGHT + Fore.MAGENTA , "See options man!!")
                winsound.Beep(500,500)
    game()
