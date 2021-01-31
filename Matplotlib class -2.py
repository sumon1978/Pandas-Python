
# coding: utf-8

# In[111]:


from matplotlib import pyplot as plt
import numpy as np
x= np.arange(1,11)
y=np.random.random(10)
print(x)
print(y)
fig,ax=plt.subplots(figsize=(10,6))
ax.bar(x,y)


# In[25]:


from matplotlib import pyplot as plt
x=np.arange(1,11)
y=np.random.random(10)
print (x)
print(y)
fig,ax=plt.subplots(figsize=(10,6))
ax.plot(x,y)
#ax.set_title('Customized Title',loc=left,fontdict={})


# In[26]:


x=np.arange(1,11)
y=np.random.random(10)
plt.plot(x,y)
print (x)
print (y)
plt.xlim(1,15)


# In[74]:


from matplotlib import pyplot as plt
import numpy as np
x=np.arange(1,11)
y=np.random.random(10)
plt.plot(x,y)
plt.xlabel('My x-label',color='blue',family='sumon',weight='bold',fontsize=15)
plt.xlabel('My y-label',fontsize='small')
plt.show()


# In[39]:


x=np.arange(1,11)
y=np.random.random(10)
fig,ax=plt.subplots(figsize=(10,6))
ax.plot(x,y,marker='o',markerfacecolor='orange',markersize=12,linestyle='--',color='skyblue',linewidth=4)


# In[55]:


x=np.arange(1,11)
y=np.random.random(10)
fig,ax=plt.subplots(figsize=(10,4))
print(x)
print (y)
ax.plot(x,y,marker='o',linestyle='--')
for i in range (len(x)):
    xi="{:.1f}".format(x[i])
    yi="{:.1f}".format(y[i])
    s=str("P("+ str(xi)+','+str(yi)+')')
    ax.text(x[i]+0.02,y[i]+0.03,s)


# In[66]:


x=np.linspace(1,10,50)
y1=np.sin(x)
y2=np.cos(x)
fig,ax=plt.subplots(1,1,figsize=(8,4))
ax.plot(x,y1,linestyle='--',color='olive',label='Sine Func')
ax.plot(x,y2,color='#FF0000',linewidth=2,label='Cos Func')
ax.set_title('Multiple line plots with legends')
ax.legend()


# In[71]:


x=np.linspace(1,10,50)
y1=np.sin(x)
y2=np.cos(x)
fig,ax=plt.subplots(1,1,figsize=(8,4))
ax.plot(x,y1,linestyle='--',color='olive',label='Sine Func')
ax.plot(x,y2,color='#FF0000',linewidth=2,label='Cos Func')
ax.set_title('Multiple line plots with legends')
ax.legend(fancybox=True,loc='upper left',framealpha=1,shadow=True,borderpad=1,fontsize=10)


# In[72]:


plt.style.use('seaborn-darkgrid')
x=np.linspace(1,10,50)
y1=np.sin(x)
y2=np.cos(x)
fig,ax=plt.subplots(1,1,figsize=(8,4))
ax.plot(x,y1,linestyle='--',color='olive',label='Sine Func')
ax.plot(x,y2,color='#FF0000',linewidth=2,label='Cos Func')
ax.set_title('Multiple line plots with legends')
ax.legend()


# In[109]:



x=np.arange(1,11)
y=np.random.random(10)
plt.plot(x,y)
plt.xlabel('My x-label',color='blue',family='sumon',weight='bold',fontsize=15)
plt.xlabel('My y-label',fontsize='small')
plt.savefig('test.jpeg')


# In[96]:


import matplotlib.pyplot as plt
w=4
h=3
d=70
plt.figure(figsize=(w,h),dpi=d)
ax=plt.gca()
ax.plot(t,exp_data)
ax.set_title('Exponential')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
fig,ax1=plt.subplots()
color='tab:red'
ax1.set_xlabel('Time(s)')
ax1.set_ylable('Exponential',color=color)
axi.plot(t,exp_data,color=color)
axi1.tick_params(axis='y',labelcolor=color)

ax2=ax1.twinx()

color='tab:blue'
ax2.set_ylabel('Sine Func.',color=color)
ax2.plot(t,sin_data,color=color)
ax2.tick_params(axis='y',labelcolor=color)

ax2.yasis.grid()


# In[110]:


fig,ax=plt.subplots(1,1,facecolor='lightgray')
ax.axis([0,10,0,10])

ax.text(1,5,'.Data:(1,5)',transform=ax.transData)
ax.text(0.5,0.1,'.Axes:(0.5,0.1)',transform=ax.transAxes)
ax.text(1,1,'.Figure:(1,1)',transform=fig.transFigure);


# In[105]:


get_ipython().run_line_magic('matplotlib', 'notebook')
fig,ax=plt.subplots()
x=np.linspace(0,20,1000)
ax.plot(x,np.cos(x))
ax.axis('equal')
ax.annotate('local maximum',xy=(6.28,1),xytext=(10,5),
            arrowprops=dict(facecolor='black',shrink=0.05))
ax.annotate('local minium',xy=(5*np.pi,-1),xytext=(2,-6),
           arrowprops=dict(arrowstyle="->",
                          connectionstyle="angle3,angleA=90,angleB=0"));

