# my_tiny_tool
some script tool

## matplotlib

the plot template
```python
plt.figure(figsize = (3.2, 3)) # 创建一个图像窗口,宽3.2 inch, 高 3 inch
plt.rc('xtick',labelsize = 9)  # 调整tick的size
plt.rc('ytick',labelsize = 9)

plt.legend(loc = 'best', prop = {'size' : 9}, frameon = False) # 调整legend的位置，字体大小和边框 

plt.tight_layout()   # 紧凑显示图片，居中显示

plt.show() # 显示图片
```
