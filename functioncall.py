import sys

def funCall(pstring):
    arr = []
    cd = {')':'(', ']':'[', '}':'{'}
    for i in pstring:
        if i in ['(', '[', '{']:
            arr.append(i)
        elif i in [')', ']', '}']:
            if len(arr) == 0:
                return False
            if arr[-1] != cd[i]:
                return False
            arr = arr[:-1]
    return len(arr) == 0