# from .a import A
# from .b import B

def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()