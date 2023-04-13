import platform
import datetime
import customtkinter as tk
from PIL import Image
import roughDraft
'''Check date and return if date is valid'''


def date_checker(date):
    try:
        datetime.datetime.strptime(date, '%m/%d/%y')
        return True
    except ValueError:
        return False


'''When clicked on the Task, popup more information about task'''


class ViewTask(tk.CTkToplevel):
    def __init__(self, item_id="", data_obj=tk, main_obj=tk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        # self.resizable(False,False)
        self.all_data = roughDraft.get_value(item_id)
        self.title("Data")
        self.item_id = item_id
        self.data_obj = data_obj
        self.main_obj = main_obj

        # form Frame
        self.form_frame_top = tk.CTkFrame(self)
        self.form_frame_top.pack(padx=10, pady=10)
        self.form_frame_bottom = tk.CTkFrame(self)
        self.form_frame_bottom.pack(padx=10, pady=10)
        self.button_frame = tk.CTkFrame(self)
        self.button_frame.pack(padx=10, pady=10)

        # Title
        self.user_title_label = tk.CTkLabel(self.form_frame_top, text="Title")
        self.user_title_label.grid(row=0, column=0)
        self.user_title_text_box = tk.CTkTextbox(
            self.form_frame_top, height=80)
        self.user_title_text_box.configure(wrap="word")
        self.user_title_text_box.grid(row=0, column=1, padx=10, pady=10)
        self.user_title_text_box.insert("0.0", self.all_data[0])
        self.user_title_text_box.configure(state="disabled")

        # Description
        self.description_label = tk.CTkLabel(
            self.form_frame_top, text="Description")
        self.description_label.grid(row=1, column=0, padx=10)
        self.description_text_box = tk.CTkTextbox(
            self.form_frame_top, height=150)
        self.description_text_box.configure(wrap="word")
        self.description_text_box.grid(row=1, column=1, padx=10, pady=10)
        self.description_text_box.insert("0.0", self.all_data[1])
        self.description_text_box.configure(state="disabled")

        # Priority
        self.priority_label = tk.CTkLabel(
            self.form_frame_bottom, text="Select Priority")
        self.priority_label.grid(row=0, column=0)
        self.priority_entry = tk.CTkEntry(self.form_frame_bottom)
        self.priority_entry.insert(0, self.all_data[3])
        self.priority_entry.configure(state="disabled")
        self.priority_entry.grid(row=0, column=1, padx=10, pady=10)

        # Date
        self.date_label = tk.CTkLabel(self.form_frame_bottom, text="Date")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.CTkEntry(
            self.form_frame_bottom,
            placeholder_text=datetime.date.today().strftime("%m/%d/%y"))
        self.date_entry.insert(0, self.all_data[2])
        self.date_entry.configure(state="disabled")
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button
        self.left_button = tk.CTkButton(
            self.button_frame,
            text="Move Left",
            command=self.move_left)
        self.right_button = tk.CTkButton(
            self.button_frame,
            text="Move right",
            command=self.move_right)
        self.delete_button = tk.CTkButton(
            self.button_frame,
            text="Delete",
            command=self.delete_data)
        self.edit_button = tk.CTkButton(self.button_frame,
                                        text="edit", command=self.edit_data)
        self.save_button = tk.CTkButton(self.button_frame,
                                        text="Save", command=self.save_data)
        self.left_button.grid(row=0, column=0, padx=10, pady=10)
        self.right_button.grid(row=0, column=1, padx=10, pady=10)
        self.delete_button.grid(row=1, column=0, padx=10, pady=10)
        self.edit_button.grid(row=1, column=1, padx=10, pady=10)
    '''Get all user input and check it, if passed, save data and change it in the gui'''

    def save_data(self):
        # get data
        self.data_title = self.user_title_text_box.get("1.0", "end-1c")
        self.data_description = self.description_text_box.get("1.0", "end-1c")
        self.data_priority = self.priority_combo_box.get()
        self.data_date = self.date_entry.get()

        # Error Checking
        self.color = self.priority_label.cget("text_color")
        self.user_title_label.configure(text_color=self.color)
        self.description_label.configure(text_color=self.color)
        self.date_label.configure(text_color=self.color)
        self.failed = False
        if len(self.data_title) == 0:
            self.user_title_label.configure(text_color="red")
            self.failed = True
        if len(self.data_description) == 0:
            self.description_label.configure(text_color="red")
            self.failed = True
        if (not (len(self.data_date) == 0) and not date_checker(self.data_date)):
            self.date_label.configure(text_color="red")
            self.failed = True
        if self.failed:
            return

        if (len(self.data_date) == 0):
            self.data_date = self.date_entry.cget("placeholder_text")
        else:
            self.data_date = datetime.datetime.strptime(
                self.data_date, '%m/%d/%y').strftime("%m/%d/%y")
        # create Task Frame
        roughDraft.edit_values(self.item_id,
                               [self.data_title,
                                self.data_description,
                                self.data_date,
                                self.data_priority,
                                self.all_data[4]])
        self.data_obj.text_box.configure(state="normal")
        self.data_obj.text_box.delete("0.0", "end")
        self.data_obj.text_box.insert("0.0", self.data_title)
        self.data_obj.text_box.configure(state="disabled")
        self.data_obj.left_label.configure(text=self.data_date)
        self.data_obj.right_label.configure(text=self.data_priority)
        if (self.data_priority == "Low"):
            self.data_obj.right_label.configure(
                text_color=("green", "light green"))
        if (self.data_priority == "Medium"):
            self.data_obj.right_label.configure(
                text_color=("orange", "orange"))
        if (self.data_priority == "High"):
            self.data_obj.right_label.configure(text_color=("red", "red"))
        # close popup
        # close popup
        self.destroy()

    '''Edit data in popup'''

    def edit_data(self):
        # make everything editable
        self.user_title_text_box.configure(state="normal")
        self.description_text_box.configure(state="normal")
        self.date_entry.configure(state="normal")

        # replace priority with priority combobox
        self.priority_entry.grid_remove()
        self.priority_combo_box = tk.CTkComboBox(
            self.form_frame_bottom, values=[
                "Low", "Medium", "High"], state="readonly")
        self.priority_combo_box.set(self.priority_entry.get())
        self.priority_combo_box.grid(row=0, column=1, padx=10, pady=10)

        # remove button
        self.left_button.grid_remove()
        self.right_button.grid_remove()
        self.edit_button.grid_remove()

        # add save button
        self.save_button.grid(row=1, column=1, padx=10, pady=10)
    '''Move task frame to right'''

    def move_right(self):
        if (self.all_data[4] == 3):
            return
        if (self.all_data[4] == 0):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=1,
                frame_to_pass_to=self.main_obj.progress_frame)
        elif (self.all_data[4] == 1):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=2,
                frame_to_pass_to=self.main_obj.review_frame)
        elif (self.all_data[4] == 2):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=3,
                frame_to_pass_to=self.main_obj.completed_frame)
        self.destroy()
    '''Move task frame to left'''

    def move_left(self):
        if (self.all_data[4] == 0):
            return
        if (self.all_data[4] == 1):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=0,
                frame_to_pass_to=self.main_obj.open_frame)
        elif (self.all_data[4] == 2):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=1,
                frame_to_pass_to=self.main_obj.progress_frame)
        elif (self.all_data[4] == 3):
            self.create_task_frame(
                title=self.all_data[0],
                description=self.all_data[1],
                priority=self.all_data[3],
                date=self.all_data[2],
                position=2,
                frame_to_pass_to=self.main_obj.review_frame)
        self.destroy()

    '''Delete task frame and delete data in database'''

    def delete_data(self):
        roughDraft.deleter(self.item_id)
        self.data_obj.destroy()
        self.destroy()
    '''Create task frame'''

    def create_task_frame(
            self,
            title="",
            description="",
            priority="",
            date="",
            frame_to_pass_to=tk,
            position=-1):
        self.temp = TaskClass(
            frame_to_pass_to,
            title=title,
            description=description,
            priority=priority,
            date=date,
            position=position,
            main_obj=self.main_obj,
            add_to_database=True)
        self.temp.grid(sticky="ew", padx=10, pady=5)
        frame_to_pass_to.columnconfigure(0, weight=1)
        roughDraft.deleter(self.item_id)
        self.data_obj.destroy()


