from time import strftime, gmtime


day_time_limit = 86400
time = 0
seconds_in_hour = 3600
seconds_in_minute = 60

while time == 0 or time > 86400:
    time = int(input("Enter time in seconds: "))

minutes_in_seconds = (time % seconds_in_hour)
hours = time // seconds_in_hour
minutes = minutes_in_seconds // seconds_in_minute
seconds = minutes_in_seconds % seconds_in_minute

def get_time(value: int) -> str:
    time_string = str(value)
    return time_string if len(time_string) > 1 else f"0{time_string}"

own_solution = f"{get_time(hours)} : {get_time(minutes)} : {get_time(seconds)}"
built_in_solution = strftime("%H : %M : %S", gmtime(time))

print(own_solution)
print(built_in_solution)
