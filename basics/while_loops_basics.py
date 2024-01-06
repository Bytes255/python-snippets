from inspect import cleandoc
# You can also import this module like this
# import inspect
# inspect.cleandoc("""
#   your indented text
#   goes here
# """)

# This variables must be outside the loop
# otherwise the loop will never end
# since the variable session_end will be set false in every cycle
# same happens with car_has_started
session_end = False
car_is_moving = False

while not session_end:
    command = input("> ").upper()
    if "HELP" == command:
        # You can always read variables outside the loop
        # Just remember to change it's value wisely
        if car_is_moving: 
            car_status = "running"
            
        else: 
            car_status = "stopped"
        
        # triple quotes for printing multiple lines
        # without triple quotes print("you can only print one line")
        # cleandoc() according to python 3 documentation is used to
        # clean up indentation from docstrings that
        # are indented to line up with blocks of code.
        # without this function the print could be different
        print(cleandoc(f"""Available commands:
            start - to start the car
            stop - to stop the car
            quit - to exit
            
            the car is actually {car_status}"""))

        # Try it yourself
        # print(f"""Available commands:
        #     start - to start the car
        #     stop - to stop the car
        #     quit - to exit
        #     
        #     the car is actually {car_status}""")
        
        
    elif "START" == command:
        if car_is_moving:
            print("The car is already moving...")
            
        else:
            print("Car started!")
            car_is_moving = True
            
    elif "STOP" == command:
        if car_is_moving:
            print("The car has stopped!")
            car_is_moving = False
            
        else:
            print("The car is already stopped...")
            
    elif "QUIT" == command:
        print("Exiting...")
        session_end = True 
    else:
        print(cleandoc("""You've inserted an unknown command!
                    Write 'help' to see the available commands"""))

# Do if the while loop condition is false       
else:
    print("Exited succesfully")