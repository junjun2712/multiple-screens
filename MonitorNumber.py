# -*- coding: utf-8 -*-
"""
功能：识别多个显示器各自的分辨率 
@Author:Cole
Version:2.0
"""
"""模块导入"""
from win32api import GetSystemMetrics
import win32api 
from win32con import SM_CMONITORS, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN
import os,time
import jmespath
from tkinter import * 
import tkinter as tk
from tkinter import filedialog



#显示器数量检测
MonitorNumber = GetSystemMetrics(SM_CMONITORS)
#print (type(MonitorNumber))
print("主屏幕个数：", MonitorNumber)
#主屏幕尺寸检测GetSystemMetrics(0)#主屏幕宽 GetSystemMetrics(1)#主屏幕高
print("主屏幕分辨率：", GetSystemMetrics(0),"*", GetSystemMetrics(1))
#配置文件路径
conf_path = os.path.abspath('.') 
file_path = conf_path + r'\conf.list'
#print(conf_path)
#print(file_path)
#浏览器用户文件夹路径
Temp_path = conf_path + r'\user'

file_name_chrome = []

def file_name():
    root = Tk()
    root.withdraw()
    Filepath = filedialog.askopenfilename()
    file_name_chrome.append(Filepath)
    print(file_name_chrome)

def show_monitor():
    for url,i in zip(open(file_path),range(MonitorNumber)):
        lj = str(url)
        lj = lj.replace('\n', '').replace('\r', '')
        monitors = win32api.EnumDisplayMonitors()
        monitors_info = win32api.GetMonitorInfo(monitors[i][0])
        monitors_location = jmespath.search("Monitor",monitors_info)
        #每个屏幕分辨率
        monitors_fbl = str(monitors_location[0:2]).strip('[()\n]').replace(" ","")
        print(monitors_fbl)
        Path = file_name_chrome[0]
        #双引号负值变量
        yh_left = '"'
        yh_right = '"'        
        print(Path)
        CMD = "start \"\" {}{}{} --new-window {} --start-fullscreen --window-position={} --user-data-dir={}{}".format(yh_left,Path,yh_right,lj,monitors_fbl,Temp_path,i)
        #print(CMD)
        time.sleep(1)
        os.system(CMD)
        

def input_pw():
    for url,i in zip(open(file_path),range(MonitorNumber)):
        lj = str(url)
        lj = lj.replace('\n', '').replace('\r', '')
        Path = file_name_chrome[0]
        #双引号负值变量
        yh_left = '"'
        yh_right = '"' 
        print(Path)
        CMD = "start \"\" {}{}{} --new-window {} --start --window-position=0,100 --user-data-dir={}{}".format(yh_left,Path,yh_right,lj,Temp_path,i)
        #print(CMD)
        #print(url)
        os.system(CMD)
        
def kill_chrome():
    CMD = "TASKKILL /f  /IM  CHROME.EXE"
    os.system(CMD) 

def exit():
    root.quit()

root = Tk()
root.resizable(False,False) #禁止窗口最大化
root.geometry("300x230")
root.title("多屏显示 Author:Cole")
tk.Button(root, text="选择谷歌浏览器EXE", command=file_name).place(x = 60, y = 10, width=180, height=30)
tk.Button(root, text="开启多屏", command=show_monitor).place(x = 60, y = 50, width=180, height=30)
tk.Button(root, text="输入账号密码", command=input_pw).place(x = 60, y = 90, width=180, height=30)
tk.Button(root, text="结束浏览器", command=kill_chrome).place(x = 60, y = 130, width=180, height=30)
tk.Button(root, text="退出程序", command=exit).place(x = 60, y = 180, width=180, height=30)
root.mainloop()
   
