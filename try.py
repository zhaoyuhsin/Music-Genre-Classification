str = "rock_15_0"
def str2num(str):
    ans = 0
    flag = False
    for i in range(len(str)):
        if (str[i] == '_'):
        	flag = not flag
        	continue
        if (flag):
            ans = ans * 10 + int(str[i])
    return ans
print(str2num(str))