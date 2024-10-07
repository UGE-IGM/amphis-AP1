def minimum(lst):
    m = lst[0]
    for elt in lst:
        if elt < m:
            m = elt
    return m

    
print(minimum([5, 3, 7, 7, 8, 2, 3, 10, 7, 10, 7, 5, 4, 1, 8, 9, 1, 3]))


# def minimum(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# print(minimum(1,2))