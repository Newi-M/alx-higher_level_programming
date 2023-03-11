#!/usr/bin/python3

if __name__ == "__main__":
    '''prints all the names defined by the compiled module'''
    import hidden_4

    lists = dir(hidden_4)
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if (lists[i][j] == '_' and lists[i][j+1] == '_'):
                break
            else:
                print(lists[i])
                break
