weight = int(input("Enter your weight in Kg: "))
height_cm = int(input("Enter your height in Cm: "))
height_ft = height_cm/30.48 # converts cm to feet
height_fts= int(height_ft) # split foots into whole number(Eg 5.64 = 5 ft)
height_in = (height_ft-height_fts)*12 # foots to inches
height = height_fts * 0.3048 + height_in * 0.0254

bmi = weight / height ** 2

print(round(bmi,1))