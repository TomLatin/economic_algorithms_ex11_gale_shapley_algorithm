import os
import tkinter as tk
from tkinter import font as tkfont, filedialog

from gale_and_shapley_algorithm import init_dicts, activate_all_func, tentative_acceptance

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="student.ico")
        tk.Tk.wm_title(self, "Gale&Shapley Algorithm")
        self.geometry("500x500")
        self.title_font = tkfont.Font(family='Times', size=18, weight="bold", slant="italic")

        '''The method is responsible for importing the file'''
        def file_dialog():
            global name_file
            name_file = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))
            add_file.config(text=os.path.basename(name_file))
            """
            >>> name_file="dict.txt"
            'Answer\nryan- Yale\n blake- Harvard\njosh- MIT\nconnor- NYU\n'
            
            """

        '''The method is responsible for writing the answer on the GUI and after a few seconds close the GUI'''
        def print_ans_using_global():
            ans = "Answer: \n"
            for i in range(len(tentative_acceptance)):
                ans += str(tentative_acceptance[i]).replace("'", '').replace('[', '').replace(']', '').replace(',','-')+"\n"
            font_style = tkfont.Font(family="Lucida Grande", size=20)
            ans_label = tk.Label(self, text=ans, font=font_style)
            ans_label.grid(row=12, column=0, columnspan=2, pady=10, padx=40, ipadx=100)
            main.after(6000, main.destroy)  #close the GUI

        # Create Button
        add_file = tk.Button(self, text="Brows A File", command=lambda: file_dialog())
        add_file.grid(row=2, column=1, pady=20, padx=10,ipadx=50)

        # Creat Text Box Labels
        add_file_label = tk.Label(self, text="Open A File:")
        add_file_label.grid(row=2, column=0, pady=20, padx=10)

        # Creat Submit Button
        submit_btn = tk.Button(self, text="Submit",command=lambda: [init_dicts(name_file), activate_all_func(), print_ans_using_global()])
        submit_btn.grid(row=10, column=0, columnspan=2, pady=50, padx=40, ipadx=100)

if __name__ == "__main__":
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    #Run the GUI
    main = SampleApp()
    main.mainloop()