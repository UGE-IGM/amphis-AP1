from turtle import forward, left

nb_cotes = 6
lg_cote = 50
angle_poly = 360 / nb_cotes

nb_petales = 12
angle_rosace = 360 / nb_petales

i = 0
while i < nb_petales:
    j = 0
    while j < nb_cotes:
        forward(lg_cote)
        left(angle_poly)
        j += 1
    left(angle_rosace)
    i += 1
