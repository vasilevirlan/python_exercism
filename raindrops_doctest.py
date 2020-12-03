def convert(number):
    """Your task is to convert a number (integer) into a string that contains
        raindrops sound coresponding to certain otential factors. A factor is 
        a number that evenly divides into another number, leaving no remainder
        The simplest way to test if one number is a factor to another is to use
        modulo operation.
        The rules of raindrops are that if a givennumber:
        - has 3 as factor, add 'Pling' to the result.
        - has 5 as factor, add 'Plang' to the result.
        - has 7 as factor, add 'Plong' to the result.
        - does not have any of these as factor, the result should be the string
        number. Examples see bellow.
    >>> convert(3)
    'Pling'
    >>> convert(5)
    'Plang'
    >>> convert(7)
    'Plong'
    >>> convert(17)
    '17'
    >>> convert (15)
    'PlingPlang'
    >>> convert(21)
    'PlingPlong'
    >>> convert(105)
    'PlingPlangPlong'
    """
    result = ''
    if number % 3 == 0: result += 'Pling' # Against PEP8, but less lines :)
    if number % 5 == 0: result += 'Plang'
    if number % 7 == 0: result += 'Plong'
    if result == '': result = str(number) # change this with 
    return result                         # return result or str(number)

if __name__ =='__main__':
    import doctest
    doctest.testmod()
