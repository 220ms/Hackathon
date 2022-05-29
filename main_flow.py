



#Function Imports
import database
import gui

#### Functions

# function for processing the 3 main pieces that make up an image, colour, shape, and text.
def compare_image(filepath: str, text: str,  database):
    pass

# function for processing the input text.
def compare_text(text: str):
    pass

# button to show the results in a report format after image/text has been processed.
def display_results():
    pass

# run the backbone code here for keeping the interface on and root for all decisions made on interface
def main_flow():
    pass

# not sure if needed but exit the interface done by closing window.
def exit():
    pass

def string_to_lists(input_string: str) -> list:
    individual_lists = []
    output_list = []
    string_to_manipulate = input_string
    num_closed_bracket = string_to_manipulate.count("]")

    for closed_bracket in range(1,num_closed_bracket):
        if string_to_manipulate[0] == ',':
            string_to_manipulate = string_to_manipulate[1:]
        index_of_closed_bracket = string_to_manipulate.index(']') + 1
        aList = string_to_manipulate[0:index_of_closed_bracket].replace(" ", "")
        if aList[0] == '[' and aList[1] == '[':
            aList = aList[1:]
        individual_lists.append(aList)
        string_to_manipulate = string_to_manipulate[index_of_closed_bracket+1:]


    for string_list in individual_lists:
        inner_list = []
        string_numbers = string_list[1:-1]
        list_of_indiv_numbers = string_numbers.split(",")
        for number in list_of_indiv_numbers:
            inner_list.append(float(number))
        output_list.append(inner_list)

    return output_list


#### Main Program ####

#Check if the database needs to be indexed
if database.checkDatabaseIndexing() == False:
    #Index the database
    print("\n====\nNo indexed Database found\nPreprocessing Database\n====\n")
    database.indexDatabase()
    print("\n====\nIndexing Complete\n====\n")


# Have the user input the image/text
comparisonDetails = gui.getInput() #WIP - This is the function to get [isImage, text, image path]

# Get the database
database = database.read_database(database.databaseToSaveLocation)

# If the comparison is an image one, compare the images
if comparisonDetails[0] == True:
    compare_image()
    


