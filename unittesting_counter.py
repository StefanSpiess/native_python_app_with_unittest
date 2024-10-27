'''Module Counter'''

def count_letters(string: str):
    '''Returns the number of letters in a string.
    Does not count spaces or signs.'''

    if string in ("", None, isinstance(string,bool)):
        raise TypeError("You must give me something to get something.")

    #Initialize a reference for the "stripped_string"
    #Strip all whitespace from the stripped_string
    stripped_string = string.replace(" ", "")

    #Make sure the function only counts alphabetical strings
    if not stripped_string.isalpha():
        raise TypeError("The string you entered was not purely alphabetical.")

    return len(stripped_string)
