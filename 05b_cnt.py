# 05b_cnt.py
#숫자 출력

print('[0-4]')

for x in range(5):
     print(x)
     
print('[1-11]')

for x in range(1, 11):
    print(x)
    
s = 0
for x in range(1, 11):
    s = s + x
    s = s + x
    
s = 0
for x in range(1, 11):
    s = s + x
    print('x:', x, ', s :', s)
    print(f'x: {x}, s: {s}')
