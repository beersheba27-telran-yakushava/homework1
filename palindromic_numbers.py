def int_reverse(num):
    """
    returns string containing digits  of integer number "num" in reversed order
    if "num" contains only one digit it will return the same digit but as a string
    examples: int_reverse(10) -> "01"; int_reverse(1) -> "1";int_reverse(702) -> "207"
    """
    #TODO
    return str(num)[::-1]
def create_palindromic_list(start, stop) :
    """
    start, stop are integer numbers
    returns list containing all palindromic numbers in the range from "start" to "stop" 
    note: "start" may be less than "stop"
    requirement: to use "int_reverse" function
    """  
    #TODO
    numbers = []

    if start < stop:
        numbers = range(start, stop+1)
    else:
        numbers = range(start, stop-1, -1)

    return list(filter(lambda x: x % 11 == 0, numbers))

print(create_palindromic_list(20, 40)) #should print   [22, 33] 
print(create_palindromic_list(40, 20)) #should print   [33, 22] 
