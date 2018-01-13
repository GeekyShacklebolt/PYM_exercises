"myfact module"

def factorial(num):
    '''
    Returns the factorial of a number.
    
    :arg num: Integer given to the function to calculate its factorial.
    
    :return: The value of the factorial or -1 if -ve value is provided.
    '''
    
    if num >= 0:
        if num == 0:
            return 1
        return num * factorial(num - 1)
    else:
        return -1
