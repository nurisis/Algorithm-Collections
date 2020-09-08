"""
Given an array of integers and a value,
determine if there are any two integers in the array whose sum is equal to the given value.
Return true if the sum exists and return false if it does not.
Consider this array and the target sums:
"""


def find_sum_of_two(A, val):
    # for i in range(len(A)):
    #     for j in A[i+1:]:
    #         if A[i] + j == val:
    #             return True
    #
    # return False

    # 다른 풀이(정답)
    found_values = set()

    for num in A:
        if (val - num) in found_values:
            return True

        found_values.add(num)

    return False


print(find_sum_of_two([5,7,1,2,8,4,3], 10))