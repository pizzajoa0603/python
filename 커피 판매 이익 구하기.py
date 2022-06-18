# ch01ex06.py
# 커피 판매 이익 구하기

print('일일판매량을 입력하세요')

an=int(input('아매리카노 판매수'))
cn=int(input('카페라데 판매수'))
pn=int(input('카푸치노 판매수'))

s = an * 2000 + cn  * 3000 + pn * 3500
print()
print(f'일일 판매 매출액은 {s}입니다.')

m_s = s * 30
print(f'한 달 30일 기준이상 {m_s} 입니다.')

print()
p = int(input('예상 지출액을 입력하세요:'))
po = m_s -p
print(f'한 달 예상 순이익은 {po}입니다.')
      


