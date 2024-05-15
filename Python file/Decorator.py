import functools

def welcome_decorator(func):
    @functools.wraps(func)
    def wrapper_fun(*arg,**kwarg):
        print("Before")
        func(*arg,**kwarg)
        print("After")
        return
    return wrapper_fun


@welcome_decorator
def hello(name,rollno):
    print("Hello .... ", name, rollno)

hello("Piyush",37)

l=[1,5,4,8,2,10,-3]

print(sorted(l, key=lambda x: x))# ascending order
print(sorted(l, key=lambda x: -x))# descending order