import Tkinter
import random
bg = ['Red','Aqua','Blue','cyan','teal','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=10

def startGame(event):

    
    if timeleft == 10:
        
        countdown()
        
    nextColour()
def nextColour():
    global score
    global timeleft
    timeleft =10
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == bg[1].lower():
            score += 1
            timeLabel.config(text="Time left: " + str(timeleft))
        e.delete(0, Tkinter.END)
        random.shuffle(bg)
        label.config(fg=str(bg[1]), text=str(bg[0]))
        
        scoreLabel.config(text="Score: " + str(score)) 
def countdown():

    
    global timeleft
    if timeleft > 0:       
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        timeLabel.config(text="Time UP!!!!")
        e.config(state='disabled')
root = Tkinter.Tk()
root.title("Color Game")
root.geometry("400x250")
instructions = Tkinter.Label(root, text="Type Colour Name,Not Word Text!", font=('Bold', 12))
instructions.pack()
scoreLabel = Tkinter.Label(root, text="Press enter to start", font=('Bold', 12))
scoreLabel.pack()
timeLabel = Tkinter.Label(root, text="Time left: " + str(timeleft), font=('Bold', 12))
timeLabel.pack()
label = Tkinter.Label(root, font=('Bold', 70))
label.pack()

e = Tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
