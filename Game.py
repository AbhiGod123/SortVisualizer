from graphics import *
import random

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            singleRect(i)
            singleRect(j)
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    singleRect(i+1)
    singleRect(high)
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def insertionSort(arr):
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)):
        key = arr[i]
		
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            w = j + 1
            j -= 1
            singleRect(w)
        arr[j + 1] = key
        w = j + 1
        singleRect(w)

def singleRect(w):
    width = win.width/float(len(arr))
    height = win.height/float(max(arr))
 
    px = Point(w * width, win.height)
    py = Point((w+1)*width, win.height - arr[w]*height)	

    clearRect = Rectangle(px,Point((w+1)*width,0))
    clearRect.setFill("Black")    
    clearRect.draw(win)

    greenrect = Rectangle(px,py)
    greenrect.setFill("Green")
    greenrect.draw(win)
 
    rect = Rectangle(px,py)
    rect.setFill(color)
    rect.draw(win)

def sortFish():
    width = win.width/float(len(arr))
    height = win.height/float(max(arr))

    bigrect = Rectangle(Point(0,win.height),Point(win.width,0))
    bigrect.setFill("Black")
    bigrect.draw(win)

    for i in range(len(arr)):
        singleRect(i)
		
win = GraphWin("Sort", 600, 600)
win.setBackground("black");		

arr = list(range(5,100))
# print(arr)
random.shuffle(arr)

color = "Red"

sortFish()
#insertionSort(arr)
quickSort(arr,0,len(arr)-1)

win.getMouse() # Pause to view result
win.close()    # Close window when done
		
