#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter another adjective: ")
  meat1 = input("Enter a type of meat: ")
  room1 = input("Enter name of a room: ")
  verb1 = input("Enter a verb in past tense: ")
  verb2 = input("Enter a verb: ")

  #Print the story with the user supplied words.
  print(" It was a " + adjective1+ ", cold November day. I woke up to the " + adjective2 + " smell of " + meat1+ " roasting in the " + room1+ " downstairs. I " + verb1+ " down the stairs to see if I could help " + verb2+ " the dinner")




#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
