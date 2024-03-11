import time

# Defining the entire program
def program_project_4():
    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display the main menu
        print(
            """
            =====================================================
                      Choose an activity from the list:
            =====================================================
                         [1] - Problem Activity #1
                         [2] - Problem Activity #2
                         [3] - Problem Activity #3
                         [4] - Exit/Quit

            """
        )

        # Get the user choice
        choice = (input("                       Please enter your choice: "))

        print(
            """
            =====================================================
            """
        )

        # Check if the input is a number
        if choice.isdigit():
            choice = int(choice)

            # Problem Activity 1
            if choice == 1:
                print(
                    """
                      Welcome to problem activity #1
                    """
                    )
                # Input list of numbers separated by spaces
                nums = input("Enter elements of a list separated by spaces: ")
                # Extract integers from input
                int_extraction = [int(i) for i in nums.split() if i.isdigit()]
                # Find odd numbers
                odd_numbers = [x for x in int_extraction if x % 2 != 0]
                # Print results
                print(f'The user list is: {int_extraction}')
                print(f'The odd numbers list is: {odd_numbers}')

            # Problem Activity 2
            elif choice == 2:
                print(
                    """
                      Welcome to problem activity #2
                    """
                    )
                # Input list of numbers separated by commas
                nums = input("Please enter your numbers here separated by commas: ")
                # Extract integers from input
                nums_extraction = [int(i) for i in nums.split(",") if i.strip().isdigit()]
                # Check if at least two numbers are entered
                if len(nums_extraction) < 2:
                    print("Please enter at least two numbers.")
                    time.sleep(1.2)
                    continue
                # Find second smallest number
                min_num = min(nums_extraction)
                second_min = min(x for x in nums_extraction if x != min_num)
                # Print results
                print(f"The user list is: {nums_extraction}")
                print(f"The second smallest number is: {second_min}")

            # Problem Activity 3
            elif choice == 3:
                print(
                    """
                      Welcome to problem activity #3
                    """
                    )
                # Input list of numbers separated by commas
                nums = input("Please enter your numbers here separated by commas: ")
                # Extract integers from input
                nums_extraction = [int(i) for i in nums.split(",") if i.strip().isdigit()]
                # Check if at least two numbers are entered
                if len(nums_extraction) < 2:
                    print("Please enter at least two numbers.")
                    time.sleep(1.2)
                    continue
                # Find second largest number
                max_num = max(nums_extraction)
                second_max = max(x for x in nums_extraction if x != max_num)
                # Print results
                print(f"The user list is: {nums_extraction}")
                print(f"The second largest number is: {second_max}")

            # Exit program
            elif choice == 4:
                print(
                    """
                        You have exited the program\n
            =====================================================
                    """
                    )
                break

            # Invalid menu selection
            else:
                print("Invalid selection. Please enter a number between 1 and 4.")

        # Invalid user input
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

        # Delay for readability
        time.sleep(0.9)

# Program execution
program_project_4()