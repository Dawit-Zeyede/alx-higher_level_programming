#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for fun in dir(hidden_4):
        if fun[0] != '_' and fun[1] != '_':
            print(fun)
