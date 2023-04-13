import tkinter as tk
from tkinter import ttk
from backend import *
import datetime
def value_checker_func(value=""):
    '''check for special char, return false if there is, return true if is'''
    if len(value) == 0:
        return False
    for x in value.lower():
        if not ((122 >= ord(x) >= 97) or (ord(x) == 32) or (57 >= ord(x) >= 48)):
            return False
    return True

def ssn_checker_func(ssn=""):
    '''Check if ssn have 9 digit and is numeric, return true if is, else return false'''
    if len(ssn) != 9:
        return False
    if not ssn.isnumeric():
        return False
    return True

def ssn_format_func(ssn):
    '''format ssn to have dashes and return it'''
    return ssn[0:3] + "-" + ssn[3:5] + "-" + ssn[5:]

def main():
    dx = reader()
    resetter(dx)
    '''Main func to make GUI, include some other functions'''
    def log_print_func(string_input=""):
        '''Print into log textbox given a string'''

        log_text_box.config(state="normal")
        log_text_box.insert(tk.END, string_input)
        log_text_box.config(state="disable")

    def log_clear_func():
        '''Clear log textbox'''
        log_text_box.config(state="normal")
        log_text_box.delete('1.0', tk.END)
        log_text_box.config(state="disable")

    def delete_index_func():
        '''Delete row at inputted index in gui'''
        log_print_func(current_time_func())
        index = delete_entry.get()
        temp_string = delete_row(index)
        if temp_string[0:5] == "Error":
            delete_error_label.config(text="Error", fg="red")
            log_print_func(temp_string + "\n")
            text_box_search.config(state="normal")
            text_box_search.delete('1.0', tk.END)
            text_box_search.insert(tk.END, temp_string)
            text_box_search.config(state="disable")
            return
        delete_error_label.config(text="Success", fg="green")
        log_print_func("Success Delete: \n" + temp_string + "\n")
        text_box_search.config(state="normal")
        text_box_search.delete('1.0', tk.END)
        text_box_search.insert(tk.END, "Deleted data:\n" + temp_string)
        text_box_search.config(state="disable")

    def button_func_input():
        '''input all entry from gui to database'''
        temp_list = [first_name_entry_input.get(), last_name_entry_input.get(), sex_entry_input.get(), email_entry_input.get(),
                    phone_numbers_entry_input.get(), ssn_entry_input.get()]
        log_print_func(current_time_func())
        for x in temp_list:
            if x == "":
                error_label_input.config(text="Error Missing Info", fg="red")
                log_print_func("failed insert, missing info: " + repr(temp_list) + "\n")
                return
        if not value_checker_func(temp_list[0]):
            error_label_input.config(text="Error First Name", fg="red")
            log_print_func("failed insert, First name error: " + repr(temp_list) + "\n")
            return
        if not value_checker_func(temp_list[1]):
            error_label_input.config(text="Error Last Name", fg="red")
            log_print_func("failed insert, Last name error: " + repr(temp_list) + "\n")
            return
        if not check_email(temp_list[3]):
            error_label_input.config(text="Error Email", fg="red")
            log_print_func("failed insert, email error: " + repr(temp_list) + "\n")
            return
        if not phone_number(temp_list[4]):
            error_label_input.config(text="Error Phone Number", fg="red")
            log_print_func("failed insert, phone number error: " + repr(temp_list) + "\n")
            return
        if not ssn_checker_func(temp_list[5]):
            error_label_input.config(text="Error ssn", fg="red")
            log_print_func("failed insert, ssn error: " + repr(temp_list) + "\n")
            return
        if not value_checker_func(temp_list[0]):
            temp_list[5] = ssn_format_func(temp_list[5])
        temp_user_id = adder(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5])
        error_label_input.config(text="Success", fg="Green")
        text_box_input.config(state="normal")
        text_box_input.delete('1.0', tk.END)
        text_box_input.insert(tk.END, search_engine("User ID", temp_user_id))
        text_box_input.config(state="disable")
        log_print_func("Success insert: " + repr(temp_list) + "\n")

    def button_func_search():
        '''search dataframe base on what inputted in gui'''
        text_box_search.config(state="normal")
        text_box_search.delete('1.0', tk.END)
        text_box_search.insert(tk.END, search_engine(select_entry_search.get(), input_entry_search.get()))
        text_box_search.config(state="disable")
        log_print_func(current_time_func() + "Searched Input: " + "[" + select_entry_search.get() + ": " + input_entry_search.get() + "]\n")
        log_print_func(search_engine(select_entry_search.get(), input_entry_search.get()) + "\n")
        delete_error_label.config(text="")

    #########################################################################################################
    def current_time_func():
        return datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + " | "

    #########################################################################################################
    program = tk.Tk()
    program.title("Data Storage App")

    tabs = ttk.Notebook(program)
    input_tab = tk.Frame(tabs)
    search_tab = tk.Frame(tabs)
    log_tab = tk.Frame(tabs)
    tabs.add(input_tab, text="Input")
    tabs.add(search_tab, text="Search")
    tabs.add(log_tab, text="Log")

    # User Input
    user_info_frame = tk.LabelFrame(input_tab, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=20)
    # All textbox to put in data for user input
    first_name_label_input = tk.Label(user_info_frame, text="First Name: ")
    first_name_label_input.grid(row=0, column=0)
    first_name_entry_input = tk.Entry(user_info_frame)
    first_name_entry_input.grid(row=0, column=1)
    last_name_label_input = tk.Label(user_info_frame, text="last Name: ")
    last_name_label_input.grid(row=1, column=0)
    last_name_entry_input = tk.Entry(user_info_frame)
    last_name_entry_input.grid(row=1, column=1)
    sex_label_input = tk.Label(user_info_frame, text="Sex: ")
    sex_label_input.grid(row=2, column=0)
    sex_entry_input = tk.Entry(user_info_frame)
    sex_entry_input.grid(row=2, column=1)
    email_label_input = tk.Label(user_info_frame, text="Email: ")
    email_label_input.grid(row=3, column=0)
    email_entry_input = tk.Entry(user_info_frame)
    email_entry_input.grid(row=3, column=1)
    phone_numbers_label_input = tk.Label(user_info_frame, text="Phone Number: ")
    phone_numbers_label_input.grid(row=4, column=0)
    phone_numbers_entry_input = tk.Entry(user_info_frame)
    phone_numbers_entry_input.grid(row=4, column=1)
    ssn_label_input = tk.Label(user_info_frame, text="SSN")
    ssn_label_input.grid(row=5, column=0)
    ssn_entry_input = tk.Entry(user_info_frame)
    ssn_entry_input.grid(row=5, column=1)

    error_label_input = tk.Label(user_info_frame, text="")
    error_label_input.grid(row=6, column=0)
    for x in user_info_frame.winfo_children():
        x.grid_configure(padx=10, pady=3)
        if x.__class__ == email_label_input.__class__:
            x.configure(bg="#333333", fg="white")
    add_button_input = tk.Button(user_info_frame, text="Enter", command=button_func_input, bg="#12505c", fg="white")
    add_button_input.grid(row=6, column=1, padx=10, pady=10)

    # A text box to display data input
    text_box_input = tk.Text(input_tab, width=120)
    text_box_input.grid(row=0, column=1, padx=20, pady=20)
    text_box_input.insert(tk.END, "Added data shows up here")
    text_box_input.config(state="disabled")
    text_box_input.configure(bg="#222222", fg="white")

    #######################################################################################################
    # Frame that will hold the search and delete frame
    search_box_frame = tk.Frame(search_tab)
    search_box_frame.grid(row=0, column=0, padx=20, pady=20)
    search_box_frame.configure(bg="#333333")
    # Search
    search_user_frame = tk.LabelFrame(search_box_frame, text="Search User Information")
    search_user_frame.grid(row=0, column=0, padx=20, pady=20)
    text_box_search = tk.Text(search_tab, width=120)
    drop_down_option = ["User ID", "First Name", "Last Name", "Sex", "Email", "Phone", "ssn"]
    # All textbox to put in data for user Search
    select_label_search = tk.Label(search_user_frame, text="Select Information: ")
    select_label_search.grid(row=0, column=0)
    select_entry_search = ttk.Combobox(search_user_frame, values=drop_down_option, state="readonly")
    select_entry_search.current(0)
    select_entry_search.grid(row=0, column=1)
    input_label_search = tk.Label(search_user_frame, text="Input: ")
    input_label_search.grid(row=1, column=0)
    input_entry_search = tk.Entry(search_user_frame)
    input_entry_search.grid(row=1, column=1)
    for x in search_user_frame.winfo_children():
        x.grid_configure(padx=10, pady=3)
        if x.__class__ == email_label_input.__class__:
            x.configure(bg="#333333", fg="white")
    add_button_frame = tk.Button(search_user_frame, text="Search", command=button_func_search, bg="#12505c", fg="white")
    add_button_frame.grid(row=2, column=1, padx=10, pady=10)

    # A text box to display data searched
    text_box_search.grid(row=0, column=1, padx=20, pady=20)
    text_box_search.insert(tk.END, "Searched/Deleted Data show up here")
    text_box_search.config(state="disabled")
    text_box_search.configure(bg="#222222", fg="white")
    ####################################################################################################
    delete_frame = tk.LabelFrame(search_box_frame, text="delete", pady=20, padx=20, bg="#333333", fg="white")
    delete_frame.grid(row=1, column=0)
    delete_label = tk.Label(delete_frame, text="Index: ", bg="#333333", fg="white")
    delete_label.grid(row=0, column=0)
    delete_entry = tk.Entry(delete_frame)
    delete_entry.grid(row=0, column=1)
    delete_button = tk.Button(delete_frame, text="Delete", command=delete_index_func, bg="#12505C", fg="white")
    delete_button.grid(row=1, column=1, padx=10, pady=10)
    delete_error_label = tk.Label(delete_frame,bg="#333333")
    delete_error_label.grid(row=1, column=0)
    ############################################################################################
    log_frame = tk.LabelFrame(log_tab, text="All Log Data", bg="#333333", fg="white")
    log_frame.grid(row=0, column=0, pady=20, padx=20)
    log_text_box = tk.Text(log_frame, padx=20, pady=20, bg="#222222", fg="white", width=160, height=15)
    log_text_box.grid(row=0, column=0, pady=20, padx=20)
    log_text_box.config(state="disable")
    log_clear_button = tk.Button(log_frame, text="Clear Logs", bg="#12505C", fg="white", command=log_clear_func)
    log_clear_button.grid(row=1, column=0, pady=10, padx=10)
    ############################################################################################

    # customized colors
    input_tab.configure(bg="#333333")
    search_tab.configure(bg="#333333")
    log_tab.configure(bg="#333333")

    user_info_frame.configure(bg="#333333", fg="white")
    search_user_frame.configure(bg="#333333", fg="white")

    tabs.pack(expand=True, fill="both")
    program.mainloop()


if __name__ == '__main__':
    main()
