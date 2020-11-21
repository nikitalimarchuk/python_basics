john = {"first_name": "John", "last_name": "Smith", "age": 20, "salary": 1000}
james = {"first_name": "James", "last_name": "Smith", "age": 30, "salary": 2000}
amanda = {"first_name": "Amanda", "last_name": "Smith", "age": 30, "salary": 34000}
marta = {"first_name": "Marta", "last_name": "Stuard", "age": 70, "salary": 100000}
bob = {"first_name": "Robert", "last_name": "Mc'Donald", "age": 10, "salary": 100}
bill = {"first_name": "Bill", "last_name": "Mc'Taller", "age": 40, "salary": 11000}
users = [john, james, amanda, marta, bob, bill]


def get_user_info(first_name: str, last_name:str, age: int, salary: int) -> str:
    return (
        f"{f'{first_name} {last_name}:'.ljust(20)} "
        f"{age} years, ${salary} salary"
    )

if __name__ == '__main__':
    for user in users:
        print(get_user_info(**user))