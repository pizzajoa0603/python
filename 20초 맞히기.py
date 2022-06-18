# 07c_t.py
# 20초 맟히기

import time

# 1.준비안내
input('준비되면 엔터를 누르세요')
start = time.time()

# 2. 시작 시간


# 3. 종료 안내
input('20초를 센 후 엔터를 누르세요')
end = time.time()
# 4. 시간 계산
et = int(end - start)
t = abs(20 - et)

# 5. 결과 출력
print(f'실제시간: {et}초')
print(f'20초와 차이: {t}초')
