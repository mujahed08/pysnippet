"""
Main
"""

print('Hello World!')


def min_from_array(arr:list):
    min_idx:int = 0
    for i in range(len(arr) - 1) :
        for j in range(i + 1, len(arr)):
            print(str(arr[i]) + ", " + str(arr[j]))
            if arr[min_idx] > arr[j]:
                min_idx = j
    print('Min element in an array is ' + str(arr[min_idx]))



min_from_array([2,3,5,6,4,-3])

def max_from_array(arr:list):
    max_idx:int = 0
    for i in range(len(arr) - 1) :
        for j in range(i + 1, len(arr)):
            print(str(arr[i]) + ", " + str(arr[j]))
            if arr[max_idx] < arr[j]:
                max_idx = j
    print('Max element in an array is ' + str(arr[max_idx]))

max_from_array([2,3,5,6,4,-3])