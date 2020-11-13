elements = [1, 1.0, True, None, {}, [], (), "string"]

for element in elements:
    print(
        f"Is '{element}' has type {type(element)}: "
        f"{isinstance(element, type(element))}"
    )
