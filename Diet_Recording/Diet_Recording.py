import os
import csv
import tkinter as tk
from tkinter import messagebox

class HealthySystem:

    def __init__(self):
        self.BEE = None
        self.suggestedcarbo = None
        self.suggestedprotein = None
        self.suggestedfat = None
        self._login_window()
        self.login_window.mainloop()

    # Login system
    def _login_window(self):
        self.login_window = tk.Tk()
        self.login_window.title('Diet-tracking Program')
        self.login_window.geometry('400x285+400+100')
        self.login_window.resizable(False, False)
        title_label = tk.Label(master=self.login_window, text='Login', font=('Arial', 30), bg='#9eeea2')
        username_label = tk.Label(master=self.login_window, text='Username:', font=('Arial', 15))
        password_label = tk.Label(master=self.login_window, text='Password:', font=('Arial', 15))
        repassword_label = tk.Label(master=self.login_window, text='Re-Password:', font=('Arial', 15))
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.repassword = tk.StringVar()
        username_entry = tk.Entry(master=self.login_window, textvariable=self.username, font=('Arial', 15))
        password_entry = tk.Entry(master=self.login_window, textvariable=self.password, font=('Arial', 15))
        repassword_entry = tk.Entry(master=self.login_window, textvariable=self.repassword, font=('Arial', 15))
        title_label.place(x=0, y=0, width=400, height=60)
        username_label.place(x=50, y=90, width=100, height=30)
        password_label.place(x=50, y=130, width=100, height=30)
        repassword_label.place(x=10, y=170, width=150, height=30)
        username_entry.place(x=170, y=90, width=200, height=30)
        password_entry.place(x=170, y=130, width=200, height=30)
        repassword_entry.place(x=170, y=170, width=200, height=30)
        login_btn = tk.Button(master=self.login_window, text='Confirm', command=self.login, font=('Arial', 15))
        register_btn = tk.Button(master=self.login_window, text='Register', command=self.register, font=('Arial', 15))
        register_btn.place(x=50, y=220, width=100, height=35)
        login_btn.place(x=250, y=220, width=100, height=35)

    # Login system Error Message
    def login(self):
        username = self.username.get()
        password = self.password.get()
        repassword = self.repassword.get()
        username_list = [row['Username'] for row in self._read_csv(filename='User_information.csv')]
        password_list = [row['Password'] for row in self._read_csv(filename='User_information.csv')]
        if username not in username_list:
            messagebox.showerror(title='ERROR', message='User '+username+' is not found. Please REGISTER!!!')
            self.username.set('')
            self.password.set('')
            self.repassword.set('')
        elif password not in password_list:
            messagebox.showerror(title='ERROR', message='Your password is INCORRECT!!!')
            self.password.set('')
            self.repassword.set('')
        elif password != repassword:
            messagebox.showerror('ERROR', message='The password is different from the repassword. Please RE-ENTER!!!')
            self.password.set('')
            self.repassword.set('')
        else:
            self.login_window.destroy()
            self._main_window()

    # Register Page
    def register(self):
        self.register_window = tk.Toplevel(self.login_window)
        self.register_window.title('Diet-tracking Program')
        self.register_window.geometry('400x260+400+100')
        self.register_window.resizable(False, False)
        title_label = tk.Label(master=self.register_window, text='Setup', font=('Arial', 30), bg='#9eeea2')
        register_name_label = tk.Label(master=self.register_window, text='Username:', font=('Arial', 15))
        register_password_label = tk.Label(master=self.register_window, text='Password:', font=('Arial', 15))
        self.register_name = tk.StringVar()
        self.register_password = tk.StringVar()
        register_name_entry = tk.Entry(master=self.register_window, textvariable=self.register_name, font=('Arial', 15))
        register_password_entry = tk.Entry(master=self.register_window, textvariable=self.register_password, font=('Arial', 15))
        register_btn = tk.Button(master=self.register_window, text='Create', command=self.create_user, font=('Arial', 15))
        title_label.place(x=0, y=0, width=400, height=60)
        register_name_label.place(x=40, y=90, width=100, height=30)
        register_password_label.place(x=40, y=140, width=100, height=30)
        register_name_entry.place(x=130, y=90, width=200, height=30)
        register_password_entry.place(x=130, y=140, width=200, height=30)
        register_btn.place(x=150, y=200, width=100, height=30)

    # Personal information
    def _config_window(self):
        def my_trace(a, b, c):
            weight = eval(self.weight.get()) if self.weight.get()!='' else 0
            height = eval(self.height.get()) if self.height.get()!='' else 1
            new_text = weight /(height*height)
            self.BMI.set(new_text)
        self.config_window = tk.Toplevel(self.main_window)
        self.config_window.title('Diet-tracking Program')
        self.config_window.geometry('500x550+400+100')
        self.config_window.resizable(False, False)
        title_label = tk.Label(master=self.config_window, text='Personal Information', font=('Arial', 30), bg='#9eeea2')
        weight_label = tk.Label(master=self.config_window, text='Weight:', font=('Arial', 15))
        kg_label = tk.Label(master=self.config_window, text='kg', font=('Arial', 15))
        heiht_label = tk.Label(master=self.config_window, text='Height:', font=('Arial', 15))
        m_label = tk.Label(master=self.config_window, text='m', font=('Arial', 15))
        BMI_label = tk.Label(master=self.config_window, text='BMI:', font=('Arial', 15))
        Age_label = tk.Label(master=self.config_window, text='Age:', font=('Arial', 15))
        Gender_label = tk.Label(master=self.config_window, text='Gender:', font=('Arial', 15))
        Job_label = tk.Label(master=self.config_window, text='Job:', font=('Arial', 15))
        ask_label = tk.Label(master=self.config_window, text='Do you get exercised? Yes or No?', font=('Arial', 15))
        self.weight= tk.StringVar()
        self.height = tk.StringVar()
        self.BMI = tk.StringVar()
        self.Age = tk.StringVar()
        self.config_answer = tk.StringVar()
        weight_entry = tk.Entry(master=self.config_window, textvariable=self.weight, font=('Arial', 15))
        height_entry = tk.Entry(master=self.config_window, textvariable=self.height, font=('Arial', 15))
        self.weight.trace('w', my_trace)
        self.height.trace('w', my_trace)
        BMI_entry = tk.Entry(master=self.config_window, textvariable=self.BMI, font=('Arial', 15))
        Age_entry = tk.Entry(master=self.config_window, textvariable=self.Age, font=('Arial', 15))
        answer_entry = tk.Entry(master=self.config_window, textvariable=self.config_answer, font=('Arial', 15))
        confirm_btn = tk.Button(master=self.config_window, text='OK', command=self.config_confirm, font=('Arial', 15))
        title_label.place(x=0, y=0, width=500, height=100)
        weight_label.place(x=80, y=120, width=120, height=30)
        kg_label.place(x=420, y=120, width=30, height=30)
        heiht_label.place(x=80, y=170, width=120, height=30)
        m_label.place(x=420, y=170, width=30, height=30)
        BMI_label.place(x=80, y=220, width=120, height=30)
        Age_label.place(x=80, y=270, width=120, height=30)
        Gender_label.place(x=80, y=320, width=120, height=30)
        Job_label.place(x=80, y=370, width=120, height=30)
        ask_label.place(x=100, y=420, width=300, height=30)
        weight_entry.place(x=200, y=120, width=200, height=30)
        height_entry.place(x=200, y=170, width=200, height=30)
        BMI_entry.place(x=200, y=220, width=200, height=30)
        Age_entry.place(x=200, y=270, width=200, height=30)
        answer_entry.place(x=100, y=460, width=350, height=30)
        confirm_btn.place(x=225, y=500, width=50, height=30)
        self.var_gender = tk.StringVar()
        self.var_job = tk.StringVar()
        self.var_gender.set('0')
        self.var_job.set('0')
        male_check = tk.Radiobutton(master=self.config_window, text='Male', variable=self.var_gender, value='male', font=('Arial', 15))
        female_check = tk.Radiobutton(master=self.config_window, text='Female', variable=self.var_gender, value='female', font=('Arial', 15))
        student_check = tk.Radiobutton(master=self.config_window, text='Student', variable=self.var_job, value='student', font=('Arial', 15))
        teacher_check = tk.Radiobutton(master=self.config_window, text='Teacher', variable=self.var_job, value='teacher', font=('Arial', 15))
        student_check.place(x=200, y=370, width=100, height=30)
        teacher_check.place(x=320, y=370, width=100, height=30)
        male_check.place(x=200, y=320, width=100, height=30)
        female_check.place(x=320, y=320, width=100, height=30)
        for row in self._read_csv(filename='User_information.csv'):
            if row['Username'] == self.username.get():
                self.weight.set(row['Weight'] if row['Weight']!=None else '')
                self.height.set(row['Height'] if row['Height']!=None else '')
                self.BMI.set(row['BMI'] if row['BMI']!=None else '')
                self.Age.set(row['Age'] if row['Age']!=None else '')
                self.var_gender.set(row['Gender'] if row['Gender']!=None else '0')
                self.var_job.set(row['Job'] if row['Job']!=None else '0')
                self.config_answer.set(row['Exercise'] if row['Exercise']!=None else '')
                break

    # Home Page
    def _main_window(self):
        self.main_window = tk.Tk()
        self.main_window.title('Diet-tracking Program')
        self.main_window.geometry('450x280+300+200')
        self.main_window.resizable(False, False)
        title_label = tk.Label(master=self.main_window, text='Home Page', font=('Arial', 30), bg='#9eeea2')
        search_btn = tk.Button(master=self.main_window, text='Search Food', font=('Arial', 15), command=self.search)
        order_btn = tk.Button(master=self.main_window, text='Ordering', font=('Arial', 15), command=self.order)
        config_btn = tk.Button(master=self.main_window, text='Personal Info', font=('Arial', 12), command=self._config_window)
        title_label.place(x=0, y=0, width=450, height=70)
        search_btn.place(x=145, y=110, width=150, height=50)
        order_btn.place(x=145, y=190, width=150, height=50)
        config_btn.place(x=20, y=100, width=83, height=43)
        self.main_window.mainloop()

    # Create Account Page
    def create_user(self):
        fp = open(os.path.split(os.path.realpath(__file__))[0]+'//User_information.csv', 'a', encoding='utf-8', newline='')
        csvWriter = csv.DictWriter(fp, fieldnames=['Username', 'Password', 'Repassword'])
        csvWriter.writerow({'Username': self.register_name.get(), 'Password': self.register_password.get(), 'Repassword': self.register_password.get()})
        fp.close()
        self.username.set(self.register_name.get())
        self.password.set(self.register_password.get())
        self.repassword.set(self.register_password.get())
        self.register_window.destroy()
        self.login_window.destroy()
        self._main_window()

    # Food Searching
    def search(self):
        self.search_window = tk.Toplevel(self.main_window)
        self.search_window.title('Diet-tracking Program')
        self.search_window.geometry('450x250+300+200')
        self.search_window.resizable(False, False)
        title_label = tk.Label(master=self.search_window, text='Dining Searching', bg='#9eeea2', font=('Arial', 30))
        ask_label = tk.Label(master=self.search_window, text='Search the food you want to eat here:', font=('Arial', 15))
        self.var_search_food = tk.StringVar()
        answer_entry = tk.Entry(master=self.search_window, textvariable=self.var_search_food, font=('Arial', 15))
        search_btn = tk.Button(master=self.search_window, text='Search', font=('Arial', 15), command=self.food_detail)
        title_label.place(x=0, y=0, width=450, height=70)
        ask_label.place(x=40, y=90, width=360, height=50)
        answer_entry.place(x=70, y=140, width=300, height=30)
        search_btn.place(x=165, y=190, width=100, height=30)

    # Food_Menu Page
    def food_detail(self):
        def click():
            self.detail_window.destroy()
        for row in self._read_csv('Food_Menu.csv'):
            if row['name'] == self.var_search_food.get():
                self.detail_window = tk.Toplevel(self.search_window)
                self.detail_window.title('Diet-tracking Program')
                self.detail_window.geometry('380x350+350+200')
                self.detail_window.resizable(False, False)
                title_label = tk.Label(master=self.detail_window, text='Food Information', font=('Arial', 28), bg='#9eeea2')
                name_label = tk.Label(master=self.detail_window, text='Name:', font=('Arial', 15))
                floor_label = tk.Label(master=self.detail_window, text='Floor:', font=('Arial', 15))
                calories_label = tk.Label(master=self.detail_window, text='Calories:', font=('Arial', 15))
                protein_label = tk.Label(master=self.detail_window, text='Protein:', font=('Arial', 15))
                carbo_label = tk.Label(master=self.detail_window, text='Carbo:', font=('Arial', 15))
                fat_label = tk.Label(master=self.detail_window, text='Fat:', font=('Arial', 15))
                mass_label = tk.Label(master=self.detail_window, text='Mass:', font=('Arial', 15))
                name_value_label = tk.Label(master=self.detail_window, text=row['name'], font=('Arial', 15))
                floor_value_label = tk.Label(master=self.detail_window, text=row['floor'], font=('Arial', 15))
                calories_value_label = tk.Label(master=self.detail_window, text=row['calories'], font=('Arial', 15))
                protein_value_label = tk.Label(master=self.detail_window, text=row['protein'], font=('Arial', 15))
                carbo_value_label = tk.Label(master=self.detail_window, text=row['carbo'], font=('Arial', 15))
                fat_value_label = tk.Label(master=self.detail_window, text=row['fat'], font=('Arial', 15))
                mass_value_label = tk.Label(master=self.detail_window, text=row['mass'], font=('Arial', 15))
                back_btn = tk.Button(master=self.detail_window, text='Back', font=('Arial', 15), command=click)
                title_label.place(x=0, y=0, width=400, height=70)
                name_label.place(x=45, y=80, width=150, height=30)
                floor_label.place(x=45, y=110, width=150, height=30)
                calories_label.place(x=45, y=140, width=150, height=30)
                protein_label.place(x=45, y=170, width=150, height=30)
                carbo_label.place(x=45, y=200, width=150, height=30)
                fat_label.place(x=45, y=230, width=150, height=30)
                mass_label.place(x=73, y=260, width=100, height=30)
                name_value_label.place(x=175, y=80, width=150, height=35)
                floor_value_label.place(x=175, y=110, width=100, height=30)
                calories_value_label.place(x=175, y=140, width=100, height=30)
                protein_value_label.place(x=175, y=170, width=100, height=30)
                carbo_value_label.place(x=175, y=200, width=100, height=30)
                fat_value_label.place(x=175, y=230, width=100, height=30)
                mass_value_label.place(x=175, y=260, width=100, height=30)
                back_btn.place(x=150, y=300, width=70, height=32)

    # Ordering Page
    def order(self):
        self.order_window = tk.Toplevel(self.main_window)
        self.order_window.title('Diet-tracking Program')
        self.order_window.geometry('500x600+350+70')
        self.order_window.resizable(False, False)
        title_label = tk.Label(master=self.order_window, text='Ordering', font=('Arial', 30), bg='#9eeea2')
        # title_label.pack(side=tk.TOP, fill=tk.X)
        title_label.place(x=0, y=0, width=500, height=70)
        food_list = [row['name'] for row in self._read_csv(filename='Food_Menu.csv')]
        check_box_scroll = tk.Scrollbar(master=self.order_window, orient='vertical')
        check_box_text = tk.Text(master=self.order_window, yscrollcommand=check_box_scroll.set, bg='#f0f0f0')
        check_box_scroll.config(command=check_box_text.yview)
        check_box_scroll.pack(side=tk.LEFT)
        check_box_text.pack(side=tk.LEFT)
        check_box_scroll.place(x=10, y=110, height=400)
        check_box_text.place(x=30, y=120, width=450, height=400)
        confirm_btn = tk.Button(master=self.order_window, text='Confirm', font=('Arial', 15), command=self.order_result)
        confirm_btn.place(x=200, y=550, width=100, height=30)
        self.order_list = []
        for name in food_list:
            var_foodname = tk.StringVar(value='0')
            cb = tk.Checkbutton(master=self.order_window, text=name, variable=var_foodname, onvalue=name, font=('Arial', 15))
            check_box_text.insert('end', '\t\t\t')
            check_box_text.window_create('end', window=cb)
            check_box_text.insert('end', "\n")
            self.order_list.append(var_foodname)

    # Personal information page to the suggested diet page
    def config_confirm(self):
        def click():
            rows = list(self._read_csv(filename='User_information.csv'))
            for i in rows:
                if i['Username'] == self.username.get():
                    index = rows.index(i)
                    i['Weight'] = self.weight.get()
                    i['Height'] = self.height.get()
                    i['BMI'] = self.BMI.get()
                    i['Age'] = self.Age.get()
                    i['Gender'] = self.var_gender.get()
                    i['Job'] = self.var_job.get()
                    i['Exercise'] = self.config_answer.get()
                    i['ExpCalories'] = self.BEE
                    i['ExpProtein'] = self.suggestedprotein
                    i['ExpCarbo'] = self.suggestedcarbo
                    i['ExpFat'] = self.suggestedfat
                    fp = open(os.path.split(os.path.realpath(__file__))[0]+'//User_information.csv', 'w', newline='')
                    csvWriter = csv.DictWriter(fp, fieldnames=['Username', 'Password', 'Repassword', 'Weight', 'Height', 'BMI', 'Age', 'Gender', 'Job', 'Exercise', 'ExpCalories', 'ExpProtein', 'ExpCarbo', 'ExpFat'])
                    csvWriter.writeheader()
                    csvWriter.writerows(rows)
                    fp.close()
            self.suggest_window.destroy()
        self.config_window.destroy()
        self.suggested_data()
        self.suggest_window = tk.Toplevel(self.main_window)
        self.suggest_window.title('Diet-tracking Program')
        self.suggest_window.geometry('500x400+400+200')
        self.suggest_window.resizable(False, False)
        title_label = tk.Label(master=self.suggest_window, text='Personal Information', font=('Arial', 30), bg='#9eeea2')
        calories_label = tk.Label(master=self.suggest_window, text='Suggested daily calories intake:', font=('Arial', 15))
        protein_label = tk.Label(master=self.suggest_window, text='Suggested daily protein intake:', font=('Arial', 15))
        carbo_label = tk.Label(master=self.suggest_window, text='Suggested daily carbo intake:', font=('Arial', 15))
        fat_label = tk.Label(master=self.suggest_window, text='Suggested daily fat intake:', font=('Arial', 15))
        calories_value_label = tk.Label(master=self.suggest_window, text=self.BEE, font=('Arial', 15))
        protein_value_label = tk.Label(master=self.suggest_window, text=self.suggestedprotein, font=('Arial', 15))
        carbo_value_label = tk.Label(master=self.suggest_window, text=self.suggestedcarbo, font=('Arial', 15))
        fat_value_label = tk.Label(master=self.suggest_window, text=self.suggestedfat, font=('Arial', 15))
        back_btn = tk.Button(master=self.suggest_window, text='Back', font=('Arial', 15), command=click)
        title_label.place(x=0, y=0, width=500, height=100)
        calories_label.place(x=30, y=120, width=300, height=30)
        protein_label.place(x=25, y=170, width=300, height=30)
        carbo_label.place(x=20, y=220, width=300, height=30)
        fat_label.place(x=10, y=270, width=300, height=30)
        calories_value_label.place(x=330, y=120, width=100, height=30)
        protein_value_label.place(x=330, y=170, width=100, height=30)
        carbo_value_label.place(x=330, y=220, width=100, height=30)
        fat_value_label.place(x=330, y=270, width=100, height=30)
        back_btn.place(x=215, y=350, width=70, height=30)

    # Getting ordering result
    def order_result(self):
        def add():
            self.report_window.destroy()
        def report():
            self.report_window.destroy()
            self.order_window.destroy()
            fp = open(os.path.split(os.path.realpath(__file__))[0] + '//Diet.csv', 'a', newline='')
            csvWriter = csv.DictWriter(fp, fieldnames=['calories', 'protein', 'carbo', 'fat', 'mass'])
            csvWriter.writerow({'calories': total_result[0], 'protein': total_result[1], 'carbo': total_result[2], 'fat': total_result[3], 'mass': total_result[4]})
            fp.close()
        outList = []
        for i in self.order_list:
            if i.get() != '0':
                outList.append(i.get())
            else: continue
        total_result = self.total_data(dataList=outList)
        self.report_window = tk.Toplevel(self.order_window)
        self.report_window.title('Diet-tracking Program')
        self.report_window.geometry('500x600+400+50')
        title_label = tk.Label(master=self.report_window, text='Report', font=('Arial', 30), bg='#9eeea2')
        title_label.place(x=0, y=0, width=500, height=100)
        keep_adding_btn = tk.Button(master=self.report_window, text='Keep Adding', font=('Arial', 15), command=add)
        report_btn = tk.Button(master=self.report_window, text='Report', font=('Arial', 15), command=report)
        keep_adding_btn.place(x=70, y=550, width=150, height=30)
        report_btn.place(x=350, y=550, width=100, height=30)
        scrollbar = tk.Scrollbar(master=self.report_window, orient='vertical')
        check_text_box = tk.Text(master=self.report_window, yscrollcommand=scrollbar.set, bg='#f0f0f0')
        scrollbar.config(command=check_text_box.yview)
        scrollbar.pack(side=tk.LEFT)
        check_text_box.pack(side=tk.LEFT)
        scrollbar.place(x=10, y=110, height=400)
        check_text_box.place(x=30, y=120, width=250, height=400)
        for name in outList:
            cb = tk.Checkbutton(master=self.report_window, text=name, font=('Arial', 15))
            cb.select()
            check_text_box.insert('end', '\t\t\t')
            check_text_box.window_create('end', window=cb)
            check_text_box.insert('end', '\n')
        total_label = tk.Label(master=self.report_window, text='Total', font=('Arial', 15))
        calories_label = tk.Label(master=self.report_window, text='calories:', font=('Arial', 15))
        protein_label = tk.Label(master=self.report_window, text='protein:', font=('Arial', 15))
        carbo_label = tk.Label(master=self.report_window, text='carbo:', font=('Arial', 15))
        fat_label = tk.Label(master=self.report_window, text='fat:', font=('Arial', 15))
        mass_label = tk.Label(master=self.report_window, text='mass:', font=('Arial', 15))
        calories_value_label = tk.Label(master=self.report_window, text=str(total_result[0]), font=('Arial', 15))
        protein_value_label = tk.Label(master=self.report_window, text=str(total_result[1]), font=('Arial', 15))
        carbo_value_label = tk.Label(master=self.report_window, text=str(total_result[2]), font=('Arial', 15))
        fat_value_label = tk.Label(master=self.report_window, text=str(total_result[3]), font=('Arial', 15))
        mass_value_label = tk.Label(master=self.report_window, text=str(total_result[4]), font=('Arial', 15))
        total_label.place(x=300, y=110, width=150, height=30)
        calories_label.place(x=270, y=150, width=100, height=30)
        protein_label.place(x=270, y=200, width=100, height=30)
        carbo_label.place(x=270, y=250, width=100, height=30)
        fat_label.place(x=270, y=300, width=100, height=30)
        mass_label.place(x=270, y=350, width=100, height=30)
        calories_value_label.place(x=380, y=150, width=100, height=30)
        protein_value_label.place(x=380, y=200, width=100, height=30)
        carbo_value_label.place(x=380, y=250, width=100, height=30)
        fat_value_label.place(x=380, y=300, width=100, height=30)
        mass_value_label.place(x=380, y=350, width=100, height=30)

    # Calculating the intake
    def total_data(self, dataList=None):
        calories, protein, carbo, fat, mass = 0, 0, 0, 0, 0
        for i in self._read_csv(filename='Food_Menu.csv'):
            if i['name'] in dataList:
                calories += eval(i['calories'])
                protein += eval(i['protein'])
                carbo += eval(i['carbo'])
                fat += eval(i['fat'])
                mass += eval(i['mass'])
            else: continue
        return round(calories, 2), round(protein, 2), round(carbo, 2), round(fat, 2), round(mass, 2)

    # Suggest Diet
    def suggested_data(self):
        if self.var_gender.get() == 'male':
            self.BEE = 66.5 + 13.8 * eval(self.weight.get()) + 500 * eval(self.height.get()) - 6.8 * eval(self.Age.get())
            self.suggestedcarbo = round(self.BEE * 0.6, 2)
            self.suggestedfat = round(self.BEE * 0.3, 2)
            self.BEE = self.BEE * 1.2 if self.config_answer.get() == 'YES' else self.BEE
        elif self.var_gender.get() == 'female':
            self.BEE = 655.1 + 9.6 * eval(self.weight.get()) + 190 * eval(self.height.get()) - 4.7 * eval(self.Age.get())
            self.suggestedcarbo = round(self.BEE * 0.6, 2)
            self.suggestedfat = round(self.BEE * 0.3, 2)
            self.BEE = self.BEE * 1.2 if self.config_answer.get() == 'YES' else self.BEE
        self.suggestedprotein = eval(self.weight.get()) * 0.8
        #Based on reference: suggest intake of protein,carbo,fat,calories
        
    # Read csv
    def _read_csv(self, filename=None):
        fp = open(os.path.split(os.path.realpath(__file__))[0]+'//'+filename, 'r')
        reader = csv.DictReader(fp)
        return reader

if __name__ == '__main__':
    HealthySystem()

