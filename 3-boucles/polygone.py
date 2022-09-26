from turtle import forward, left

nb_cotes = 6
lg_cote = 50
angle_poly = 360 / nb_cotes

i = 0
while i < nb_cotes:
    forward(lg_cote)
    left(angle_poly)
    i += 1
