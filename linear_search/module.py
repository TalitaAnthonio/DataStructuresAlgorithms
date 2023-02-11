'''Module for applying the linear search algorithm. 
Linear search: algorithm that finds a query by iterating through each element
of a list untill it is found. 
'''


def linear_search(python_list: list, query: int):
    '''Applies linear search algorithm: iterate through 
    the array and return the query if it matches the element in the query. 
    :param python_list: list with int or floats 
    :param query: int or float which represents the query. 
    :returns [query, index]: if query is in python_list it will return a list with the query as the first 
    element and the index as the second element. 
    found index. 
    :returns -1: if the query is not in the python_list, it will return -1. 
    '''

    for index in range(len(python_list)):
        if query == python_list[index]:
            print('the query {0} is in the list {1} '.format(query, index))
            return query, index
    return -1
