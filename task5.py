def non_negatives(nums):
    result=nums.copy()
    for number in list(result):      # копія списку
        if number < 0:
            result.remove(number)
    return result
print(non_negatives([-1, 5, 9, 8]))