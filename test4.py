import math
import random
from scipy.stats import norm, zscore
population=eval(input("請輸入母體大小: "))
poewr=eval(input("請輸入信心水準: "))
error=eval(input("請輸入誤差範圍: "))
z = norm.isf([poewr/2])
n=((0.25*((z/error)**2))/(1+(1/population)*(0.25*(z/error)**2-1)))
sample=math.ceil(n)
print("需抽出樣本數為: %d"%sample)
data = range(1,population+1)
print(random.sample(data,sample))