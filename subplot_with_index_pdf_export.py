fig=plt.figure(figsize=(12,16))
font = {'family' : 'serif',  
        'color'  : 'darkred',  
        'weight' : 'normal',  
        'size'   : 16,  
        }  
for i in range(10):
    ax=fig.add_subplot(2,5,i+1)
    ax.matshow(inter_snapshot[i])
    ax.set_xlabel('('+str(i)+')',fontdict=font)
    
plt.show()
fig.savefig('y_pred.pdf',bbox_inches='tight')
