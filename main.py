
print("Hello, user!\nWelcome to Python Tutorial Program!")
user = input("Would you like to proceed?(YES/NO) ").upper()

if user == "YES":
    while True:
        print("=" * 40)
        print("1. Introduction to Programming")
        print("2. Basic Syntax")
        print("3. Arithmetic Operators and Expressions")
        print("4. Basic Input and Output")
        print("5. Conditional Statements")
        print("6. Logical Operator")
        print("7. Introduction to Iteration and Loops")

        user1 = int(input("\nWhat lesson do you want? "))

        if user1 == 1:
            print("=" * 40)
            print(" WHAT IS PROGRAMMING LANGUAGE?")
            print(" - A programming language is a special language that computers understand and use to perform tasks.")
            print()
            print(" COMMON PROGRAMMING LANGUAGE INCLUDE:")
            print("  - PYTHON")
            print("  - C/C++")
            print("  - PHP")
            print("  - JAVA")
            print("  - JavaScript")
            print("  - Ruby")

            next = input("\nType 'NEXT' to proceed: ").upper()

            if next == "NEXT":
                print("=" * 40)
                print(" WHAT IS PYTHON PROGRAMMING")
                print(" - Python is a high-level, interpreted, and general-purpose programming language designed to be simple, readable, and easy to learn.")
                print(" - Python is a widely used programming language that was created by Guido van Rossum in 1991.")
                print()
                print(" WHO IS GUIDO VAN ROSSUM?")
                print(" - Guido van Rossum is a dutch software engineer best known for creating the Python programming language in 1991")

                next1 = input("\nType 'NEXT' to proceed: ").upper()

                if next1 == "NEXT":
                    print("=" * 40)
                    print(" WHY LEARN PYTHON?")
                    print("  1. Simple and easy to learn")
                    print("  2. Readable Syntax")
                    print("  3. Versatile")
                    print("  4. Huge Community")
                    print("\n   LESSON 1 COMPLETED!")
                    print("It's time to test your knowledge!")
                    print("\nThere are 5 questions. Each correct answer is 1 point.")

                    ready = input("Are you ready for the quiz? (YES/NO): ").upper()

                    if ready == "YES":
                        print()
                        print("LET'S BEGIN THE QUIZ!")
                        print("=" * 40)
                        score = 0

                        print("1. What is a programming language?")
                        print("A. A language used only by humans")
                        print("B. A language computers understand")
                        print("C. A type of computer hardware")
                        print("D. An internet browser")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct!")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")
                            print()

                        print("2. Who created Python?")
                        print("A. Bill Gates")
                        print("B. Mark Zuckerberg")
                        print("C. Guido van Rossum")
                        print("D. Steve Jobs")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct!")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")
                            print()

                        print("3. When was Python created?")
                        print("A. 1985")
                        print("B. 1991")
                        print("C. 2000")
                        print("D. 2010")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct!")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")
                            print()

                        print("4. Which of the following is a programming language?")
                        print("A. Python")
                        print("B. Google")
                        print("C. Windows")
                        print("D. Facebook")
                        answer = input("Your answer: ").upper()

                        if answer == "A":
                            print("Correct!")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is A.")
                            print()

                        print("5. Why is Python popular among beginners?")
                        print("A. It is difficult to understand")
                        print("B. It only works on computers")
                        print("C. It has simple and readable syntax")
                        print("D. It cannot perform calculations")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct!")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")

                        print()
                        print("=" * 40)
                        print("             QUIZ RESULTS")
                        print("=" * 40)
                        print("Your Score:", score, "/ 5")

                        if score == 5:
                            print("Excellent! Perfect score!")
                        elif score >= 3:
                            print("Good job! You understood the lesson!")
                        else:
                            print("Keep practicing! Review the lesson and try again.")

                        print("=" * 40)

                    elif ready == "NO":
                        print("You can take the quiz when you're ready!")
                    else:
                        print("Invalid Input")

                else:
                    print("Invalid Input")
                    exit()

            else:
                print("Invalid Input")
                exit()

        elif user1 == 2:
            print("=" * 40)
            print(" PYTHON BASIC SYNTAX")
            print(" - Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
            print(" 1. Python is Case-Sensitive\n- Python treats uppercase and lowercase letters differently.")
            print(" 2. Indentation\n- Unlike other programming languages, Python uses indentation (spaces) to define blocks of code.")
            print()
            print(" PRINTING OUTPUT")
            print("  PRINT STATEMENT")
            print("  - The print() function displays information on the screen.")
            print("  print - The function that display output.")
            print("  () - Parentheses that contain the information to be displayed.")
            print("  value - The text, number, variable, or expression you want to show.")
            print("  PRINTING TEXT")
            print("  - Text (also called string) must be enclosed in quotation marks.")
            print("  PRINTING NUMBERS")
            print("  - You can print numbers directly without quotation marks.")

            next = input("\nType 'NEXT' to proceed: ").upper()

            if next == "NEXT":
                print("=" * 40)
                print(" PYTHON COMMENTS")
                print(" - Comments ignored by Python.")
                print(" - They are used to explain the code.")
                print(" - Uses the hashtag symbol")
                print()
                print(" VARIABLES, CONSTANTS, AND DATA TYPES IN PYTHON")
                print("  WHAT IS A VARIABLE?")
                print("  - A variable is a named storage location used to keep data in a program. The value of a variable can change while the program is running.")
                print("  VARIABLE NAMING RULES:")
                print("  - A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).")
                print("  - A variable name must start with a letter or the underscore character.")
                print("  - A variable name cannot start with a number.")
                print("  - Variable names are case-sensitive\n    (age and AGE are two different variables)")

                next1 = input("\nType 'NEXT' to proceed: ").upper()

                if next1 == "NEXT":
                    print("=" * 40)
                    print(" ASSIGNED VALUE TO VARIABLE")
                    print(" - In programming, we store data in variables. We assign a value to a variable using the = (assignment operator).")
                    print()
                    print(" OUTPUT VARIABLES")
                    print(" - The Python print() function is often used to output variables.")
                    print(" - In the print() function, you output multiple variables, separated by a comma.")
                    print(" - In the print() function, you output multiple variables, separated by a +.")
                    print()
                    print(" BASIC DATA TYPES IN PYTHON")
                    print(" - Data types are categories that tell Python what kind of data a variable stores. They determine the type of value a variable can hold and what operations can be performed on that value.")
                    print(" int - Integer numbers\n float - Decimal numbers\n str - String or text\n bool - Boolean values")

                    print("\nLESSON 2 COMPLETED!")
                    print("It's time to test your Python syntax skills!")
                    print("\nMINI-GAME: FIND THE ERROR!")
                    print("There are 5 questions. Each correct answer is 1 point.")

                    ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

                    if ready == "YES":
                        print("\nLET'S BEGIN THE CHALLENGE!")
                        print("=" * 40)
                        score = 0

                        print("1. Which line has an error?")
                        print("A. print('Hello World')")
                        print("B. Print('Hello World')")
                        print("C. print(100)")
                        print("D. print('Python')")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! Python is case-sensitive.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("2. What is wrong with this code?")
                        print("if age >= 18:")
                        print("print('Adult')")
                        print("A. Missing quotation marks")
                        print("B. Incorrect indentation")
                        print("C. Incorrect variable name")
                        print("D. Missing parentheses")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! The statement inside the if block needs indentation.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("3. Which variable name is INVALID?")
                        print("A. student_name")
                        print("B. age")
                        print("C. 1student")
                        print("D. total_score")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct! A variable name cannot start with a number.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")

                        print()
                        print("4. Which line correctly creates a comment?")
                        print("A. // This is a comment")
                        print("B. # This is a comment")
                        print("C. ** This is a comment")
                        print("D. comment: This is a comment")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! Python uses the # symbol for comments.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("5. What data type is the value 3.14?")
                        print("A. int")
                        print("B. str")
                        print("C. bool")
                        print("D. float")
                        answer = input("Your answer: ").upper()

                        if answer == "D":
                            print("Correct! Decimal numbers use the float data type.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is D.")

                        print()
                        print("=" * 40)
                        print("             GAME RESULTS")
                        print("=" * 40)
                        print("Your Score:", score, "/ 5")

                        if score == 5:
                            print("Excellent! You're a Python Syntax Master!")
                        elif score >= 3:
                            print("Good job! You understand the basics!")
                        else:
                            print("Keep practicing! Review Lesson 2 and try again.")

                        print("=" * 40)

                    elif ready == "NO":
                        print("You can play the challenge when you're ready!")
                    else:
                        print("Invalid Input")

                else:
                    print("Invalid Input")
                    exit()

            else:
                print("Invalid Input")
                exit()

        elif user1 == 3:
            print("=" * 40)
            print(" WHAT ARE ARITHMETIC OPERATORS?")
            print(" - Arithmetic operators are symbols used to perform mathematical calculations on numbers. They work the same way as the operators used in everyday mathematics.")
            print()
            print(" PYTHON ARITHMETIC OPERATORS")
            print("  + Addition")
            print("  - Subtraction")
            print("  * Multiplication")
            print("  / Division (float)")
            print("  // Floor Division")
            print("  % Modulus")
            print("  ** Exponentiation")
            print()
            print(" EXPRESSIONS IN PYTHON")
            print(" - An expression is a combination of values, variables, and operators that evaluates to a result.")
            print(" - Python follows the order of operations (PEMDAS):")
            print("    P Parentheses\n    E Exponents\n    M Multiplication\n    D Division\n    A Addition\n    S Subtraction")

            print("\nLESSON 3 COMPLETED!")
            print("It's time to test your math skills!")
            print("\nMINI-GAME: PYTHON MATH CHALLENGE!")
            print("There are 5 questions. Each correct answer is 1 point.")

            ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

            if ready == "YES":
                print()
                print("LET'S BEGIN THE CHALLENGE!")
                print("=" * 40)
                score = 0

                print("1. What is the result of 15 + 10?")
                print("A. 20")
                print("B. 25")
                print("C. 30")
                print("D. 35")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    print("Correct! 15 + 10 = 25.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is B.")

                print()
                print("2. What is the result of 20 // 3?")
                print("A. 6")
                print("B. 6.67")
                print("C. 2")
                print("D. 7")
                answer = input("Your answer: ").upper()

                if answer == "A":
                    print("Correct! Floor division gives the whole-number quotient.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is A.")

                print()
                print("3. What is the result of 17 % 5?")
                print("A. 3")
                print("B. 5")
                print("C. 2")
                print("D. 0")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    print("Correct! Modulus gives the remainder.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is C.")

                print()
                print("4. What is the result of 4 ** 2?")
                print("A. 8")
                print("B. 12")
                print("C. 16")
                print("D. 20")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    print("Correct! Exponentiation means raising a number to a power.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is C.")

                print()
                print("5. What is the result of 5 + 3 * 2?")
                print("A. 16")
                print("B. 11")
                print("C. 13")
                print("D. 10")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    print("Correct! Multiplication is performed before addition.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is B.")

                print()
                print("=" * 40)
                print("             GAME RESULTS")
                print("=" * 40)
                print("Your Score:", score, "/ 5")

                if score == 5:
                    print("Excellent! You're a Python Math Master!")
                elif score >= 3:
                    print("Good job! You understand arithmetic operators!")
                else:
                    print("Keep practicing! Review Lesson 3 and try again.")

                print("=" * 40)

            elif ready == "NO":
                print("You can play the challenge when you're ready!")
            else:
                print("Invalid Input")

        elif user1 == 4:
            print("=" * 40)
            print(" ACCEPTING USER INPUT")
            print("  - Purpose of input in programming\n   Real-life analogies (e.g., asking for a user's name and responding)")
            print()
            print(" ACCEPTING USER INPUT")
            print("  name = input('Enter your name: ')\n  age = input('Enter your age: ')")
            print(" Using input() function")
            print(" Syntax: variable=input('Prompt message: ')")
            print(" All input is string type by default")
            print()
            print(" FORMATTING OUTPUT")
            print("A. Using comma, in print():")
            print("  name = input('Enter your name: ')\n  age = input('Enter your age: ')")
            print("  print('name', name)\n  print('age', age)")
            print()
            print(" CONVERTING INPUT TO OTHER DATA TYPES")
            print("B. Float input (for decimal numbers)")
            print("  grade = float(input('Enter your grade: '))")
            print("  print(f'Your grade is: {grade}')")
            print("C. Boolean Input (True or False using conditions)")
            print("  answer = input('Are you a student? (yes/no): ')")
            print("  is student answer.lower() === 'yes'")
            print("  print('Student status:', is_student)")
            print()
            print(" Example Program (Combining All)")
            print("name = input('Enter your name: ')")
            print("age = int(input('Enter your age: '))")
            print("grade = float(input('Enter your final grade: '))")
            print("print(f'Student: {name}, Age: {age}, Final grade: {grade})")

            print("\nLESSON 4 COMPLETED!")
            print("It's time to test your knowledge!")
            print("\nMINI-GAME: INPUT AND OUTPUT CHALLENGE!")
            print("There are 5 questions. Each correct answer is 1 point.")

            ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

            if ready == "YES":
                print()
                print("LET'S BEGIN THE CHALLENGE!")
                print("=" * 40)
                score = 0

                print("1. Which Python function is used to accept information from the user?")
                print("A. print()")
                print("B. input()")
                print("C. type()")
                print("D. int()")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    print("Correct! input() accepts information from the user.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is B.")

                print()
                print("2. What data type does input() return by default?")
                print("A. Integer")
                print("B. Float")
                print("C. String")
                print("D. Boolean")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    print("Correct! input() returns the entered value as a string.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is C.")

                print()
                print("3. Which function converts a value into an integer?")
                print("A. str()")
                print("B. float()")
                print("C. bool()")
                print("D. int()")
                answer = input("Your answer: ").upper()

                if answer == "D":
                    print("Correct! int() converts a value into an integer.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is D.")

                print()
                print("4. What is the purpose of an f-string?")
                print("A. To repeat a statement")
                print("B. To format output using variables")
                print("C. To accept user input")
                print("D. To convert text into an integer")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    print("Correct! F-strings allow variables to be placed inside formatted text.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is B.")

                print()
                print("5. Which function converts a value into a decimal number?")
                print("A. int()")
                print("B. str()")
                print("C. float()")
                print("D. input()")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    print("Correct! float() converts a value into a decimal number.")
                    score += 1
                else:
                    print("Incorrect! The correct answer is C.")

                print()
                print("=" * 40)
                print("             GAME RESULTS")
                print("=" * 40)
                print("Your Score:", score, "/ 5")

                if score == 5:
                    print("Excellent! You're an Input and Output Master!")
                elif score >= 3:
                    print("Good job! You understood the lesson!")
                else:
                    print("Keep practicing! Review Lesson 4 and try again.")

                print("=" * 40)

            elif ready == "NO":
                print("You can play the challenge when you're ready!")
            else:
                print("Invalid Input")

        elif user1 == 5:
            print("=" * 40)
            print(" INTRODUCTION TO CONDITIONAL STATEMENTS")
            print(" - A conditional statement allows a program to make decisions based on whether a condition is True or False.")
            print("\n BASIC STRUCTURE:\n  if condition:\n      statement")
            print()
            print(" RELATIONAL OPERATORS")
            print(" - Relational operators, also called comparison operators, are used to compare two values. The result is always either True or False.")
            print("  == Equal to")
            print("  != Not equal to")
            print("  > Greater than")
            print("  < Less than")
            print("  >= Greater than or equal to")
            print("  <= Less than or equal to")

            next = input("\nType 'NEXT' to proceed: ").upper()

            if next == "NEXT":
                print("=" * 40)
                print(" THE if STATEMENT")
                print(" - The if statement executes a block of code only when a condition is true.")
                print(" - If the condition is False, the intended block is skipped.")
                print("SYNTAX")
                print("if condition:\n  statement")
                print()
                print(" THE if-else STATEMENT")
                print(" - The else statement provides an alternative when the if condition is false.")
                print("SYNTAX")
                print("if condition:\n  statement\nelse:\n  statement")
                print("KEY POINTS:")
                print(" • Use else when you want an alternative action if the if condition is false.")
                print(" • Only one of the if or else block will be executed.")

                next1 = input("\nType 'NEXT' to proceed: ").upper()

                if next1 == "NEXT":
                    print("=" * 40)
                    print(" THE if-elif-else STATEMENT")
                    print(" - The elif statement is used when there are multiple conditions to evaluate. Python checks each condition from top to bottom and executes the first condition that is True.")
                    print("SYNTAX")
                    print("if condition1:\n  statement\nelif condition2:\n  statement\nelse:\n  statement")
                    print()
                    print(" NESTED CONDITION IN PYTHON")
                    print(" - A nested condition is a condition inside another condition.")
                    print("SYNTAX")
                    print("if condition1:\n  if condition2:\n    statement\n  else:\n    statement\nelse:\n  statement")

                    print("\nLESSON 5 COMPLETED!")
                    print("It's time to test your decision-making skills!")
                    print("\nMINI-GAME: DECISION-MAKING CHALLENGE!")
                    print("There are 5 challenges. Each correct answer is 1 point.")

                    ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

                    if ready == "YES":
                        print()
                        print("LET'S BEGIN THE CHALLENGE!")
                        print("=" * 40)
                        score = 0

                        print("1. A student has a grade of 90.")
                        print("What will this condition display?")
                        print("grade = 90")
                        print("if grade >= 75:")
                        print("    print('PASSED')")
                        print("else:")
                        print("    print('FAILED')")
                        print("A. PASSED")
                        print("B. FAILED")
                        print("C. 90")
                        print("D. Nothing")
                        answer = input("Your answer: ").upper()

                        if answer == "A":
                            print("Correct! 90 is greater than or equal to 75.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is A.")

                        print()
                        print("2. Which operator means NOT EQUAL TO?")
                        print("A. ==")
                        print("B. >=")
                        print("C. !=")
                        print("D. <=")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct! The != operator checks if two values are different.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")

                        print()
                        print("3. What will this program display?")
                        print("age = 16")
                        print("if age >= 18:")
                        print("    print('Adult')")
                        print("else:")
                        print("    print('Minor')")
                        print("A. Adult")
                        print("B. Minor")
                        print("C. 16")
                        print("D. Error")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! Since 16 is less than 18, the else block executes.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("4. Which statement is used to check another condition")
                        print("when the previous if condition is False?")
                        print("A. else")
                        print("B. elif")
                        print("C. print")
                        print("D. input")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! elif allows us to check another condition.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("5. What will this nested condition display?")
                        print("age = 20")
                        print("if age >= 18:")
                        print("    if age >= 21:")
                        print("        print('Qualified')")
                        print("    else:")
                        print("        print('Not Qualified')")
                        print("else:")
                        print("    print('Too Young')")
                        print("A. Qualified")
                        print("B. Not Qualified")
                        print("C. Too Young")
                        print("D. Error")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! Age is at least 18 but less than 21.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("=" * 40)
                        print("             GAME RESULTS")
                        print("=" * 40)
                        print("Your Score:", score, "/ 5")

                        if score == 5:
                            print("Excellent! You're a Decision-Making Master!")
                        elif score >= 3:
                            print("Good job! You understand conditional statements!")
                        else:
                            print("Keep practicing! Review Lesson 5 and try again.")

                        print("=" * 40)

                    elif ready == "NO":
                        print("You can play the challenge when you're ready!")
                    else:
                        print("Invalid Input")

                else:
                    print("Invalid Input")
                    exit()

            else:
                print("Invalid Input")
                exit()

        elif user1 == 6:
            print("=" * 40)
            print(" WHAT ARE LOGICAL OPERATORS?")
            print(" - Logical operators are used to combine or reverse conditions in a Python program. They are commonly used with if, elif, and else.")
            print("PYTHON HAS THREE LOGICAL OPERATORS:")
            print(" and - Both conditions must be True")
            print(" or  - At least one condition must be True")
            print(" not - Reverses the result")
            print()
            print(" THE and OPERATOR")
            print(" - The and operator returns True only when ALL conditions are True.")
            print("TRUTH TABLE - and")
            print("True | True  = True")
            print("True | False = False")
            print("False | True = False")
            print("False | False = False")

            next = input("\nType 'NEXT' to proceed: ").upper()

            if next == "NEXT":
                print("=" * 40)
                print(" THE or OPERATOR")
                print(" - The or operator returns True when at least ONE condition is True.")
                print("TRUTH TABLE - or")
                print("True | True  = True")
                print("True | False = True")
                print("False | True =True")
                print("False | False = False")
                print()
                print(" THE not OPERATOR")
                print(" - The not operator reverses the result of a condition.")
                print("TRUTH TABLE - not")
                print(" True -> False")
                print(" False -> True")

                print("\nLESSON 6 COMPLETED!")
                print("It's time to test your logical thinking!")
                print("\nMINI-GAME: LOGIC MASTER CHALLENGE!")
                print("There are 5 questions. Each correct answer is 1 point.")

                ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

                if ready == "YES":
                    print()
                    print("LET'S BEGIN THE CHALLENGE!")
                    print("=" * 40)
                    score = 0

                    print("1. What is the result of True and True?")
                    print("A. True")
                    print("B. False")
                    print("C. None")
                    print("D. Error")
                    answer = input("Your answer: ").upper()

                    if answer == "A":
                        print("Correct! Both conditions must be True.")
                        score += 1
                    else:
                        print("Incorrect! The correct answer is A.")

                    print()
                    print("2. What is the result of True or False?")
                    print("A. False")
                    print("B. True")
                    print("C. None")
                    print("D. Error")
                    answer = input("Your answer: ").upper()

                    if answer == "B":
                        print("Correct! The or operator returns True if at least one condition is True.")
                        score += 1
                    else:
                        print("Incorrect! The correct answer is B.")

                    print()
                    print("3. What is the result of not True?")
                    print("A. True")
                    print("B. False")
                    print("C. None")
                    print("D. Error")
                    answer = input("Your answer: ").upper()

                    if answer == "B":
                        print("Correct! The not operator reverses the result.")
                        score += 1
                    else:
                        print("Incorrect! The correct answer is B.")

                    print()
                    print("4. A student must pass BOTH subjects to qualify.")
                    print("Math = True")
                    print("English = False")
                    print("Which operator should be used?")
                    print("A. or")
                    print("B. not")
                    print("C. and")
                    print("D. if")
                    answer = input("Your answer: ").upper()

                    if answer == "C":
                        print("Correct! The and operator requires both conditions to be True.")
                        score += 1
                    else:
                        print("Incorrect! The correct answer is C.")

                    print()
                    print("5. What is the result of False or False?")
                    print("A. True")
                    print("B. False")
                    print("C. None")
                    print("D. Error")
                    answer = input("Your answer: ").upper()

                    if answer == "B":
                        print("Correct! The or operator returns False when both conditions are False.")
                        score += 1
                    else:
                        print("Incorrect! The correct answer is B.")

                    print()
                    print("=" * 40)
                    print("             GAME RESULTS")
                    print("=" * 40)
                    print("Your Score:", score, "/ 5")

                    if score == 5:
                        print("Excellent! You're a Logic Master!")
                    elif score >= 3:
                        print("Good job! You understand logical operators!")
                    else:
                        print("Keep practicing! Review Lesson 6 and try again.")

                    print("=" * 40)

                elif ready == "NO":
                    print("You can play the challenge when you're ready!")
                else:
                    print("Invalid Input")

            else:
                print("Invalid Input")
                exit()

        elif user1 == 7:
            print("=" * 40)
            print(" INTRODUCTION TO ITERATION")
            print(" - Iteration means repeating a process. In programming, it means repeatedly executing a set of instructions. Each repetition is called an iteration.")
            print()
            print("Iteration allows a program to perform the same task multiple times.")
            print("Without a loop, instructions must be written repeatedly:")
            print("WITHOUT LOOP:")
            print("print('Study Python')\nprint('Study Python')\nprint('Study Python')")
            print("USING A LOOP:")
            print("for number in range(4):\n   print('Study Python')")
            print("Both programs produce the same output, but the loop makes the program shorter and easier to modify. To repeat the message 100 times, change 4 to 100.")

            next = input("\nType 'NEXT' to proceed: ").upper()

            if next == "NEXT":
                print("=" * 40)
                print(" TYPES OF LOOPS IN PYTHON")
                print(" - Python has two main types of loops: for and while.")
                print()
                print(" for loop")
                print(" - Repeats instructions for each item in a sequence. Useful when the number of repetitions is known")
                print("for number in range(3):\n   print('Hello!')")
                print(" while loop")
                print(" - Repeats instructions while a condition is True. Useful when repetition depends on a condition.")
                print("count = 1\nwhile count is <= 3:\n   print('Hello!')\n   count += 1")
                print()
                print(" PYTHON for loop")
                print("SYNTAX")
                print("for variable in sequence:\n   statement(s)")
                print("EXAMPLE CODE")
                print("for number in range(4):\n   print('Study Python')")
                print()
                print(" for loop: PRINT NUMBER 1 TO 5")
                print("for number in range(1,6):\n   print(number)")
                print("OUTPUT:\n1\n2\n3\n4\n5")
                print()
                print(" COUNTING DOWNWARD WITH range(): 5 to 1")
                print("for number in range(5,0,-1):\n   print(number)")
                print("OUTPUT:\n5\n4\n3\n2\n1")

                next1 = input("\nType 'NEXT' to proceed: ").upper()

                if next1 == "NEXT":
                    print("=" * 40)
                    print(" PYTHON while loop")
                    print("SYNTAX")
                    print("while conditions:\n   statement(s)")
                    print("EXAMPLE CODE")
                    print("count = 1\nwhile count <= 1:\n   print(count)\n   count += 1")
                    print()
                    print(" COUNTING DOWNWARD WITH A while loop: 5 TO 1")
                    print("EXAMPLE CODE")
                    print("number = 5\nwhile number >= 1:\n   print(number)\n   number -= 1")
                    print("OUTPUT:\n5\n4\n3\n2\n1")
                    print()
                    print(" REPEATING A PROGRAM WITH while True")
                    print("while True:\n  name = input('Enter your name(X to exit): ')\n  if name.upper() == X:\n    print('Program stopped.')\n    break\n  print('Hello,', name)")
                    print(" SAMPLE OUTPUT")
                    print("Enter your name(X to exit): Ana\nHello, Ana\nEnter your name(X to exit): Mark\nHello, Mark\nEnter your name(X to exit): X\nProgram stopped.")

                    print("\nLESSON 7 COMPLETED!")
                    print("It's time to test your looping skills!")
                    print("\nMINI-GAME: LOOP MASTER CHALLENGE!")
                    print("There are 5 questions. Each correct answer is 1 point.")

                    ready = input("\nAre you ready for the challenge? (YES/NO): ").upper()

                    if ready == "YES":
                        print()
                        print("LET'S BEGIN THE CHALLENGE!")
                        print("=" * 40)
                        score = 0

                        print("1. What is iteration in programming?")
                        print("A. Making decisions")
                        print("B. Repeating a set of instructions")
                        print("C. Storing data")
                        print("D. Displaying output")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! Iteration means repeating instructions.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("2. Which loop is commonly used when the number of repetitions is already known?")
                        print("A. while loop")
                        print("B. if statement")
                        print("C. for loop")
                        print("D. else statement")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct! A for loop is useful for known repetitions.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")

                        print()
                        print("3. What numbers will this code display?")
                        print("for number in range(1, 4):")
                        print("    print(number)")
                        print("A. 1, 2, 3")
                        print("B. 1, 2, 3, 4")
                        print("C. 0, 1, 2, 3")
                        print("D. 2, 3, 4")
                        answer = input("Your answer: ").upper()

                        if answer == "A":
                            print("Correct! range(1, 4) produces 1, 2, and 3.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is A.")

                        print()
                        print("4. When does a while loop continue executing?")
                        print("A. When the condition is False")
                        print("B. When the condition is True")
                        print("C. Only once")
                        print("D. When the program has ended")
                        answer = input("Your answer: ").upper()

                        if answer == "B":
                            print("Correct! A while loop repeats while its condition is True.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is B.")

                        print()
                        print("5. What is the purpose of the break statement?")
                        print("A. To repeat the loop")
                        print("B. To skip an entire program")
                        print("C. To stop a loop")
                        print("D. To display a message")
                        answer = input("Your answer: ").upper()

                        if answer == "C":
                            print("Correct! The break statement immediately exits a loop.")
                            score += 1
                        else:
                            print("Incorrect! The correct answer is C.")

                        print()
                        print("=" * 40)
                        print("             GAME RESULTS")
                        print("=" * 40)
                        print("Your Score:", score, "/ 5")

                        if score == 5:
                            print("Excellent! You're a Loop Master!")
                        elif score >= 3:
                            print("Good job! You understand iteration and loops!")
                        else:
                            print("Keep practicing! Review Lesson 7 and try again.")

                        print("=" * 40)

                    elif ready == "NO":
                        print("You can play the challenge when you're ready!")
                    else:
                        print("Invalid Input")

                else:
                    print("Invalid Input")
                    exit()

            else:
                print("Invalid Input")
                exit()

        else:
            print("Invalid number input")
            exit()

        again = input("\nDo you want to choose another lesson?(YES/NO) ").upper()

        if again == "YES":
            continue
        elif again == "NO":
            print("\nThank you for using Python Tutorial Program! : )")
            break
        else:
            print("Invalid Input")
            break

elif user == "NO":
    print("\nThank you for visiting Python Tutorial Program! : )")
    exit()
else:
    print("\nInvalid Input")
    exit()
