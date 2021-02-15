"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
Function Description
Complete the function rotLeft in the editor below.
rotLeft has the following parameter(s):
int a[n]: the array to rotate
int d: the number of rotations
Returns
int a'[n]: the rotated array
Input Format
The first line contains two space-separated integers  and , the size of  and the number of left rotations.
The second line contains  space-separated integers, each an .
Constraints



Sample Input
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
Explanation
When we perform  left rotations, the array undergoes the following sequence of changes:


"""
import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]


def rot_left(a, d):
    i = 0
    reverse = False
    if len(a) - d < round(len(a) / 2) and len(a) > d:
        reverse = True
        a = a[::-1]
        d = len(a) - d
    d = d if len(a) > d else len(a) % d
    while i < d:
        temp = a[0]
        for index, elem in enumerate(a):
            a[index] = a[index + 1]
            if index == len(a) - 2:
                break
        a[len(a) - 1] = temp
        i += 1
    if reverse:
        a = a[::-1]
    return a


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()
    #
    # n = int(nd[0])
    #
    # d = int(nd[1])
    #
    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    d = 10
    result = rotLeft(a, d)
    print(result)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    d = 10
    result = rot_left(a, d)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
