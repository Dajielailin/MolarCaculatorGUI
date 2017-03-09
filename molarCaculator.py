#制作一个关于摩尔百分比计算器的GUI
from tkinter import * #从tkinter库中导入所有定义
import time
class molarCaculator:
    def __init__(self):
        win = Tk()
        win.title("Molar caculator")
    #创建相对分子质量标签及对应文本框，假定有9种物质
        X=[1]*10
        Label(win,text="相对分子质量",justify=LEFT).grid(row=1,column=1,sticky=W)
        #物质1
        self.X1=DoubleVar()
        E11=Entry(win,textvariable=self.X1,justify=LEFT)
        E11.grid(row=2,column=1,sticky=W)
        #物质2
        self.X2=DoubleVar()
        E21=Entry(win,textvariable=self.X2,justify=LEFT)
        E21.grid(row=3,column=1,sticky=W)
        #物质3
        self.X3=DoubleVar()
        E31=Entry(win,textvariable=self.X3,justify=LEFT)
        E31.grid(row=4,column=1,sticky=W)
        #物质4
        self.X4=DoubleVar()
        E41=Entry(win,textvariable=self.X4,justify=LEFT)
        E41.grid(row=5,column=1,sticky=W)
        #物质5
        self.X5=DoubleVar()
        E51=Entry(win,textvariable=self.X5,justify=LEFT)
        E51.grid(row=6,column=1,sticky=W)
        #物质6
        self.X6=DoubleVar()
        E61=Entry(win,textvariable=self.X6,justify=LEFT)
        E61.grid(row=7,column=1,sticky=W)
        #物质7
        self.X7=DoubleVar()
        E71=Entry(win,textvariable=self.X7,justify=LEFT)
        E71.grid(row=8,column=1,sticky=W)
        #物质8
        self.X8=DoubleVar()
        E81=Entry(win,textvariable=self.X8,justify=LEFT)
        E81.grid(row=9,column=1,sticky=W)
        #物质9
        self.X9=DoubleVar()
        E91=Entry(win,textvariable=self.X9,justify=LEFT)
        E91.grid(row=10,column=1,sticky=W)
        
    #创建摩尔百分比标签及对应的输入文本框
        Label(win,text="摩尔百分比",justify=LEFT).grid(row=1,column=2,sticky=W)
         #物质1
        self.M1=DoubleVar()
        E12=Entry(win,textvariable=self.M1,justify=LEFT)
        E12.grid(row=2,column=2)
        #物质2
        self.M2=DoubleVar()
        E22=Entry(win,textvariable=self.M2,justify=LEFT)
        E22.grid(row=3,column=2)
        #物质3
        self.M3=DoubleVar()
        E32=Entry(win,textvariable=self.M3,justify=LEFT)
        E32.grid(row=4,column=2)
        #物质4
        self.M4=DoubleVar()
        E42=Entry(win,textvariable=self.M4,justify=LEFT)
        E42.grid(row=5,column=2)
        #物质5
        self.M5=DoubleVar()
        E52=Entry(win,textvariable=self.M5,justify=LEFT)
        E52.grid(row=6,column=2)
        #物质6
        self.M6=DoubleVar()
        E62=Entry(win,textvariable=self.M6,justify=LEFT)
        E62.grid(row=7,column=2)
        #物质7
        self.M7=DoubleVar()
        E72=Entry(win,textvariable=self.M7,justify=LEFT)
        E72.grid(row=8,column=2)
        #物质8
        self.M8=DoubleVar()
        E82=Entry(win,textvariable=self.M8,justify=LEFT)
        E82.grid(row=9,column=2)
        #物质9
        self.M9=DoubleVar()
        E92=Entry(win,textvariable=self.M9,justify=LEFT)
        E92.grid(row=10,column=2)

        
    #创建三个按钮分别命名为，清除，重置和计算
        Button(win,text="清除",command=self.clear,justify=RIGHT).grid(row=1,column=3)
        Button(win,text="重置",command=self.reset,justify=RIGHT).grid(row=1,column=5,\
                              )
        Button(win,text="计算",command=self.caculator,justify=RIGHT).grid(row=1,column=4)
        Button(win,text="保存",command=self.saveData,justify=RIGHT).grid(row=1,column=6)

    #创建总质量标签及相应输入文本框
        Label(win,text="总质量",justify=RIGHT).grid(row=2,column=3)
        self.Mass=DoubleVar()
        Entry(win,textvariable=self.Mass,justify=RIGHT).grid(row=2,column=4)
        Label(win,text="g   ",justify=RIGHT).grid(row=2,column=5)

    #创建输出区域
        Label(win,text="  序号   ").grid(row=3,column=3)
        Label(win,text=" 质量/g  ").grid(row=3,column=4,columnspan=2)
        #显示第一种成分的质量
        L11=Label(win,text=" 1 ",bg="white")
        L11.grid(row=4,column=3)
        self.L12=Label(win,text="",bg="white")
        self.L12.grid(row=4,column=4,columnspan=2)
        #显示第二种成分的质量
        L21=Label(win,text=" 2 ",bg="white")
        L21.grid(row=5,column=3)
        self.L22=Label(win,text="",bg="white")
        self.L22.grid(row=5,column=4,columnspan=2)
        #显示第三种成分的质量
        L31=Label(win,text=" 3 ",bg="white")
        L31.grid(row=6,column=3)
        self.L32=Label(win,text="",bg="white")
        self.L32.grid(row=6,column=4,columnspan=2)
        #显示第四种成分的质量
        L41=Label(win,text=" 4 ",bg="white")
        L41.grid(row=7,column=3)
        self.L42=Label(win,text="",bg="white")
        self.L42.grid(row=7,column=4,columnspan=2)
        #显示第五种成分的质量
        L51=Label(win,text=" 5 ",bg="white")
        L51.grid(row=8,column=3)
        self.L52=Label(win,text="",bg="white")
        self.L52.grid(row=8,column=4,columnspan=2)
        #显示第六种成分的质量
        L61=Label(win,text=" 6 ",bg="white")
        L61.grid(row=9,column=3)
        self.L62=Label(win,text="",bg="white")
        self.L62.grid(row=9,column=4,columnspan=2)
        #显示第七种成分的质量
        L71=Label(win,text=" 7 ",bg="white")
        L71.grid(row=10,column=3)
        self.L72=Label(win,text="",bg="white")
        self.L72.grid(row=10,column=4,columnspan=2)
        #初试界面
        self.reset()
        
        

        
        win.mainloop()
    
    def clear(self):
        self.Mass.set('')
    def reset(self):
        self.M1.set('0')
        self.M2.set('0')
        self.M3.set('0')
        self.M4.set('0')
        self.M5.set('0')
        self.M6.set('0')
        self.M7.set('0')
        self.M8.set('0')
        self.M9.set('0')
        self.X1.set('0')
        self.X2.set('0')
        self.X3.set('0')
        self.X4.set('0')
        self.X5.set('0')
        self.X6.set('0')
        self.X7.set('0')
        self.X8.set('0')
        self.X9.set('0')
        self.L12["text"]=''
        self.L22["text"]=''
        self.L32["text"]=''
        self.L42["text"]=''
        self.L52["text"]=''
        self.L62["text"]=''
        self.L72["text"]=''
        self.Mass.set('')
      
          
    def caculator(self):
        sumOfXM = self.X1.get()*self.M1.get() + self.X2.get()*self.M2.get() + self.X3.get()*self.M3.get() + self.X4.get()*self.M4.get() \
                      + self.X5.get()*self.M5.get() + self.X6.get()*self.M6.get() + self.X7.get()*self.M7.get()
        massRateOfX1= self.X1.get()*self.M1.get() / sumOfXM
        massRateOfX2= self.X2.get()*self.M2.get() / sumOfXM
        massRateOfX3= self.X3.get()*self.M3.get() / sumOfXM
        massRateOfX4= self.X4.get()*self.M4.get() / sumOfXM
        massRateOfX5= self.X5.get()*self.M5.get() / sumOfXM
        massRateOfX6= self.X6.get()*self.M6.get() / sumOfXM
        massRateOfX7= self.X7.get()*self.M7.get() / sumOfXM
        massofX1 = self.Mass.get() * massRateOfX1
        massofX2 = self.Mass.get() * massRateOfX2
        massofX3 = self.Mass.get() * massRateOfX3
        massofX4 = self.Mass.get() * massRateOfX4
        massofX5 = self.Mass.get() * massRateOfX5
        massofX6 = self.Mass.get() * massRateOfX6
        massofX7 = self.Mass.get() * massRateOfX7
        self.L12["text"]=format(massofX1,"6.3f")
        self.L22["text"]=format(massofX2,"6.3f")
        self.L32["text"]=format(massofX3,"6.3f")
        self.L42["text"]=format(massofX4,"6.3f")
        self.L52["text"]=format(massofX5,"6.3f")
        self.L62["text"]=format(massofX6,"6.3f")
        self.L72["text"]=format(massofX7,"6.3f")
    #写一个saveData()函数,存储上一次的数据   
    def saveData(self):
        #打开文件
        infile=open("Data.txt","w")
        infile.write(str(self.X1.get())+','+str(self.M1.get())+'\n')
        infile.write(str(self.X2.get())+','+str(self.M2.get())+'\n')
        infile.write(str(self.X3.get())+','+str(self.M3.get())+'\n')
        infile.write(str(self.X4.get())+','+str(self.M4.get())+'\n')
        infile.write(str(self.X5.get())+','+str(self.M5.get())+'\n')
        infile.write(str(self.X6.get())+','+str(self.M6.get())+'\n')
        infile.write(str(self.X7.get())+','+str(self.M7.get())+'\n')
        
        infile.close()
      
    
molarCaculator()

        
