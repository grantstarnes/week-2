import numpy as np


# update/add code below ...

def ways(n):           # The provided ways function that takes n, the total amount of cents
   
   return (n // 5) + 1 # This return statement first takes into account the number of nickels (5 cents) 
                       # that could possibly fit into n (total cents) 
                       # and then adds 1 to account for the singular case in which n is less than 5 
                       # (i.e., when there are no nickels) and uses only pennies (1 cent).

                       # While observing the above test cases, I realized there is exactly one instance 
                       # in each test case that uses only pennies, which is why we add 1 to the final result,
                       # making the solution far easier to compute.

def lowest_score(names, scores):                 # The provided lowest_score function that takes in two arrays: names and scores
    min_score = np.argmin(scores)                # This line uses the numpy function argmin to find the index of the minimum value in the scores array.
    return names[min_score]                      # This line returns the name corresponding to the index of the lowest score found in the previous line.

def sort_names(names, scores):                   # The provided sort_names function that takes in two arrays: names and scores
    high_to_low = np.argsort(scores)[::-1]       # This line uses the numpy function argsort to get the indices that would sort the scores array in ascending order.
                                                 # The [::-1] slice then reverses this array of indices to arrange them in descending order.
    return names[high_to_low].tolist()           # This line returns the names array rearranged according to the indices in high_to_low, effectively sorting the 
                                                 # names based on their corresponding scores from highest to lowest.