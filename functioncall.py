import sys

#this is a random comment

def funtionCall(pstring):
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