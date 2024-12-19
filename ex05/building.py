import sys

def character_counter(string:str):
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

    print(f"The text contain {characters} characters:")
    print(f"{upper_letters} upper_letters")
    print(f"{lower_letters} lower_letters")
    print(f"{punctuation_marks} punctuacion_marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    
def main():
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