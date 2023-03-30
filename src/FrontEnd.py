import customtkinter as tk
import platform

class taskClass(tk.CTkFrame):
    def __init__(self, master, title = "", **kwargs):
        super().__init__(master, **kwargs)
        self.tempFont = tk.CTkFont(family="Calibri", size=18)
        self.textBox = tk.CTkTextbox(self, height=100,font=self.tempFont)
        self.textBox.grid(row = 0, column = 0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # set text
        self.textBox.insert("0.0", title)
        self.textBox.configure(state="disabled",wrap="word")
        self.leftLabel = tk.CTkLabel(self, text="Temp Date Label",padx=10)
        self.leftLabel.grid(row = 1, column=0,sticky="w")
        self.rightLabel = tk.CTkLabel(self, text="priority label",padx=10)
        self.rightLabel.grid(row = 1, column=0,sticky="e")

class ToplevelTaskForm(tk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.resizable(False,False)
        self.title("Bug Form")
        self.userTitle = tk.CTkTextbox(self)

        # form frame
        self.formFrame = tk.CTkFrame(self)
        self.formFrame.pack()

        # Priority
        self.priorityLabel = tk.CTkLabel(self.formFrame, text="Select Priority")
        self.priorityLabel.grid(row=0,column=0)
        self.priorityComboBox = tk.CTkComboBox(self.formFrame,values=["Low", "Medium", "High"])
        self.priorityComboBox.grid(row=0, column=1)

        # Date
        self.dateLabel = tk.CTkLabel(self.formFrame, text="Date")
        self.dateLabel.grid(row=1,column=0)
        self.dateEntry = tk.CTkEntry(self.formFrame,placeholder_text="")
        self.dateEntry.grid(row=1,column=1)

        # Description
        self.descriptionTextBox = tk.CTkTextbox(self)
        self.descriptionTextBox.pack()

        # Button
        self.confirmButton = tk.CTkButton(self, text="Confirm", command=self.confirmFunc)
        self.confirmButton.pack()

    def confirmFunc(self):
        pass




class app(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bug Tracker")
        self.popUpForm = None

        #linux config
        self.host = platform.system()
        if self.host == "Linux":
            self.attributes('-type', 'dialog')

        #four scrollable frames
        self.openContainerFrame = tk.CTkFrame(self)
        self.openContainerFrame.grid(row=0,column=0, sticky = "nesw", padx = 15, pady=15)
        self.openFrame = tk.CTkScrollableFrame(self.openContainerFrame,label_text="Open")
        self.openFrame.grid(row=0,column=0, sticky = "nesw")
        self.progressFrame = tk.CTkScrollableFrame(self,label_text="In Progress")
        self.progressFrame.grid(row=0,column=1, sticky = "nesw", padx = 15, pady=15)
        self.reviewFrame = tk.CTkScrollableFrame(self,label_text="Ready For Review")
        self.reviewFrame.grid(row=0,column=2, sticky = "nesw", padx = 15, pady=15)
        self.completedFrame= tk.CTkScrollableFrame(self,label_text="Complete")
        self.completedFrame.grid(row=0,column=3,sticky="nesw", padx = 15, pady=15)

        # Button
        self.addTaskButton =tk.CTkButton(master=self.openContainerFrame, text="Add Task", command=self.createTask)
        self.addTaskButton.grid(row=1,column=0, sticky="nesw",pady=15, padx=15)

        # Weight for the scrollable frames
        for x in range(4):
            self.columnconfigure(x, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.openContainerFrame.columnconfigure(0, weight=1)
        self.openContainerFrame.grid_rowconfigure(0, weight=1)

        self.testList = []
    def createTask(self):
        self.testList.append(taskClass(master=self.openFrame,title="Bug: Every time I Press add task button, popup is not taking focus"))
        self.testList[-1].grid(sticky="ew",padx=10,pady=5)
        self.openFrame.columnconfigure(0,weight=1)
        if self.popUpForm is None or not self.popUpForm.winfo_exists():
            self.popUpForm = ToplevelTaskForm(self)  # create window if its None or destroyed
            self.popUpForm.grab_set()
        else:
            self.popUpForm.focus()  # if window exists focus it

if __name__ == "__main__":
    tk.set_appearance_mode("dark")
    app = app()
    app.geometry("1200x600")
    app.mainloop()
