x = [1, 2, 3]
y = [5,25,125]

#plotting the values on the graph 
plt.plot(x,y,color='green', label='5**x', linewidth=2, marker='x', markersize=10, markeredgecolor='red')

#Defines the title of the graph , it is posible to use the parameter fontdict to change the text style
plt.title('My first graph' , fontdict={'fontsize':'20',})

#Defines the texts for the X and Y axis 
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#Modifies the ticks 
plt.xticks([1,2,3])
plt.yticks([5,25,125])


plt.legend() #Shows the legend to the parameter label
plt.show()  #Displays the graph automatically 