'''Display/Create task on gui'''


class TaskClass(tk.CTkFrame):
    def __init__(
            self,
            master,
            title="",
            description="",
            priority="",
            date="",
            position=-1,
            main_obj=tk,
            add_to_database=False,
            item_id="",
            **kwargs):
        super().__init__(master, **kwargs)

        self.main_obj = main_obj
        self.add_to_database = add_to_database
        # self.configure(fg_color=("#333333", "#333333"),
        # border_color=("#333333", "#3333333"))

        self.temp_font = tk.CTkFont(family="Calibri", size=18)
        self.text_box = tk.CTkTextbox(self, height=100, font=self.temp_font)
        self.text_box.grid(row=0, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # set text
        self.text_box.insert("0.0", title)
        self.text_box.configure(state="disabled", wrap="word")
        self.left_label = tk.CTkLabel(self, text=date, padx=10)
        self.left_label.grid(row=1, column=0, sticky="w")
        self.right_label = tk.CTkLabel(self, text=priority, padx=10)
        self.right_label.grid(row=1, column=0, sticky="e")

        if self.add_to_database:
            self.item_id = roughDraft.storage(
                title, description, date, priority, position)
        else:
            self.item_id = item_id

        if (priority == "Low"):
            self.right_label.configure(text_color=("green", "light green"))
        if (priority == "Medium"):
            self.right_label.configure(text_color=("orange", "orange"))
        if (priority == "High"):
            self.right_label.configure(text_color=("red", "red"))

        # Making it clickable
        self.bind("<Button-1>", self.left_click)
        self.text_box.bind("<Button-1>", self.left_click)
        self.left_label.bind("<Button-1>", self.left_click)
        self.right_label.bind("<Button-1>", self.left_click)
        '''When user click on task frame, create a popup'''

    def left_click(self, event):
        self.popup_data = ViewTask(self.item_id, self, main_obj=self.main_obj)
        self.popup_data.attributes('-topmost', True)
        self.popup_data.grab_set()


'''Popup for user to input data'''


class ToplevelTaskForm(tk.CTkToplevel):
    def __init__(self, frame=tk, list_data=[], main_obj=tk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        # self.resizable(False,False)
        self.title("Bug Form")
        self.frame = frame
        self.list_data = list_data
        self.main_obj = main_obj

        # form Frame
        self.form_frame_top = tk.CTkFrame(self)
        self.form_frame_top.pack(padx=10, pady=10)
        self.form_frame_bottom = tk.CTkFrame(self)
        self.form_frame_bottom.pack(padx=10, pady=10)

        # Title
        self.user_title_label = tk.CTkLabel(self.form_frame_top, text="Title")
        self.user_title_label.grid(row=0, column=0,)
        self.user_title_text_box = tk.CTkTextbox(
            self.form_frame_top, height=80)
        self.user_title_text_box.configure(wrap="word")
        self.user_title_text_box.grid(row=0, column=1, padx=10, pady=10)

        # Description
        self.description_label = tk.CTkLabel(
            self.form_frame_top, text="Description")
        self.description_label.grid(row=1, column=0, padx=10)
        self.description_text_box = tk.CTkTextbox(
            self.form_frame_top, height=150)
        self.description_text_box.configure(wrap="word")
        self.description_text_box.grid(row=1, column=1, padx=10, pady=10)

        # Priority
        self.priority_label = tk.CTkLabel(
            self.form_frame_bottom, text="Select Priority")
        self.priority_label.grid(row=0, column=0)
        self.priority_combo_box = tk.CTkComboBox(
            self.form_frame_bottom, values=[
                "Low", "Medium", "High"], state="readonly")
        self.priority_combo_box.set("Low")
        self.priority_combo_box.grid(row=0, column=1, padx=10, pady=10)

        # Date
        self.date_label = tk.CTkLabel(self.form_frame_bottom, text="Date")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.CTkEntry(
            self.form_frame_bottom,
            placeholder_text=datetime.date.today().strftime("%m/%d/%y"))
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button
        self.confirm_button = tk.CTkButton(
            self, text="Confirm", command=self.confirm_func)
        self.confirm_button.pack(padx=10, pady=10)
    '''get and check all user data, if passed, save to database, create task frame, and close popup'''

    def confirm_func(self):
        # get data
        self.data_title = self.user_title_text_box.get("1.0", "end-1c")
        self.data_description = self.description_text_box.get("1.0", "end-1c")
        self.data_priority = self.priority_combo_box.get()
        self.data_date = self.date_entry.get()

        # Error Checking
        self.color = self.priority_label.cget("text_color")
        self.user_title_label.configure(text_color=self.color)
        self.description_label.configure(text_color=self.color)
        self.date_label.configure(text_color=self.color)
        self.failed = False
        if (len(self.data_title) == 0):
            self.user_title_label.configure(text_color="red")
            self.failed = True
        if (len(self.data_description) == 0):
            self.description_label.configure(text_color="red")
            self.failed = True
        if (not (len(self.data_date) == 0) and not date_checker(self.data_date)):
            self.date_label.configure(text_color="red")
            self.failed = True
        if self.failed:
            return

        if (len(self.data_date) == 0):
            self.data_date = self.date_entry.cget("placeholder_text")
        else:
            self.data_date = datetime.datetime.strptime(
                self.data_date, '%m/%d/%y').strftime("%m/%d/%y")
        # create Task Frame
        self.create_task_frame(
            title=self.data_title,
            description=self.data_description,
            date=self.data_date,
            priority=self.data_priority,
            frame_to_pass_to=self.frame)
        # close popup
        self.destroy()

    '''Create Task Frame Func'''

    def create_task_frame(
            self,
            title="",
            description="",
            priority="",
            date="",
            frame_to_pass_to=tk):
        self.list_data.append(
            TaskClass(
                frame_to_pass_to,
                title=title,
                description=description,
                priority=priority,
                date=date,
                position=0,
                main_obj=self.main_obj,
                add_to_database=True))
        self.list_data[-1].grid(sticky="ew", padx=10, pady=5)
        frame_to_pass_to.columnconfigure(0, weight=1)


'''Main gui that holds everything'''


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        # add data
        roughDraft.file_checker()

        self.title("Bug Tracker")
        self.pop_up_form = None

        # linux config
        self.host = platform.system()
        if self.host == "Linux":
            self.attributes('-type', 'dialog')
        self.frame = tk.CTkFrame(self)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky="nesw")
        self.tab_view = tk.CTkTabview(self.frame)
        self.tab_view.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.tab_view.add("Tracker")
        self.tab_view.add("Settings")
        # four scrollable frames
        self.open_container_frame = tk.CTkFrame(self.tab_view.tab("Tracker"))
        self.open_container_frame.grid(
            row=0, column=0, sticky="nesw", padx=15, pady=15)
        self.open_frame = tk.CTkScrollableFrame(
            self.open_container_frame, label_text="Open")
        self.open_frame.grid(row=0, column=0, sticky="nesw", padx=15, pady=15)
        self.open_container_frame.columnconfigure(0, weight=1)
        self.open_container_frame.grid_rowconfigure(0, weight=1)
        self.open_frame.configure(
            label_fg_color="#3194F0",
            label_text_color="white")

        self.progress_container_frame = tk.CTkFrame(
            self.tab_view.tab("Tracker"))
        self.progress_container_frame.grid(
            row=0, column=1, sticky="nesw", padx=15, pady=15)
        self.progress_frame = tk.CTkScrollableFrame(
            self.progress_container_frame, label_text="In Progress")
        self.progress_frame.grid(
            row=0,
            column=0,
            sticky="nesw",
            padx=15,
            pady=15)
        self.progress_container_frame.columnconfigure(0, weight=1)
        self.progress_container_frame.grid_rowconfigure(0, weight=1)
        self.progress_frame.configure(
            label_fg_color="#20B963",
            label_text_color="white")

        self.review_container_frame = tk.CTkFrame(self.tab_view.tab("Tracker"))
        self.review_container_frame.grid(
            row=0, column=2, sticky="nesw", padx=15, pady=15)
        self.review_frame = tk.CTkScrollableFrame(
            self.review_container_frame, label_text="Ready For Review")
        self.review_frame.grid(
            row=0,
            column=0,
            sticky="nesw",
            padx=15,
            pady=15)
        self.review_container_frame.columnconfigure(0, weight=1)
        self.review_container_frame.grid_rowconfigure(0, weight=1)
        self.review_frame.configure(
            label_fg_color="#FB6123",
            label_text_color="white")

        self.complete_container_frame = tk.CTkFrame(
            self.tab_view.tab("Tracker"))
        self.complete_container_frame.grid(
            row=0, column=3, sticky="nesw", padx=15, pady=15)
        self.completed_frame = tk.CTkScrollableFrame(
            self.complete_container_frame, label_text="Complete")
        self.completed_frame.grid(
            row=0, column=0, sticky="nesw", padx=15, pady=15)
        self.complete_container_frame.columnconfigure(0, weight=1)
        self.complete_container_frame.grid_rowconfigure(0, weight=1)
        self.completed_frame.configure(
            label_fg_color="#768C90",
            label_text_color="white")

        # Button
        self.add_task_button = tk.CTkButton(
            master=self.open_container_frame,
            text="Add Task",
            command=self.create_task)
        self.add_task_button.grid(
            row=1, column=0, sticky="nesw", pady=15, padx=15)

        # Settings stuff
        self.setting_frame = tk.CTkFrame(self.tab_view.tab("Settings"))
        self.setting_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.theme_label = tk.CTkLabel(self.setting_frame, text="Light/Dark")
        self.theme_label.grid(row=0, column=0, padx=10, pady=10)
        self.theme_option_menu = tk.CTkOptionMenu(
            master=self.setting_frame, values=[
                "System Theme", "Light", "Dark"], command=self.theme_select)
        self.theme_option_menu.grid(row=0, column=1, padx=10, pady=10)
        self.color_label = tk.CTkLabel(self.setting_frame, text="Themes")
        self.color_label.grid(row=1, column=0)
        self.color_option_menu = tk.CTkOptionMenu(
            master=self.setting_frame,
            values=[
                "Blue",
                "Dark Blue",
                "Green",
                "Orange",
                "Pink",
                "Retro",
                "Violet",
                "Yellow"],
            command=self.color_select)
        self.color_option_menu.grid(row=1, column=1)
        # Color
        if roughDraft.getter()[0] == "src/orange.json":
            self.color_option_menu.set("Orange")
        elif roughDraft.getter()[0] == "src/pink.json":
            self.color_option_menu.set("Pink")
        elif roughDraft.getter()[0] == "src/retro.json":
            self.color_option_menu.set("Retro")
        elif roughDraft.getter()[0] == "src/violet.json":
            self.color_option_menu.set("Violet")
        elif roughDraft.getter()[0] == "src/yellow.json":
            self.color_option_menu.set("Yellow")
        elif roughDraft.getter()[0] == "blue":
            self.color_option_menu.set("Blue")
        elif roughDraft.getter()[0] == "dark-blue":
            self.color_option_menu.set("Dark Blue")
        elif roughDraft.getter()[0] == "green":
            self.color_option_menu.set("Green")
        if roughDraft.getter()[1] == "light":
            self.theme_option_menu.set("Light")
        elif roughDraft.getter()[1] == "dark":
            self.theme_option_menu.set("Dark")
        elif roughDraft.getter()[1] == "system":
            self.theme_option_menu.set("System Theme")

        # images
        self.fox_logo = tk.CTkImage(light_image=Image.open("src/logo.png"),
                                    dark_image=Image.open("src/logo.png"),
                                    size=(100, 100))
        self.image_label = tk.CTkLabel(
            self.setting_frame, image=self.fox_logo, text="")
        self.image_label.grid(row=2, column=0, padx=10, pady=10)
        self.fox_font = tk.CTkFont(family="Calibri", size=24)
        self.fox_label = tk.CTkLabel(
            self.setting_frame,
            text="FoxFile Inc.",
            font=self.fox_font)
        self.fox_label.grid(row=2, column=1)

        # Weight for the scrollable frames
        for x in range(4):
            self.tab_view.tab("Tracker").columnconfigure(x, weight=1)
            self.tab_view.tab("Tracker").grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # currently holding all the task frame in a list
        self.all_task_list = []
        self.startup_load_data()
    '''set color theme'''

    def color_select(self, color):
        if color == "Orange":
            roughDraft.setter("src/orange.json", roughDraft.getter()[1])
            tk.set_default_color_theme("src/orange.json")
        if color == "Pink":
            roughDraft.setter("src/pink.json", roughDraft.getter()[1])
            tk.set_default_color_theme("src/pink.json")
        if color == "Retro":
            roughDraft.setter("src/retro.json", roughDraft.getter()[1])
            tk.set_default_color_theme("src/retro.json")
        if color == "Violet":
            roughDraft.setter("src/violet.json", roughDraft.getter()[1])
            tk.set_default_color_theme("src/violet.json")
        if color == "Yellow":
            roughDraft.setter("src/yellow.json", roughDraft.getter()[1])
            tk.set_default_color_theme("src/yellow.json")
        if color == "Blue":
            roughDraft.setter("blue", roughDraft.getter()[1])
            tk.set_default_color_theme("blue")
        if color == "Dark Blue":
            roughDraft.setter("dark-blue", roughDraft.getter()[1])
            tk.set_default_color_theme("dark-blue")
        if color == "Green":
            roughDraft.setter("green", roughDraft.getter()[1])
            tk.set_default_color_theme("green")
        self.restart_popup = tk.CTkToplevel()
        self.restart_popup.grab_set()
        self.restart_label = tk.CTkLabel(
            self.restart_popup,
            text="restart to apply Color",
            padx=50,
            pady=50,
            font=self.fox_font)
        self.restart_label.pack()
        self.restart_button = tk.CTkButton(
            master=self.restart_popup,
            text="Restart",
            command=self.exit_func)
        self.restart_button.pack(padx=10, pady=20)
        self.restart_popup.protocol("WM_DELETE_WINDOW", self.exit_func)

    def exit_func(self):
        self.destroy()

    def theme_select(self, color):
        if color == "Dark":
            roughDraft.setter(roughDraft.getter()[0], "dark")
            tk.set_appearance_mode("dark")
        elif color == "Light":
            roughDraft.setter(roughDraft.getter()[0], "light")
            tk.set_appearance_mode("light")
        elif color == "System Theme":
            roughDraft.setter(roughDraft.getter()[0], "system")
            tk.set_appearance_mode("system")
    '''Create all frame from database for startup'''

    def startup_load_data(self):
        self.all_id = roughDraft.get_all_keys()
        print(self.all_id)
        for data in self.all_id:
            self.tempList = roughDraft.get_value(data)
            if (self.tempList[4] == 0):
                self.add_task_frame(
                    title=self.tempList[0],
                    description=self.tempList[1],
                    priority=self.tempList[3],
                    date=self.tempList[2],
                    position=self.tempList[4],
                    frame_to_pass_to=self.open_frame,
                    item_id=data)
            elif (self.tempList[4] == 1):
                self.add_task_frame(
                    title=self.tempList[0],
                    description=self.tempList[1],
                    priority=self.tempList[3],
                    date=self.tempList[2],
                    position=self.tempList[4],
                    frame_to_pass_to=self.progress_frame,
                    item_id=data)
            elif (self.tempList[4] == 2):
                self.add_task_frame(
                    title=self.tempList[0],
                    description=self.tempList[1],
                    priority=self.tempList[3],
                    date=self.tempList[2],
                    position=self.tempList[4],
                    frame_to_pass_to=self.review_frame,
                    item_id=data)
            elif (self.tempList[4] == 3):
                self.add_task_frame(
                    title=self.tempList[0],
                    description=self.tempList[1],
                    priority=self.tempList[3],
                    date=self.tempList[2],
                    position=self.tempList[4],
                    frame_to_pass_to=self.completed_frame,
                    item_id=data)
    '''Create task frame'''

    def create_task_frame(
            self,
            title="",
            description="",
            priority="",
            date="",
            frame_to_pass_to=tk,
            position=-1):
        self.all_task_list.append(
            TaskClass(
                frame_to_pass_to,
                title=title,
                description=description,
                priority=priority,
                date=date,
                position=position,
                main_obj=self,
                add_to_database=True))
        self.all_task_list[-1].grid(sticky="ew", padx=10, pady=5)
        frame_to_pass_to.columnconfigure(0, weight=1)

    '''add task frame'''

    def add_task_frame(
            self,
            title="",
            description="",
            priority="",
            date="",
            frame_to_pass_to=tk,
            position=-1,
            item_id=""):
        self.all_task_list.append(
            TaskClass(
                frame_to_pass_to,
                title=title,
                description=description,
                priority=priority,
                date=date,
                position=position,
                main_obj=self,
                item_id=item_id))
        self.all_task_list[-1].grid(sticky="ew", padx=10, pady=5)
        frame_to_pass_to.columnconfigure(0, weight=1)

    '''Popup for add task'''

    def create_task(self):
        if self.pop_up_form is None or not self.pop_up_form.winfo_exists():
            self.pop_up_form = ToplevelTaskForm(
                frame=self.open_frame,
                list_data=self.all_task_list,
                main_obj=self)  # create window if its None or destroyed
            self.pop_up_form.attributes('-topmost', True)
            self.pop_up_form.grab_set()
        else:
            self.pop_up_form.focus()  # if window exists focus it


if __name__ == "__main__":
    roughDraft.ofile_checker()
    print(roughDraft.getter()[0])
    print(roughDraft.getter()[1])
    tk.set_appearance_mode(roughDraft.getter()[1])
    tk.set_default_color_theme(roughDraft.getter()[0])
    App = App()
    App.geometry("1200x600")
    App.mainloop()
