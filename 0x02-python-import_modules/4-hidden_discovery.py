#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i[0] == "_" and i[1] == "_":
            pass
        else:
            print(i)
