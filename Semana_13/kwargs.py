def my_function(first_parameter, *args, **kwargs):
    print(f"First parameter: {first_parameter}")
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"Kwargs: {kwargs}")


my_function("First value", 1, 2, 3, 4, my_other_parameter="World", whatever=6)