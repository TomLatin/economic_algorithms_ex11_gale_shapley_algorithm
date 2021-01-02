import tkinter as tk
from tkinter import font as tkfont, filedialog

from gale_and_shapley_algorithm import init_dicts, activate_all_func


class  SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="student.ico")
        tk.Tk.wm_title(self, "Gale&Shapley Algorithm")
        self.geometry("400x200")
        self.title_font = tkfont.Font(family='Times', size=18, weight="bold", slant="italic")
        def file_dialog():
            global name_file
            name_file = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))

        # Create Text Box
        add_file = tk.Button(self, text="Brows A File", command=lambda: file_dialog())
        add_file.grid(row=2, column=1, pady=20, padx=10)

        # Creat Text Box Labels
        add_file_label = tk.Label(self, text="Open A File:")
        add_file_label.grid(row=2, column=0, pady=20, padx=10)

        # Creat Submit Button
        submit_btn = tk.Button(self, text="Submit",command=lambda: [init_dicts(name_file),activate_all_func()])
        submit_btn.grid(row=10, column=0, columnspan=2, pady=50, padx=40, ipadx=100)

if __name__ == "__main__":
    main = SampleApp()
    main.mainloop()