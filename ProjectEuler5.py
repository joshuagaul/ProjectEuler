def check(num):
    for x in range(2, 21): 
        if num % x != 0:
            return False

    return True

go = True
num = 2520
offset = 100000
answer = 0

while(go):
    if (check(num)):
        answer = num
        go = False
    else:
        num += 2520
    if (num > offset):
        print str(num) + "\n"

print "The answer is: " + str(num) + "!!!"