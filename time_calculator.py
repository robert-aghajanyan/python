min = 60
hour = 3600
day = 86400

user_input = int(input("Please enter the number of seconds: "))

if user_input >= day:
    user_day = user_input // day
    user_hour = (user_input % day) // hour
    user_min = (user_input - user_day*day - user_hour*hour) // min
    user_sec = user_input - user_day*day - user_hour*hour - user_min*min
    result = f"There are {user_day} day(s), {user_hour} hour(s), {user_min} min and {user_sec} sec."
    print(result)
elif user_input >= hour:
    user_hour = user_input // hour
    user_min = (user_input - user_hour*hour) // min
    user_sec = user_input-user_hour*hour - user_min*min
    result = f'There are {user_hour} hour(s), {user_min} min and {user_sec} sec.'
    print(result)
elif user_input >= min:
    user_min = user_input // min
    user_sec = user_input - user_min*min
    result = f'There are {user_min} min and {user_sec} sec.'
    print(result)
else:
    result = f"There are {user_input} sec."
    print(result)
