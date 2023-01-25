#create a swapping technique for the start and end
def swap():
    temp = 1



#create a partition function to make the pivot in the middle
def partition(nums):
    pivot_index = 0
    pivot = nums[pivot_index]

    #Create a start and end locator
    start = pivot_index + 1
    end = len(nums) - 1

#create a quick sort function
def quick_sort(nums):
    partition(nums)



nums = [70, 1, 32, 61, 11, 8, 3, 53, 69, 14]
quick_sort(nums)
print(nums)