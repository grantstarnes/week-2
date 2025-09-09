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

def sort_names(names, scores):                             # The provided sort_names function that takes in two arrays: names and scores
    high_to_low = np.argsort(scores)[::-1]                 # This line uses the numpy function argsort to get the indices that would sort the scores array in ascending order.
                                                           # The [::-1] slice then reverses this array of indices to arrange them in descending order.
    sorted_names = names[high_to_low].tolist()             # This line uses the sorted indices to reorder the names array accordingly and converts it to a list.
    sorted_scores = scores[high_to_low].tolist()           # This line does the same for the scores array.
    name_grade = list(zip(sorted_names, sorted_scores))    # This line combines the sorted names and scores into a list of tuples, where each tuple contains a name and its corresponding score.
    return name_grade                                      # Finally, this line returns the list of tuples containing names and their corresponding scores sorted from highest to lowest score.