# Restaurant Recommendation System

# Set of user's preferred foods
food_preference = {"burger", "pizza", "ice cream"}

# Dictionary of restaurants and their menus (sets)
restraunts = {
    "seafood_cove": {"fish", "crab"},
    "hungry_jacks": {"burger", "pizza"},
    "potting_shed": {"brocalli", "carrot"}
}

# Initialize best match variables
best_match_foods = set()      # Empty set to track best matched foods
best_match_restraunt = None   # No restaurant selected yet

# Loop through each restaurant
for restraunt_name, menu in restraunts.items():

    # Find common foods using set intersection
    common_foods = food_preference.intersection(menu)

    # Compare length of current match with best match so far
    if len(common_foods) > len(best_match_foods):
        best_match_foods = common_foods
        best_match_restraunt = restraunt_name

# Print final result
print(f"The best match is {best_match_restraunt} with {best_match_foods} matched foods.")