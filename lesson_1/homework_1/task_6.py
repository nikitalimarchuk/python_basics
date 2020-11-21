numbers = input("Enter first and desired distance separated with space: ")
numbers = [int(number) for number in numbers.split(" ")]
first_distance, desired_distance = numbers
day_counter = 0
visualize_iterations = False

while first_distance < desired_distance:
    day_counter += 1
    first_distance += first_distance * 0.1
    if visualize_iterations:
        print(f"{day_counter} day: {first_distance}")

if visualize_iterations:
    output_message = (
        f"On {day_counter} day sportsmen reached result "
        f"- desired distance not less then {desired_distance}"
    )
else:
    output_message = day_counter

print(output_message)
