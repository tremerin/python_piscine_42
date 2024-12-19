import sys

def is_punctuation(char:str):
    """
    Checks if the character is a punctuation mark and return True
    """
    punctuations_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if char in punctuations_chars:
        return True
    return False

def character_counter(string:str):
    """
    Analyzes the type of characteres and print them 
    """
    upper_letters:int = 0
    lower_letters:int = 0
    punctuation_marks:int = 0
    spaces:int = 0
    digits:int = 0
    characters:int = len(string)
    for element in string:
        if element.isupper(): upper_letters += 1
        elif element.islower(): lower_letters += 1
        elif element.isspace(): spaces += 1
        elif element.isnumeric(): digits += 1
        elif is_punctuation(element): punctuation_marks += 1 

    print(f"The text contain {characters} characters:")
    print(f"{upper_letters} upper_letters")
    print(f"{lower_letters} lower_letters")
    print(f"{punctuation_marks} punctuacion_marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    
def main():
    """
    Receives a text as an argument or waits for input and parses and prints the character type
    """
    if len(sys.argv) == 1:
        print("What is the text to count?")
        argument = input()
        character_counter(argument)
    elif len(sys.argv) == 2:
        character_counter(sys.argv[1])
    else:
        print("AssertionError: too many arguments")
    

if __name__ == "__main__":
    main()