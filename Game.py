from graphics import *
import random

def insertionSort(arr,win,color): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  	sortFish(win,arr,color)

        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
		sortFish(win,arr,color)
                j -= 1
        arr[j + 1] = key
	sortFish(win,arr,color) 

def sortFish(win,arr,color):
    width = win.width/len(arr)
    height = win.height/max(arr)

    bigrect = Rectangle(Point(0,win.height),Point(win.width,0))
    bigrect.setFill("Black")
    bigrect.draw(win)

    for i in range(len(arr)):
	px = Point(i * width, win.height)
	py = Point((i+1)*width, win.height - arr[i]*height)	
	rect = Rectangle(px,py)
        rect.setFill(color)
        rect.draw(win)

def main():
    win = GraphWin("My Circle", 800, 600)
    win.setBackground("black");		

    arr = range(10,50)
    print(arr)
    random.shuffle(arr)
    print(arr)
    #sortFish(win,arr,"Red")

    insertionSort(arr,win,"Red")
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()

