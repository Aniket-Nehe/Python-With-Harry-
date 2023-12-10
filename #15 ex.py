import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
H=int(time.strftime('%H'))
print(H)
M=time.strftime('%M')
print(M)
S=time.strftime('%S')
print(S)

if H>5 and H<12:
    print("Good Morning")
elif H>=12 and H<5:
    print("Good Afternoon")
elif H>=6 and H<=10:
    print("Good Evening")
elif H>=10 and H<=4:
    print("Good Night")