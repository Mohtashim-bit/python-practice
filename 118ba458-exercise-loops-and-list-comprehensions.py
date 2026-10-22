"""Kaggle Python course - Exercise: Loops and List Comprehensions
Solutions only, cleaned up to run as a plain Python script.
"""


# 1. Fix the early-exit bug
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    # Only return False after checking every number
    return False


# 2. Element-wise comparison
def elementwise_greater_than(L, thresh):
    """Return a list the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    result = []
    for x in L:
        result.append(x > thresh)
    return result


# 3. Boring menu
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False


# 4. Monte Carlo estimate of slot machine payout
# NOTE: play_slot_machine() is provided by Kaggle's learntools and is not
# defined here. Define or import your own version before calling this.
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run
    (each play costs $1).
    """
    total = 0
    for _ in range(n_runs):
        total += play_slot_machine() - 1
    return total / n_runs


if __name__ == "__main__":
    assert has_lucky_number([1, 14, 3]) is True
    assert has_lucky_number([1, 2, 3]) is False
    assert elementwise_greater_than([1, 2, 3, 4], 2) == [False, False, True, True]
    assert menu_is_boring(["pizza", "pasta", "pasta"]) is True
    assert menu_is_boring(["pizza", "pasta", "pizza"]) is False
    print("All checks passed.")
