```python3
import torch
from torch.autograd import Variable # torch 中 Variable 模块


tensor = torch.FloatTensor([[1,2],[3,4]])

variable = Variable(tensor, requires_grad=True) #容器

v_out = torch.mean(variable*variable)   # （x1^2+x2^2+x3^2+x4^2)/4

v_out.backward()    # 误差反向传递


print(variable.grad)    # 梯度计算结果,只能对torch.autograd.Variable使用
'''
 0.5000  1.0000
 1.5000  2.0000
'''


print(variable)     #  Variable 形式

print(variable.data)    # tensor 形式

print(variable.data.numpy())    # numpy 形式
```
