```python3
for i in range(1, 65):
    plt.subplot(8,8,i)
    plt.imshow(pic[i-1])
    plt.axis('off')
plt.show()
```
