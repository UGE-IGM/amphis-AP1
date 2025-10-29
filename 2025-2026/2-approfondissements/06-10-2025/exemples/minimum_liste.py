def minimum(lst: int list) -> int:
    m = lst[0]
    for elt in lst:
        if elt < m:
            m = elt
    return m


# # ma_liste_2 = [1, 2, 3]
# ma_liste = [3, 2, 7, 8, 2, 3, 10, 7, 10, 7, 5, 4, 1, 8, 9, 1, 3]    
print(minimum(3))


# def minimum(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# print(minimum(1,2))