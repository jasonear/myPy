a = 1
print(id(a),id(1))

def fun(a):
    print(id(a))
    a = 2
    print(id(a),id(2))

fun(a)

print(id(a))
print(a)