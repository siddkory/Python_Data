"""

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
Example


Queries are interpreted as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.
Function Description
Complete the function arrayManipulation in the editor below.
arrayManipulation has the following parameters:
int n - the number of elements in the array
int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Returns
int - the maximum value in the resultant array
Input Format
The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.
Constraints




Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
Explanation
After the first update the list is 100 100 0 0 0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.
The maximum value is .
"""


# Complete the arrayManipulation function below.
def array_manipulation(n, queries):
    arr = [0] * n
    len_arr = len(queries)
    print('len_arr', len_arr, '  n: ', n)
    common_range = [0,n-1]
    # find the common index
    for i in range(0, len_arr):
        first_num = queries[i][0] - 1
        second_num = queries[i][1]
        if first_num > common_range[0]:
            common_range[0] = first_num
        if second_num < common_range[1]:
            common_range[1] = second_num
        if common_range[0] >= common_range[1]:
            common_range = []
            break

    print(common_range)
    if len(common_range) > 0:
        sum_n = 0
        for i in range(0, len_arr):
            sum_n += queries[i][2]
        return sum_n

    for i in range(0, len_arr):
        start, end, incr = queries[i]
        for j in range(start - 1, end):
            arr[j] = arr[j] + incr
    print(arr)
    return max(arr)


if __name__ == '__main__':
    #fptr = open('/tmp/input09.txt', 'w')
    queries_ = []
    num = 0
    with open('/Users/ukorysi/tmp/input09.txt', 'r') as f:
        first_line_read = False
        for line in f:
            #sprint(line)
            if not first_line_read:
                num, m = line.split()
                first_line_read = True
                num, m = int(num), int(m)
            else:
                queries_.append(list(map(int, line.split())))

        # num = 10
        # queries_ = [[1, 5, 3], [4, 8, 7], [5, 9, 1], [4, 5, 9]]
        # 2501448788
        result = array_manipulation(num, queries_)
        print(result)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
