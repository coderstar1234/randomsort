import random

first select catagory 
   r for random number
   h for random hex
   o for random oct
second select value reference
 rather number (ex.. 1-100), 
 hex value (ex.. 0x58), or 
 oct value (ex.. 0o71)
 
There are preset inputs values for testing purposes
"""
try:
    t = input() or 'r'
except EOFError:
    t = 'r'

a =[]
b =[]
c =[]
while(len(a)<100):
   y = random.randint(1,100)
   if y in c:
      continue
   else:
      c.append(y)
      a.append(hex(y))
      b.append(oct(y))
if t == 'r':
       # Handle EOFError exception when calling input()
   try:
        r = int(input() or 68)  # random number
   except EOFError:
        r = 68
   print("\nnorm random:")
   print(c)
   if r in c:
      print("\nfound",r,'in list')
      for i in range(len(c)):
          print(c[i])
          if c[i] == r:
             print(f"found as no. {i+1} in list")
             print(f"norm: {r} hex: {a[i]} oct: {b[i]}")
             break
   else:
       print("\nnumber not found")
elif t == 'h':
     try:
        h = input() or '0x58'  # hex value
     except EOFError:
        h = '0x58'
     print("\nhex random:")
     print(a)
     if h in a:
        print("\nfound",h,'in list')
        for i in range(len(a)):
            print(a[i])
            if a[i] == h:
               print(f"found as no. {i+1} in list")
               print(f"norm: {c[i]} hex: {a[i]} oct: {b[i]}")
               break
        
     else:
         print("\nhex value not found")
elif t == 'o':
     try:
        o = input() or '0o71'  # oct value
     except EOFError:
        o = '0o71'
     print("\noct random:")
     print(b)
     if o in b:
        print("\nfound",o,'in list')
        for i in range(len(b)):
            print(b[i])
            if b[i] == o:
               print(f"found as no. {i+1} in list")
               
print(f"norm: {c[i]} hex: {a[i]} oct: {o}")
               break
     else:
         print("\noct value not found")
else:
    print("Incorrect type entered please try again")