def decorator(function):
    def func():
        print("After")
        function()
        print("Before")
        
@decorator
def suma():
    print(2+3)

suma()    