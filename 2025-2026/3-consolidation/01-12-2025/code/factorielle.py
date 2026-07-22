def factorielle(n):
    print(n)
    # Attention à ne pas oublier le cas de base !
    if n == 0:
        return 1
    else:
    ### Attention à appeler avec un paramètre plus simple !
        return n * factorielle(n-1)
    

print(factorielle(5))

# factorielle(5) =
#     5 * factorielle (4) =
#         5 * 4 * factorielle(3) =
#         5 * 4 * 3 * factorielle(2) =
#         5 * 4 * 3 * 2 * factorielle(1) =
#         5 * 4 * 3 * 2 * 1 * factorielle(0) =
#         5 * 4 * 3 * 2 * 1 * 1 = 120