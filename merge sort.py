from tkinter import *
from random import shuffle
from time import sleep

# set up data
data = [1,2,3,4,5,6,7,8]
shuffle(data)
print(data)

## graphical stuff
# window
window = Tk()
c = Canvas(window,width = 850,height = 350, bg='lightblue')
c.pack()
desctext = c.create_text(425,25,fill='black',font='Times 15',text='Circles touching each other are part of the same list.',anchor = 'n')

# circle creation
circles = []
texts = []
for i in range(len(data)):
    circles.append(c.create_oval(50*i+225,75,50*i+275,125,fill='red',outline='black'))
    texts.append(c.create_text(50*i+250,100,fill='black',font = 'Times 30',text = data[i],anchor = 'center'))
window.update()
sleep(3)

# functions for screen
def movecircleto(circle,x_dest,y,steps,secs): # moves circle at index <circle> in circles to <x_dest> and <y> down with <steps> steps in <secs> seconds
    circx = c.coords(texts[circle])[0]
    distance = x_dest - circx
    for i in range(steps):
        c.move(circles[circle],distance/steps,y / steps)
        c.move(texts[circle],distance/steps,y / steps)
        window.update()
        sleep(secs / steps)

def updatetext(text):
    c.itemconfig(desctext,text = text)
    window.update()

# break data into lists of length 1
updatetext('Breaking data into lists of length 1')
lists = []
for i in range(len(data)):
    lists.append([data[i]])
    movecircleto(i,100*(i+1)-25,50,20,0.5)
    window.update()
    sleep(0.1)

print(lists)

# function that will merge a pair of sorted lists into one sorted list
def merge_lists(index): # merges lists[index] and lists[index+1] -> lists[index] is overwritten with the merged list and lists[index+1] is deleted
    # setup needed variables and lists
    global lists
    list1 = lists[index]
    list2 = lists[index+1]
    numbers = len(list1) + len(list2)
    sortedlist = []
    list1index = 0
    list2index = 0
    deststart = ((850/next_length)*(i+0.5)) - 50*(numbers/2) + 25

    # iterate so every number is used
    for j in range(numbers):
        # check if both lists still have values left
        if list1index < len(list1) and list2index < len(list2):
            list1check = list1[list1index]
            list2check = list2[list2index]

            # add the smallest number and shift to the next one in the respective list
            if list1check < list2check:
                sortedlist.append(list1check)
                list1index += 1
                circleindex = data.index(list1check)
            else:
                sortedlist.append(list2check)
                list2index += 1
                circleindex = data.index(list2check)
        
        # if one is full just add from the other
        elif list1index >= len(list1):
            sortedlist.append(list2[list2index])
            circleindex = data.index(list2[list2index])
            list2index += 1
        elif list2index >= len(list2):
            sortedlist.append(list1[list1index])
            circleindex = data.index(list1[list1index])
            list1index += 1
        
        movecircleto(circleindex,deststart + j*50,50,20,0.5)

    #overwrite lists with the answer
    lists[index] = sortedlist
    del lists[index+1]

# merge lists until there is only one left
updatetext('Merging lists...')
while len(lists) != 1:
    next_length = len(lists)//2 + len(lists)%2
    for i in range(len(lists)//2):
        merge_lists(i)
    print(lists)
    sleep(1)

updatetext('Complete.')
window.mainloop()