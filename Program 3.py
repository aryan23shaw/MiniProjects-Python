def modify_list(lst):
    result = [x * 2 if x % 2 != 0 else x * 3 for x in lst]
    print("Modified list:", result)

lst = [1, 2, 3, 4, 5]
modify_list(lst)
