import time

user_name = input("What is your name?: ")
time.sleep(1.5)
favorite_animal = input("What is your favorite animal?: ")
time.sleep(1.5)
print(f"Hello! {user_name}, your favorite animal is a {favorite_animal}")
time.sleep(1.5)
user_age = input("How old are you?: ")
future_user_age = int(user_age) + 10
time.sleep(1.5)
print(f"In 10 years you will be {future_user_age}")