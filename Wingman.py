
# Dictionary of locations and things to say
location_dict = {"gym": ["gym pick_up line 1", "gym pick-up line 2", "gym pick-up line 3"], 
"grocery store": ["grocery store pick-up line 1", "grocery store pick-up line 2", "grocery store pick-up line 3"], 
"park": ["park pick-up line 1", "park pick-up line 2", "park pick-up line 3"], 
"bank": ["bank pick-up line 1", "bank pick_up line 2", "bank pick_up line 3"], 
"bar": ["bar pick_up line 1", "bar pick-up line 2", "bar pick-up line 3"], 
"party": ["party pick_up line 1", "party pick-up line 2", "party pick-up line 3"],
"unlisted": ["general pick_up line 1", "general pick-up line 2", "general pick-up line 3"]}

# Making list of locations for user to choose from
location_string = ""                                            # creates empty location string variable
for location, line in location_dict.items():                    # creates for loop to print locations
    location_string += "{0}\n".format(location)                     # creates line by line string of locations in location string variable


# greet user
def greet():                                                                                                            # greet function created
    print("We're in this together. These lines will work for the following locations:\n" + location_string)             # prints locations line by line to user

# get user's location and give pick-up line
def get_location():                                                                         # get_location function created
    location = input("Where ya at? Type in the corresponding location: ")                        # user inputs location 
    if location in location_dict:                                                                # checks if location is in location_dict
        pick_up_line_list = location_dict[location]                                                  # creates pick-up line list from location_dict
        counter = 0                                                                                  # creates counter for while loop
        while counter < len(pick_up_line_list):                                                      # while loop to go through pick-up line list
            for line in pick_up_line_list:                                                              # takes pick-up line from pick-up line list
                print(line)                                                                                 # prints pick-up line for user
                counter += 1                                                                                # increments while loop counter
                diff_line = input("Would you like a different line? Type 'yes' or 'no': ")                      # asks user if they want to see another pick-up line
                if diff_line == "no":                                                                       # checks if user does not want to see another pick-up line
                    return good_luck()                                                                          # returns good_luck function after user says they do not want to see another line
        print("That's all I have.")                                                                 # tells user that's all the pick-up lines available for location
        return good_luck()                                                                          # returns good_luck functions
    else:                                                                                       # if user gives location not in location_dict
        print("That wasn't one of the locations.")                                                  # tells user that wasn't a list location
        again = input("Would you like to see the location list again? Type 'yes' or 'no': ")        # asks user if they'd like to see location list again
        if again == "no":                                                                           # checks if user does not want to see location list again
            return good_luck()                                                                          # returns good_luck function
        else:                                                                                       # user wants to see list again
            print(location_string)                                                                      # prints location_string
            return get_location()                                                                       # recalls get_location function for user to try again                                     
                                                                                   

    
def good_luck():                                            # good_luck function created
    print("Good luck.  You got this.")                      # prints good luck message


def wingman():                                              # wingman function created
    greet()                                                 # calls greet function
    get_location()                                          # calls get_location function
    

wingman()                               # wingman function call




