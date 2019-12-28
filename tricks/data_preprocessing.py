import time
import os
import pandas as pd

rootdir = 'D:\ALI\Metro_train'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
trains = []
for i in range(len(list)):
    path = os.path.join(rootdir, list[i])#os.path.join()
    if os.path.isfile(path):
        trains.append(path)
trains.sort()

time_start=time.time()

def getTimeIdx(ttime): # read : 2019-01-01 02:00:05
  
    time = ttime[-8:]
    hh = int(time[:2])
    mm = int(time[3:5])
 
#     print(str(hh[0]) + str(hh[1]) + ':' + str(mm[0]) + '0:00')
    ans = hh * 6 + (mm // 10)
    
    return ans

def save_day_file(save_path, inNums, outNums):
    if os.path.exists(save_path) == False:
        os.makedirs(save_path)
    for station in range(81):
        with open(save_path + "\station" + str(station) + ".csv", 'w') as fw:
            fw.write("time,inNums,outNums\n")
            for i in range(144):
                fw.write(str(i+1) + ',' + str(inNums["station" + str(station)][i]) + ',' +  str(outNums["station"+str(station)][i]) + '\n')

for day in range(1, 25):
    
    path = trains[day]
    rootdir = 'D:\ALI\Metro_process'
    save_path = os.path.join(rootdir, "day" + str(day+1)) # 25天
    
    if os.path.exists(save_path) == False:
        os.makedirs(save_path)
    
    inNums = {}
    for i in range(81):  # station from 0 to 80
        inNums["station" + str(i)] = {}
        for jj in range(144):
            inNums["station" + str(i)][jj] = 0
    outNums = {}
    for i in range(81):  # station from 0 to 80
        outNums["station" + str(i)] = {}
        for jj in range(144):
            outNums["station" + str(i)][jj] = 0
    
    df = pd.read_csv(path)  # time, stationID, status
    # inNums[station3][timeIdx] += 1
    # inNums[0:80][0:143] = 2008
    for idx in range(len(df)):
        dd = df['status'][idx]
        if(idx % 10000 == 0):
            print(idx)
        if dd == 0:
            outNums["station" + str(df['stationID'][idx])][getTimeIdx(df['time'][idx])] += 1
        else:
            inNums["station" + str(df['stationID'][idx])][getTimeIdx(df['time'][idx])] += 1
    save_day_file(save_path, inNums, outNums)
    
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
