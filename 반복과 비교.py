# ch02ex4_2.py
# 반복과 비교

for x in range(1, 11):
    if x % 2 == 0:
        msg = '짝수'
    else:
        msg = '홀수'
    print(f'{x}은(는){msg}입니다.') # 1은(는) 홀수입니다.


    # 1은(는) 로나눈 나머지가 1이므로 홀수입니다.
