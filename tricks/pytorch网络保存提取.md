```python3
  
    torch.save(net, 'D:/net.pkl') #保存整个网络
    torch.save(net.state_dict(), 'D:/net_params.pkl') #只保存网络中的参数，推荐


    # restore entire net1 to net2
    net2 = torch.load('net.pkl')
    prediction = net2(x)
    
    
    #提取参数，推荐
    net3 = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
    )
    net3.load_state_dict(torch.load('net_params.pkl'))
    prediction = net3(x)
```
