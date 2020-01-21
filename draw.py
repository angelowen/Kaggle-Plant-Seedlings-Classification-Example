import matplotlib.pyplot as plt
import re
import numpy as np
def read_file():
    list_loss,list_acc=[],[]
    with open ("output1.txt","r") as fp:
        all_lines = fp.readlines()
    flag,cnt=0,1
    for line in all_lines:
        if flag is 0:
            flag = 1
            continue
        if cnt%4==3:
            # print(line)
            mylist=re.findall(r"\d+\.?\d*", line)
            list_loss.append(mylist[0])
            list_acc.append(mylist[1])
        cnt+=1
    
    list_loss = list(map(float, list_loss))
    list_acc = list(map(float, list_acc))
    print(list_loss,list_acc)
    pic(list_loss,list_acc)

def pic(list_loss,list_acc):
    t=len(list_loss)
    times = [i for i in range(1,t+1)]
    
    # list_loss = [255,246,247.5,227,224,216.5,246,256,262.5,234,225.5,225.5]
    # list_acc = [92.2,88.1,88.5,82.9,85.7,83.2,83.8,80.5,79.2,78.8,71.9,70.8]

    # 設定圖片大小為長15、寬10
    plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
    # 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意
    plt.plot(times,list_loss,'s-',color = 'r', label="Loss")
    # 把資料放進來並指定對應的X軸、Y軸的資料 用圓形做標記(o-)，並指定線條顏色為綠色、使用label標記線條含意
    plt.plot(times,list_acc,'o-',color = 'g', label="Accuracy")
    # 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離
    plt.title("times & Loss,Accuracy",  x=0.5, y=1.03)

    ticks = np.linspace(0,3,20)
    plt.yticks(ticks)
    # 设置刻度字体大小
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    # 標示x軸(labelpad代表與圖片的距離)
    plt.xlabel("times", fontsize=30, labelpad = 15)
    # 標示y軸(labelpad代表與圖片的距離)
 # plt.ylabel("price", fontsize=30, labelpad = 20)
    # 顯示出線條標記位置
    plt.legend(loc = "best", fontsize=20)
    # 畫出圖片
    plt.show()
if __name__=='__main__':
    read_file()
    # pic()