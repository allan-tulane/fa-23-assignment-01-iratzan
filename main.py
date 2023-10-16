"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        first = foo(x - 1)
        second = foo(x - 2)
        return first + second

def longest_run(mylist, key):
    longest_length = 0  # Set longest and current length values to 0
    current_length = 0  
    
    for item in mylist:
        if item == key:
            current_length += 1 #adds the increase in length to current length
        else:
            current_length = 0  # Resets the run length if the key is wrong
        
        # updates the longest length if current is >
        if current_length > longest_length:
            longest_length = current_length
    
    return longest_length


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(myarray, key):
    def divide_and_conquer(left_size, right_size):
        if left_size == right_size:
            return Result(1 if myarray[left_size] == key else 0, 1)

        mid = (left_size + right_size) // 2

        left_result = divide_and_conquer(left_size, mid)
        right_result = divide_and_conquer(mid + 1, right_size)

        current_run = 0

        if myarray[mid] == key:
            current_run = left_result.current_run + right_result.current_run

        longest_size = max(left_result.longest_run, right_result.longest_run, current_run)

        return Result(longest_run, current_run)

    result = divide_and_conquer(0, len(myarray) - 1)
    return result.longest_run

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


