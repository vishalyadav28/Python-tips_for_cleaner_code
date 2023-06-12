# Tips :4 


# Here the data is taking the multiple input at once
def some_func(*data: int) -> int:
    # by print it we can see that it's nothing just a tuple of values
    print(data)
    # sum() in built which will add all and return
    return sum(data)

print(some_func(1,2,3,4))



# for example our print statement tooks multiple input like 

# print("do_something", 1, 2)
