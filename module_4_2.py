def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return
test_function()
#inner_function() Мы не можем вызвать эту функцию, так как она находится в другой области видимости