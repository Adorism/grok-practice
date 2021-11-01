# Given an array of positive numbers and a positive number 'K', find the maximum sum of any contiguous subarray of size 'K'.

def max_sub_array_of_size_k(array, k):
    if k > len(array):
        return -1
    max_sum = 0
    for i in range(len(array) - k + 1):
        sub_array = array[i:i+k]
        max_sum = max(max_sum, sum(sub_array))
    return max_sum

# OR


def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Time Complexity: O(N*K

# OR


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()

# OR


def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
# this is O(N) time and O(1) space
