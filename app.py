# Todo app Python3
# library used : tkinter and pickle
# created : 5/08/2021
# twitter : Code Tech -> @ayanupadhaya96

from tkinter import*
from tkinter import messagebox as ms
import pickle

root = Tk()
root.title('Todo list @Code Tech')
root.geometry('300x350')

def add_task():
	task = entry_task.get()

	if task != "":
		list_box.insert(END,task)
		entry_task.delete(0,END)
	else:
		ms.showwarning(title="Warning!",message="You must enter a task")

def delete_task():
	try:
		task_index = list_box.curselection()[0]
		list_box.delete(task_index)

	except:
		ms.showwarning(title='Warning',message="You must select task to delete")

def load_tasks():
	list_box.delete(0,END)
	try:
		tasks = pickle.load(open('tasks.dat','rb'))
		for task in tasks:
			list_box.insert(END,task)
	except:
		ms.showwarning(title="Warning",message="Cannot find task file")

def save_task():
	tasks = list_box.get(0,list_box.size())
	pickle.dump(tasks,open('tasks.dat','wb'))


# Create Gui

frame_task = Frame(root)
frame_task.pack(fill="both")

#scrollbar
scrollbar_task = Scrollbar(frame_task,orient='vertical')
scrollbar_task.pack(side = RIGHT,fill =Y)  

#list box
list_box = Listbox(frame_task,height=10,width=50)
list_box.pack(expand=1,fill="both")

#entry widget
entry_task = Entry(root,width = 50)
entry_task.pack()

#buttons

button_add_task= Button(root,text="Add Task",width=48,command=add_task)
button_add_task.pack()

button_delete_task= Button(root,text="Delete Task",width=48,command=delete_task)
button_delete_task.pack()

button_load_tasks= Button(root,text="Load Tasks",width=48,command=load_tasks)
button_load_tasks.pack()

button_save_tasks= Button(root,text="Save Tasks",width=48,command=save_task)
button_save_tasks.pack()

#configurations

list_box.configure(bg='white',fg='black')
list_box.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=list_box.yview)

entry_task.configure(bg='white',fg='black')
root.configure(bg="#a4a6a6")

root.mainloop()


