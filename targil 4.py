name= (input("enter name:"))
age= int(input("enter age:"))
year_today= int(input("enter year today: "))
futhur_year= int(input("futur year: "))
futhur_age= futhur_year - year_today + age
print(f"{name} will be {futhur_age} in year {futhur_year}")