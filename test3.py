import numpy as np
a3=np.array([1,3,7,1,2,6,0,1])
# a3 = np.array([1,2,3,4,5,4,3,2,1])
# # numpy.diff —— 计算离散差值，后一个数减去前一个数
# a=np.diff(a3)
# print(a)
# # numpy.sign —— 取正负号，sign(x) = 1(x>0) / 0(X=0) / -1(X<0)
# b=np.sign(a)
# print(b)
# # 获取b中值为-1的下标
# peak_loc=np.where(b==-1)
# # 输出
# print (a3[peak_loc])

peak = []
for i in range(1, len(a3)-1):
    if (a3[i] > a3[i-1]) and (a3[i] > a3[i+1]):
        peak.append(a3[i])
print(peak)