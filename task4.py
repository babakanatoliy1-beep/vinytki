def min_pair(nums):
    min_sum = nums[0] + nums[1]#Потрібна сума, а не добуток, Не можна називати змінну min — це вбудована функція

    for i in range(len(nums) - 1):#Починати потрібно з 0, а не з 2, Так пропускаються перші пари
        min_sum = min(nums[i] + nums[i + 1], min_sum)#При i = len(nums)-1 буде вихід за межі списку, Тут використовується перевизначена функція min

    return min_sum