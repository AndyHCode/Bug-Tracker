import customtkinter as tk
import platform
import datetime

class taskClass(tk.CTkFrame):
    def __init__(self, master, title = "", description="", priority="", date="", **kwargs):
        super().__init__(master, **kwargs)
        self.tempFont = tk.CTkFont(family="Calibri", size=18)
        self.textBox = tk.CTkTextbox(self, height=100,font=self.tempFont)
        self.textBox.grid(row = 0, column = 0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # set text
        self.textBox.insert("0.0", title)
        self.textBox.configure(state="disabled",wrap="word")
        self.leftLabel = tk.CTkLabel(self, text=date,padx=10)
        self.leftLabel.grid(row = 1, column=0,sticky="w")
        self.rightLabel = tk.CTkLabel(self, text=priority,padx=10)
        self.rightLabel.grid(row = 1, column=0,sticky="e")

class ToplevelTaskForm(tk.CTkToplevel):
    def __init__(self, frame=tk, listData=[] ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        # self.resizable(False,False)
        self.title("Bug Form")
        self.frame = frame
        self.listData = listData

        #form Frame
        self.formFrameTop = tk.CTkFrame(self)
        self.formFrameTop.pack(padx=10, pady=10)
        self.formFrameBottom = tk.CTkFrame(self)
        self.formFrameBottom.pack(padx=10,pady=10)

        # Title
        self.userTitleLabel = tk.CTkLabel(self.formFrameTop, text="Title")
        self.userTitleLabel.grid(row=0, column=0,)
        self.userTitleTextBox = tk.CTkTextbox(self.formFrameTop, height=80)
        self.userTitleTextBox.configure(wrap="word")
        self.userTitleTextBox.grid(row=0, column=1, padx=10, pady=10)

        # Description
        self.descriptionLabel = tk.CTkLabel(self.formFrameTop, text="Description")
        self.descriptionLabel.grid(row=1, column=0, padx=10)
        self.descriptionTextBox = tk.CTkTextbox(self.formFrameTop, height=150)
        self.descriptionTextBox.configure(wrap="word")
        self.descriptionTextBox.grid(row=1, column=1, padx=10, pady=10)

        # Priority
        self.priorityLabel = tk.CTkLabel(self.formFrameBottom, text="Select Priority")
        self.priorityLabel.grid(row=0,column=0)
        self.priorityComboBox = tk.CTkComboBox(self.formFrameBottom, values=["Low", "Medium", "High"], state="readonly")
        self.priorityComboBox.set("Low")
        self.priorityComboBox.grid(row=0, column=1,padx=10,pady=10)

        # Date
        self.dateLabel = tk.CTkLabel(self.formFrameBottom, text="Date")
        self.dateLabel.grid(row=1,column=0)
        self.dateEntry = tk.CTkEntry(self.formFrameBottom, placeholder_text="")
        self.dateEntry.grid(row=1,column=1,padx=10, pady=10)

        # Button
        self.confirmButton = tk.CTkButton(self, text="Confirm", command=self.confirmFunc)
        self.confirmButton.pack(padx=10, pady=10)

    def confirmFunc(self):
        #get data
        self.dataTitle = self.userTitleTextBox.get("1.0", "end-1c")
        self.dataDescription = self.descriptionTextBox.get("1.0","end-1c")
        self.dataPriority = self.priorityComboBox.get()
        self.dataDate = self.dateEntry.get()

        # Error Checking
        self.color = self.priorityLabel.cget("text_color")
        self.userTitleLabel.configure(text_color=self.color)
        self.descriptionLabel.configure(text_color=self.color)
        self.dateLabel.configure(text_color=self.color)
        self.failed = False
        if(len(self.dataTitle) == 0):
            self.userTitleLabel.configure(text_color="red")
            self.failed = True
        if(len(self.dataDescription) == 0):
            self.descriptionLabel.configure(text_color="red")
            self.failed = True
        if(len(self.dataDate) == 0):
            self.dateLabel.configure(text_color="red")
            self.failed = True
        if self.failed:
            return

        # create Task Frame
        self.createTaskFrame(title=self.dataTitle, description=self.dataDescription,date=self.dataDate, priority=self.dataPriority, frameToPassTo=self.frame)
        # close popup
        self.destroy()

    #Create Task Frame Func
    def createTaskFrame(self, title="", description="", priority="", date="", frameToPassTo=tk):
        self.listData.append(taskClass(frameToPassTo, title=title, description=description, priority=priority, date=date))
        self.listData[-1].grid(sticky="ew",padx=10,pady=5)
        frameToPassTo.columnconfigure(0,weight=1)
        


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

        #currently holding all the task frame in a list
        self.testList = []

    def createTask(self):
        # self.testList.append(taskClass(master=self.openFrame,title="Bug: Every time I Press add task button, popup is not taking focus"))
        # self.testList[-1].grid(sticky="ew",padx=10,pady=5)
        # self.openFrame.columnconfigure(0,weight=1)
        if self.popUpForm is None or not self.popUpForm.winfo_exists():
            self.popUpForm = ToplevelTaskForm(frame=self.openFrame, listData=self.testList)  # create window if its None or destroyed
            self.popUpForm.grab_set()
        else:
            self.popUpForm.focus()  # if window exists focus it

if __name__ == "__main__":
    tk.set_appearance_mode("dark")
    app = app()
    app.geometry("1200x600")
    app.mainloop()
