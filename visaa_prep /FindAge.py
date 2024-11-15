def vignesh_age_when_charan_was_x(charan_current_age, vignesh_current_age, x):
    age_difference = charan_current_age - vignesh_current_age
    return max(0, x - age_difference)

charan_current_age = 25
vignesh_current_age = 10

x = int(input())

vignesh_age = vignesh_age_when_charan_was_x(charan_current_age, vignesh_current_age, x)

print(vignesh_age)
