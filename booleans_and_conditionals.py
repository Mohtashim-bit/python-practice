# Kaggle Python course - Exercise: Booleans and Conditionals
# My solutions for questions 1-6.


# 1. sign: return -1 if negative, 1 if positive, 0 if zero
def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


# 2. to_smash with correct grammar for one candy
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    if total_candies < 2:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3


# 3. Weather bug: inputs where prepared_for_weather gives the wrong answer
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Buggy on purpose. The goal was to find the bug, not fix it.
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday


# Not raining and not a workday, so we are fine, but the function returns False.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False


# 4. One-line version of is_negative
def is_negative(number):
    if number < 0:
        return True
    else:
        return False


def concise_is_negative(number):
    return number < 0


# 5a. Wants all three toppings
def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion


# 5b. Wants a plain hot dog
def wants_plain_hotdog(ketchup, mustard, onion):
    return not ketchup and not mustard and not onion


# 5c. Exactly one sauce (exclusive or)
def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)


# 6. Exactly one topping (True counts as 1, False counts as 0)
def exactly_one_topping(ketchup, mustard, onion):
    return (ketchup + mustard + onion) == 1


if __name__ == "__main__":
    print(sign(-7), sign(12), sign(0))
    to_smash(91)
    to_smash(1)
    print(prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday))
    print(concise_is_negative(-5), concise_is_negative(5))
    print(exactly_one_sauce(True, False, True), exactly_one_sauce(True, True, True))
    print(exactly_one_topping(True, False, False), exactly_one_topping(True, True, False))
