'''
DIRECTIONS
==========

1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    [ "Sally", [ "lollipop", "bubble gum", "laffy taffy" ]],
    [ "Bob", [ "milky way", "licorice", "lollipop" ]],
	[ "Arlene", [ "chocolate bar", "milky way", "laffy taffy" ]],
	[ "Carlie", [ "nerds", "sour patch kids", "laffy taffy" ]]
]
2. In `get_friends_who_like_specific_candy()`, return friends who like lollipops.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''


def create_new_candy_data_structure(data):
    # Create dict where key is the type of candy and value is a list of people who like the candy
    # Example: 
    # favorites_by_candy = {
    #   "lollipop": ["Sally", "Bob"],
    #   " laffy taffy": ["Sally", "Arlene", Carlie]
    # }
    # 1. Create empty dict - this will be returned
    favorites_by_candy = {}
    # Need a for loop to access elements inside friend_favorites
    for friend in data:
        for candy in friend[1]:
            if candy not in favorites_by_candy:
                favorites_by_candy[candy] = [friend[0]]
            else:
                favorites_by_candy[candy].append(friend[0])
    return favorites_by_candy


def get_friends_who_like_specific_candy(data, candy_name):
    # Expected Output: ["Sally", "Bob"] - returning a list of folks who like lollipops
    candy_dictionary = create_new_candy_data_structure(data)
    return candy_dictionary[candy_name]



def create_candy_set(data):
    set(data)