import requests 
import matplotlib.animation as animation
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import time 
from itertools import count

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
ticker = 'PLTR'
url = (f'https://ca.finance.yahoo.com/quote/{ticker}?.tsrc=fin-srch' )
response = requests.get(url, headers= headers) 
html_content = response.text 

def Stock_price(): 
    response = requests.get(url, headers= headers)  
    soup = BeautifulSoup(response.text, 'lxml') 
    active_price = soup.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)' }).find('fin-streamer').text  
    
    return float(active_price.replace(',', ''))  



fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 20)  # Initial x-axis range
    ax.set_ylim(0, 40)  # Adjust y-axis range based on expected stock price variation
    return ln,

def update(frame):
    price = Stock_price()
    xdata.append(frame)
    ydata.append(price)
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update, frames=count(1), init_func=init, blit=True, interval=1000, cache_frame_data=False)
plt.show()

