#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    fun = dir(hidden_4)
    for f in fun:
        if f[0] == "_":
            continue
        else:
            print(f)
