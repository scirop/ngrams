import random
from tkinter import *

def gramify():
	root=Tk()
	root.iconbitmap('icon.ico')
	root.title("Codey Story")
	root.geometry('1000x600+100+20')

	var1=IntVar()
	var2=IntVar()

	scale2 = Scale(root, variable = var2, from_=1, to=1000, orient=HORIZONTAL, length=200, label="Set Length of Story")
	scale2.pack(anchor=N)

	frame1=Frame(root)
	frame1.pack()

	frame2=Frame(root)
	frame2.pack()

	labelEntry=Label(frame1, text="Enter the training story here")
	labelEntry.pack(side=TOP)

	labelEntry=Label(frame2, text="The new story shows below.")
	labelEntry.pack(side=TOP)

	entry=Text(frame1, height=10, width=100)
	entry.pack(side=TOP)

	newStoryText = Text(frame2, height= 10, width=100)
	def story():
		text=entry.get("1.0", END)
		length=scale2.get()
		newStoryText.delete('1.0', END)
		newStoryText.insert(INSERT,MarkovIt(length, text))
	newStoryText.pack(side=TOP)

	showButton = Button(frame1, text ="Create Story", command = story)
	showButton.pack(side=BOTTOM)
	QuitButton = Button(frame2, text="Quit", command=root.quit)
	QuitButton.pack(side=BOTTOM)

	root.mainloop()

def setup(text):
	ngrams={}
	j=0
	for i in range(0,len(text)):
		#if text[i]==" " or text[i]=="," or text[i] == "." or text[i]==";" or text[i]==":" or text[i]==
		if text[i]==(" " or "," or "." or ";" or ":"):
			gram=text[j:i]
			j=i+1
		if gram not in ngrams:
			ngrams[gram]=[]
		ngrams[gram].append(text[i])
	return ngrams
		
def MarkovIt(longstory, text):
	ngrams=setup(text)
	currentGram = ngrams[0]
	result = currentGram
	for x in range(1,longstory):
		if currentGram not in ngrams:
			break
		possibilities = ngrams[currentGram]
		nextchar = random.choice(possibilities)
		result = result+nextchar
		lenres=len(result)
		currentGram=result[lenres-order:]
	
	return result

gramify()