import tkinter
import customtkinter as tk


class app(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bug Tracker")
        self.openContainerFrame = tk.CTkFrame(self)
        self.openContainerFrame.grid(row=0,column=0, sticky = "nesw", padx = 15, pady=15)
        self.openFrame = tk.CTkScrollableFrame(self.openContainerFrame,label_text="Open")
        self.openFrame.grid(row=0,column=0, sticky = "nesw")
        #self.openFrame = tk.CTkScrollableFrame(self,label_text="Open")
        #self.openFrame.grid(row=0,column=0, sticky = "nesw", padx = 15, pady=15)
        self.progressFrame = tk.CTkScrollableFrame(self,label_text="In Progress")
        self.progressFrame.grid(row=0,column=1, sticky = "nesw", padx = 15, pady=15)
        self.reviewFrame = tk.CTkScrollableFrame(self,label_text="Ready For Review")
        self.reviewFrame.grid(row=0,column=2, sticky = "nesw", padx = 15, pady=15)
        self.completedFrame= tk.CTkScrollableFrame(self,label_text="Complete")
        self.completedFrame.grid(row=0,column=3,sticky="nesw", padx = 15, pady=15)




        for x in range(4):
            self.columnconfigure(x, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.openContainerFrame.columnconfigure(0, weight=1)
        self.openContainerFrame.grid_rowconfigure(0, weight=1)
    


if __name__ == "__main__":
    tk.set_appearance_mode("dark")
    app = app()
    app.mainloop()