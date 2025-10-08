my_nums = [10, 50, 0, 5, 5, 100]
my_nums.append('123')  # [10, 50, 0, 5, 5, 100, '123']
my_nums.extend('123')  # [10, 50, 0, 5, 5, 100, '1', '2', '3']

print(my_nums)