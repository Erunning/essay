```python3
vgg16 = models.vgg16(pretrained=True) #加载网络结构和预训练模型
#static_dict()返回包含模块所有状态的字典
pretrained_dict = vgg16.state_dict()  #返回内置预训练vgg模块的字典
model_dict = model.state_dict()  #返回我们自己model的字典

#------------------------最关键的三步------------------------------------------
# 1. filter out unnecessary keys，也就是说从内置模块中删除掉我们不需要的字典
pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}

# 2. overwrite entries in the existing state dict，利用pretrained_dict更新现有的model_dict
model_dict.update(pretrained_dict)

# 3. load the new state dict，更新模型，加载我们真正需要的state_dict
model.load_state_dict(model_dict)
```
