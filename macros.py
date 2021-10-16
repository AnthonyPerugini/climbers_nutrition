weight = int(input('Weight: '))

#TODO: catch bad inputs
boulder_alpinist_scale = float(input('from only bouldering (0) to only alpinist climbing (1), I want to optimize for: '))

PROTEIN_RATIO = .15
protein_scaling = (0.3 * (-1 * (boulder_alpinist_scale - 1)) + 1.2)
print(f'{protein_scaling=:.5f}')

fat_scaling = (0.15 * boulder_alpinist_scale) + 0.15

print(f'{fat_scaling=:.5f}')

carb_scaling = (0.15 * (-1 * (boulder_alpinist_scale - 1))) + 0.55


print(f'{carb_scaling=:.5f}')


protein_intake = weight * protein_scaling
total_intake = protein_intake / PROTEIN_RATIO 

fat_intake = total_intake * fat_scaling
carb_intake = total_intake * carb_scaling

print(f'{fat_intake=:.5f}')
print(f'{protein_intake=:.5f}')
print(f'{carb_intake=:.5f}')
print(f'{total_intake=:.5f}')

#TODO: make better
cal = 0
cal += protein_intake * 4
cal += carb_intake * 4
cal += fat_intake * 9

print(cal)



