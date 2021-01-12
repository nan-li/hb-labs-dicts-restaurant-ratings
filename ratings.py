"""Restaurant rating lister."""

# Create a function that takes in restaurant names and scores
# Prints them out
def restaurant_ratings(filename):
    """Create a function that takes in restaurant names and scores
    Outputs a sorted list.
    """
# open file
    scores = open(filename)
    restaurantnames_and_scores = {}
    for line in scores:
        restaurant_info = line.rstrip().split(":")
# unpack the list made with restaurant_info        
        restaurant_name, score = restaurant_info
# define dict = {'Ministry Munchies': 1, 'The Porcupine': 5}        
        restaurantnames_and_scores[restaurant_name] = score
# alphabetize the list        
    sorted_list = sorted(restaurantnames_and_scores)
# for i in keysortedlist    
# reference the dict pair
    for restaurant_name in sorted_list:
        print(f'{restaurant_name} is rated at {restaurantnames_and_scores[restaurant_name]}.')

        

restaurant_ratings("scores.txt")
