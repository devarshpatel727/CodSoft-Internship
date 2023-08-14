import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("My todo list")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!", message="To add a task, please enter some task!!")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)

    except IndexError:
        tkinter.messagebox.showwarning(title="Attention!!", message="To delete a task, you must select a task")

def task_load():
    try:
        todo_list = pickle.load(open("tasks.dat", "rb"))
        todo_box.delete(0, tkinter.END)
        for todo in todo_list:
            todo_box.insert(tkinter.END, todo)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Attention!!", message="Cannot find tasks.dat")

def task_save():
    todo_list = todo_box.get(0, tkinter.END)
    pickle.dump(todo_list, open("tasks.dat", "wb"))

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=50)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=todo_box.yview)

task_add = tkinter.Entry(window, width=30, font=("Helvetica", 14))  # Increased text box height
task_add.pack(pady=10)  # Added some padding

add_task_button = tkinter.Button(window, text="Click to Add task", font=("arial", 20, "bold"), background="blue", width=20, command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="Click to Delete task", font=("arial", 20, "bold"), background="green", width=20, command=task_removing)
remove_task_button.pack()

load_task_button = tkinter.Button(window, text="Click to Load task", font=("arial", 20, "bold"), background="red", width=20, command=task_load)
load_task_button.pack()

save_task_button = tkinter.Button(window, text="Click to Save task", font=("arial", 20, "bold"), background="brown", width=20, command=task_save)
save_task_button.pack()

window.mainloop()
