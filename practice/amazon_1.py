"""
You are given an array of positive numbers from 1 to n,
such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted.
Look at the below array and give it a try before checking the solution.
"""


def find_number(array):
    # # sort
    # array.sort()
    #
    # for i in range(1, len(array)):
    #     if array[i]-array[i-1] > 1:
    #         return array[i-1]+1
    #
    # return -1

    # 다른 풀이
    sum_of_array = sum(array)

    n = len(array)+1
    total_sum = (n+1)*n/2

    return total_sum-sum_of_array

print(find_number([6,4,9,7,5,1,3,2]))