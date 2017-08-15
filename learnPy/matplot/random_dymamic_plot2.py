"""
绘制余弦周期运动的点，鼠标单击可暂停
"""
import matplotlib.pyplot as plt    
import numpy as np    
import matplotlib.animation as animation    
    
pause = False    
def simData():    
    t_max = 10.0    
    dt = 0.05    
    x = 0.0    
    t = 0.0    
    while t < t_max:    
        if not pause:    
            x = np.sin(np.pi*t)    
            t = t + dt    
        yield t, x #以生成器的形式返回 t, x
    
def onClick(event):    
    global pause    
    pause ^= True # 使用异或切换状态
    
def simPoints(simData):
    '''
    根据 simData() 生成的 t 和 x，绘制时间和点
    '''
    t, x = simData[0], simData[1]    
    time_text.set_text(time_template%(t))    
    line.set_data(t, x)    
    return line, time_text    
    
fig = plt.figure()    
ax = fig.add_subplot(111)    
line, = ax.plot([], [], 'bo', ms=90) # x轴，y轴，绘制圆点，绘制元素大小 
ax.set_ylim(-1, 1)
ax.set_xlim(0, 10)    
    
time_template = 'Time = %.1f s'    # prints running simulation time    
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)    
fig.canvas.mpl_connect('button_press_event', onClick)    
ani = animation.FuncAnimation(fig, simPoints, simData, blit=False, interval=10,    
    repeat=True)    
plt.show()   