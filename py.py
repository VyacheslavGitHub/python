from tkinter import *
root = Tk()


def select_item(event):
	selected = list(listbox1.curselection())
	selected.reverse()
	for i in selected:
		listbox2.insert(END, listbox1.get(i))
		listbox1.delete(i)

def select_item_1(event):
	selected = list(listbox2.curselection())
	selected.reverse()
	for i in selected:
		listbox1.insert(END, listbox2.get(i))
		listbox2.delete(i)

listbox1 = Listbox(root, selectmode=EXTENDED)

items = ['a', 'b', 'c']
for item in items:
	listbox1.insert(END, item)


listbox2 = Listbox(
	root,
	)


but = Button(
	root,
	text='>>>',
	)

but_1 = Button(
	root,
	text='<<<')


but.bind('<Button-1>', select_item)
but_1.bind('<Button-1>', select_item_1)
listbox1.pack()
but.pack()
but_1.pack()
listbox2.pack()

root.mainloop()
