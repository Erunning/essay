```python3
# 折线图展示
import matplotlib.pyplot as plt
x1=[]; y1=[]; x2=[]; y2=[]
for key in day_in:
    x1.append(key)
    y1.append(day_in[key])
for key in day_out:
    x2.append(key)
    y2.append(day_out[key])
plt.plot(x1,y1,label='people in',linewidth=1,color='r',marker='.', markerfacecolor='blue',markersize=5) 
plt.plot(x2,y2,label='people out') 
plt.xlabel('Day') 
plt.ylabel('the number of people') 
plt.title('the number of people floating in 25 days')
#点标注
plt.text(x1[0], y1[0], 'Thuesday', ha='center', va='bottom', fontsize=10)
plt.text(x1[3], y1[3], 'Friday', ha='center', va='bottom', fontsize=10)
plt.text(x1[10], y1[10], 'Friday', ha='center', va='bottom', fontsize=10)
plt.text(x1[17], y1[17], 'Friday', ha='center', va='bottom', fontsize=10)
plt.text(x1[24], y1[24], 'Friday', ha='center', va='bottom', fontsize=10)
#显示图例&画图
plt.legend() 
plt.show() 
```
