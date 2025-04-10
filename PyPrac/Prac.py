print("김대중")
ark = range(5)
print(ark)
temp = [1,2,3,4,5]
minso = 23

#print(next(uzin))

def printntime(value, n):
    for i in range(n):
        print(value)

def testfunc():
    ark = temp[2]
    global minso
    minso = minso +1
    print(ark)
    print(minso)

ark = lambda x:x**2

testfunc()