"""
Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .
Example

-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:
-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :
0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.
Function Description
Complete the function hourglassSum in the editor below.
hourglassSum has the following parameter(s):
int arr[6][6]: an array of integers
Returns
int: the maximum hourglass sum
Input Format
Each of the  lines of inputs  contains  space-separated integers .
Constraints


Output Format
Print the largest (maximum) hourglass sum found in .
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19
Explanation
 contains the following hourglasses:
image
The hourglass with the maximum sum () is:
2 4 4
  2
1 2 4
"""

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hour_glass_sum(arr):
    sum_array = []
    for i, array_one in enumerate(arr):
        if i == 4:
            break
        for j, elem in enumerate(array_one):
            if j == 4:
                break
            print(i, j, elem)
            t = [x for elem in arr[i:i + 3] for x in elem[j:j + 3]]
            sum_num, index = 0, 0
            ## VERY VERY IMPORTANT
            ## Index for a flattend list is kept as-is
            for elem in t:
                print(index)
                if index != 3 and index != 5:
                    sum_num += elem
                index += 1
            sum_array.append(sum_num)
    print(max(sum_array))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6]]
    result = hour_glass_sum(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
