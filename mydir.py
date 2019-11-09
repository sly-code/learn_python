"""mydir.py: a module that lists the namespace of other modules"""
seplen = 30
sepchr = '- '


def listing(mod, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print("name:", mod.__name__, "file:", mod.__file__)
        print(sepline)
    count = 0
    for attr in mod.__dict__:
        print("{0:*>05}) {1}".format(count, attr), end=' ')
        if attr.startswith("__"):
            print("<built-in name>")
        else:
            print(getattr(mod, attr))       # Same as mod.__dict__[attr]
        count += 1
    if verbose:
        print(sepline)
        print("{0} has {1} names".format(mod.__name__, count))
        print(sepline)


if __name__ == "__main__":
    import mydir
    listing(mydir)      # Self-test code: list myself
