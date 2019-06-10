import threading
import time


def test(p):
    time.sleep(0.001)  # time.sleep(float)   程序会被挂起指定时间。
    print(p)


ts = []
for i in range(0, 15):  # 迭代线程
    th = threading.Thread(target=test, args=[i])
    th.start()
    ts.append(th)
for i in ts:
    i.join()
print("hoho,end!!!!!")
