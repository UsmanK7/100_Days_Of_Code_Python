# namespace- anything that you declare it and give it a name is called namespace for example variable functions etc.
# Global scope-This variable can be used anywhere and also inside the function
local_variable=2

# Local scope-This variable can be used only in the function

def fun():
    global_variable=4

    print(local_variable)
    print(global_variable)

fun()

# The line 16 will give a NameError: because its scope is only limited inside function
# print(global_variable)

# same goes for functions

def fun():
    def fun2():
        return 1
    return fun2()
    

print(fun())
# now with line 28 we cannot call fun2() because it has local scope so we have to call it inside fun()
# fun2()
