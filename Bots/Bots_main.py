from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox  
from joblib import Parallel, delayed
from selenium.common.exceptions import NoSuchElementException
from Inst import *
import tkinter as tk 
import random
import json



class gui1:

    def __init__(self):
        self.window = Tk()
        self.window.geometry('1280x500')
        self.window.title("Bots")
        
        self.B_np = 0
        self.B_table = 0
        self.B_create_bot = 0
        self.B_settings = 0
        self.B_ButtonFunctionSettingsSave = 0

        self.count = 1
        self.botusecount = 0
        
        self.select_index_Proxy = 0
        self.select_index_Delay = 1
        self.Num_Th = 1
        
        
        self.Lost_bot_in_Bot_DB = 0

        try:
            self.load_User_DB()
        except Exception as ex:
            print("Ошибка загрузки: User_DB")
            print(ex)
            self.count = 0

        try:
            self.load_Proxy_DB()
        except Exception as ex:
            print("Ошибка загрузки: Proxy_DB")
            print(ex)

        try:
            self.load_Bot_DB()
        except Exception as ex:
            print("Ошибка загрузки: Bot_DB")
            print(ex)

        try:
            self.load_Settings()
        except Exception as ex:
            print("Ошибка загрузки: Settings")
            print(ex)

        
            

    #описывается загрузка начальных файлов
    def load_User_DB(self):
        FileOutput = open(f'User_DB.txt','r')
        StringFileOutput = FileOutput.readline()
        for char in StringFileOutput:
            if char==',':
                self.count = self.count + 1
        FileOutput.close()

        self.count = int(float(self.count) / 5)

        self.UserDB = [0] * self.count
        for i in range(self.count):
            self.UserDB[i] = [0] * 5

        self.EntryTable = [0] * self.count
        for i in range(self.count):
            self.EntryTable[i] = [0] * 5

        self.UserDB = json.load(open(f"User_DB.txt", "r"))

    def load_Proxy_DB(self):
        with open(f'Proxy_DB.txt','r') as f:
            self.ProxyDBbasic = f.readlines()
        self.ProxyDBbasic.insert(0, "")
        
    def load_Bot_DB(self):     
        with open(f'Bot_DB.txt','r') as f:
            self.BotDB = f.readlines()

        self.botcount = len(self.BotDB)

    def load_Settings(self):
        with open(f"Settings.txt","r") as f:
            self.select_index_Proxy = int(f.readline())
            self.CountUseProxy = int(f.readline())

            self.select_index_Delay = int(f.readline())
            self.Delay = f.readline()

            self.Num_Th = int(f.readline())


    #описывается меню
    def menu(self):
        window = self.window
        menu = Menu(window)


        #проект
        new_item_Project = Menu(menu, tearoff = 0)

        sub_item = Menu(new_item_Project, tearoff = 0)

        sub_item.add_command(label="Inst", command = lambda: self.new_project("Inst"))

        sub_item.add_command(label="Vk", command = lambda: self.new_project("Vk"))

        sub_item.add_command(label="TikTok", command = lambda: self.new_project("TikTok"))

        new_item_Project.add_cascade(label = 'Новый проект', menu = sub_item)    

        new_item_Project.add_command(label = 'Все проекты', command = self.drow_table)
        new_item_Project.add_separator()  

        new_item_Project.add_command(label = 'Сохранить',command = self.save)
        new_item_Project.add_separator()

        new_item_Project.add_command(label = 'Выход', command = self.close_window)  


        #создание бота
        new_item_CreateBot = Menu(menu, tearoff = 0)

        new_item_CreateBot.add_command(label = 'Inst', command = lambda: self.Create_Bot('Inst'))  

        new_item_CreateBot.add_command(label = 'Vk') 

        new_item_CreateBot.add_command(label = 'TikTok')

       
        #объединение
        menu.add_cascade(label = 'Проект', menu = new_item_Project)
        menu.add_cascade(label = 'Создание бота', menu = new_item_CreateBot)
        menu.add_cascade(label = 'Параметры', command = self.settings)
        menu.add_cascade(label = 'Режим отладки') 

        window.config(menu = menu)


    #описывается новый проект
    def new_project(self,_type):
        if self.B_np == 0:
                        
            self.clear_window_settings()
            self.clear_window_table()
            self.clear_window_Create_Bot()
            self.clear_window_Progress_Bart()

            self.child_window = Toplevel()
            self.child_window.geometry('600x300')

            self.B_np = 1
            #содержимое дочернего окна
            LabelNew_projectName = Label(self.child_window,text = "Name")
            LabelNew_projectName.grid(row = 0,column = 0, pady = 5)

            LabelNew_projectLike = Label(self.child_window,text = "Like")
            LabelNew_projectLike.grid(row = 0,column = 1, pady = 5)

            LabelNew_projectComment = Label(self.child_window,text="Comment")
            LabelNew_projectComment.grid(row = 0,column = 2, pady = 5)

            LabelNew_projectFollow = Label(self.child_window,text="Follow")
            LabelNew_projectFollow.grid(row = 0,column = 3, pady = 5)


            LabelNew_projectUrlPage = Label(self.child_window,text="URL страницы")
            LabelNew_projectUrlPage.grid(row = 2,column = 0, pady = 20)

            LabelNew_projectUrlPost = Label(self.child_window,text="URL постa")
            LabelNew_projectUrlPost.grid(row = 3,column = 0, pady = 20)


            

            self.EntryNew_projectName = Entry(self.child_window, justify = CENTER, relief = GROOVE)
            self.EntryNew_projectName.grid(row = 1, column = 0, padx = 5)

            self.EntryNew_projectLike = Entry(self.child_window, bd = 1.5, justify = CENTER, relief = GROOVE)
            self.EntryNew_projectLike.grid(row = 1, column = 1,padx = 5)

            self.EntryNew_projectComment = Entry(self.child_window, bd = 1.5, justify = CENTER, relief = GROOVE)
            self.EntryNew_projectComment.grid(row = 1, column = 2,padx = 5)

            self.EntryNew_projectFollow = Entry(self.child_window, bd = 1.5, justify = CENTER, relief = GROOVE)
            self.EntryNew_projectFollow.grid(row = 1, column = 3,padx = 5)


            self.EntryNew_projectUrlPage = Entry(self.child_window, bd = 1.5, justify = CENTER, width = 20, relief = GROOVE)
            self.EntryNew_projectUrlPage.grid(row = 2, column = 1,pady = 5)

            self.EntryNew_projectUrlPost = Entry(self.child_window, bd = 1.5, justify = CENTER, width = 20, relief = GROOVE)
            self.EntryNew_projectUrlPost.grid(row = 3, column = 1,pady = 5)



            ButtonNew_projectOk = Button(self.child_window, text="Ок", width = 20, relief = GROOVE, command = lambda: self.InsertToUserDB(_type))  
            ButtonNew_projectOk.grid(row = 4, column = 3, pady = 50)  

            self.child_window.protocol("WM_DELETE_WINDOW", self.on_closing)
      
    def on_closing(self):
        if messagebox.askokcancel("Закрыть", "Вы уверены что хотите закрыть?"):
            self.B_np = 0
            self.child_window.destroy()

    def InsertToUserDB(self,_type):
        window = self.window

        self.B_np = 0

        if self.EntryNew_projectLike.get() != "":
            NumLike = int(self.EntryNew_projectLike.get())
        else:
            NumLike = 0

        if self.EntryNew_projectComment.get() != "":
            NumComment = int(self.EntryNew_projectComment.get())
        else:
            NumComment = 0

        if self.EntryNew_projectFollow.get() != "":
            NumFollow = int(self.EntryNew_projectFollow.get())
        else:
            NumFollow = 0

        URL_Post = self.EntryNew_projectUrlPost.get()
        URL_Page = self.EntryNew_projectUrlPage.get()


        self.UserDB.insert(self.count,[self.EntryNew_projectName.get(), NumLike, NumComment, NumFollow,_type])
        self.EntryTable.insert(self.count,[0,0,0,0,0])
        self.count = self.count + 1
        self.child_window.destroy()

        if self.Num_Th == 1:
            self.Create_Progress_Bar(window, "init", NumLike + NumComment + NumFollow, 0) 

        if NumLike > 0:
            self.botusecount = NumLike
            self.InstMain(URL_Post, URL_Page, "Like")

        if NumComment > 0:
            self.botusecount = NumComment
            self.InstMain(URL_Post, URL_Page, "Comment")
        
        if NumFollow > 0:
            self.botusecount = NumFollow
            self.InstMain(URL_Post, URL_Page, "Follow")
        
    def InstMain(self,URL1, URL2, w_type):
        window = self.window

        botusecount = self.botusecount

        if self.Num_Th == 1:
            for i in range(self.botusecount):
                self.bot("Inst", i, URL1, URL2, w_type)
                self.Create_Progress_Bar(window, "", botusecount, i)
        else:
            Parallel(n_jobs = self.Num_Th, require = 'sharedmem')(delayed(self.bot)("Inst", i, URL1, URL2, w_type) for i in range(self.botusecount))

    def bot(self, Platform, i ,URL1, URL2, w_type):

        self.Lost_bot_in_Bot_DB = i

        if self.botusecount <= self.botcount:

            if Platform == "Inst":
                if w_type == "Like":
                    b = 0
                    while b <= 0:
                        if b == -5:
                            i = self.Lost_bot_in_Bot_DB + 1
                            self.botusecount += 1
                            print("смена бота")
                            b = 0
                            self.Lost_bot_in_Bot_DB = i
                        try:
                            username = self.BotDB[i] + "@yandex.ru"
                            password = self.BotDB[i][::-1]
                            test_bot_1 = InstagramBot(username, password, self.Ind_to_Proxy(i), self.Delay)
                            test_bot_1.login()
                            print(f"b(1) = {b}")
                            test_bot_1.post_like(URL1)
                            print(f"b(2) = {b}")
                            test_bot_1.close_browser()
                            b = 1
                            print(f"b(3) = {b}")
                        except NoSuchElementException:
                            b = b - 1
                            print(f"b(1) = {b}")
                            test_bot_1.close_browser()
                            print(f"b(1) = {b}")                      
                if w_type == "Follow":
                    b = 0
                    while b <= 0:
                        if b == -5:
                            i += 1
                            self.botusecount += 1
                            print("смена бота")
                            b = 0
                        try:
                            username = self.BotDB[i] + "@yandex.ru"
                            password = self.BotDB[i][::-1]
                            test_bot_1 = InstagramBot(username, password, self.Ind_to_Proxy(i), self.Delay)
                            test_bot_1.login()
                            test_bot_1.user_follow(URL2)
                            test_bot_1.close_browser()
                            b = 1
                        except NoSuchElementException:
                            b <= 0
                            test_bot_1.close_browser()
                if w_type == "Comment":
                    b=0
                    while b <= 0:
                        if b == -5:
                            i += 1
                            self.botusecount += 1
                            print("смена бота")
                            b = 0
                        try:
                            username = self.BotDB[i] + "@yandex.ru"
                            password = self.BotDB[i][::-1]
                            print(username)
                            print(password)
                            test_bot_1 = InstagramBot(username, password, self.Ind_to_Proxy(i), self.Delay)
                            test_bot_1.login()
                            test_bot_1.user_follow(URL1)
                            test_bot_1.close_browser()
                            b = 1
                        except NoSuchElementException:
                            b <= 0
                            test_bot_1.close_browser()
    
            elif Platform == "Vk":
                print(Platform)
            b=0
        else:
            print("Боты закончились")


    #описывается все проекты
    def drow_table(self):
        if self.B_table == 0:

            self.clear_window_settings()
            self.clear_window_Create_Bot()
            self.clear_window_Progress_Bart()

            root = self.window


            self.frame_table = Frame(root)
            self.canvas_table = tk.Canvas(self.frame_table, highlightthickness = 0)

            self.scrollbar_table = ttk.Scrollbar(self.frame_table, orient = "vertical", command = self.canvas_table.yview)
            scrollable_frame = ttk.Frame(self.canvas_table)
            scrollable_frame.bind("<Configure>", lambda e: self.canvas_table.configure(scrollregion = self.canvas_table.bbox("all")))
            self.canvas_table.create_window((0, 0), window = scrollable_frame,anchor="nw")
 
            self.canvas_table.configure(yscrollcommand = self.scrollbar_table.set)
 
           
            self.frame_table.pack(fill="both", expand = True)
            self.canvas_table.pack(side="left", fill="both", expand = True)
            self.scrollbar_table.pack(side = "right", fill = "y")

            if self.count!=0:
                LabelTableName = Label(scrollable_frame,text = "Name")
                LabelTableName.grid(row = 0,column=0, pady = 5)

                LabelTableLike = Label(scrollable_frame,text = "Like")
                LabelTableLike.grid(row = 0,column=1, pady = 5)

                LabelTableComment = Label(scrollable_frame,text="Comment")
                LabelTableComment.grid(row = 0,column = 2, pady = 5)

                LabelTableFollow = Label(scrollable_frame,text="Follow")
                LabelTableFollow.grid(row = 0,column = 3, pady = 5)

                LabelTablePlatform = Label(scrollable_frame,text = "Platform")
                LabelTablePlatform.grid(row = 0,column = 4, pady = 5)

                self.B_table = self.B_table + 1
            else:
                LabelTableNoProject = Label(scrollable_frame,text = "У вас пока нет проектов")
                LabelTableNoProject.grid(row = 0,column=0, pady = 5)

            for row in range(self.count):
                self.EntryTable[row][0] = Entry(scrollable_frame, bd = 1.5, justify = CENTER, relief = GROOVE)
                self.EntryTable[row][0].insert(END, self.UserDB[row][0])
                self.EntryTable[row][0].grid(row = row + 1, column = 0)

                self.EntryTable[row][1] = Entry(scrollable_frame, bd = 1.5, justify = CENTER, relief = GROOVE)
                self.EntryTable[row][1].insert(END, self.UserDB[row][1])
                self.EntryTable[row][1].grid(row = row + 1, column = 1)

                self.EntryTable[row][2] = Entry(scrollable_frame, bd = 1.5, justify = CENTER, relief = GROOVE)
                self.EntryTable[row][2].insert(END, self.UserDB[row][2])
                self.EntryTable[row][2].grid(row = row + 1, column = 2)

                self.EntryTable[row][3] = Entry(scrollable_frame, bd = 1.5, justify = CENTER, relief = GROOVE)
                self.EntryTable[row][3].insert(END, self.UserDB[row][3])
                self.EntryTable[row][3].grid(row = row + 1, column = 3)

                self.EntryTable[row][4] = Entry(scrollable_frame, bd = 1.5, justify = CENTER, relief = GROOVE)
                self.EntryTable[row][4].insert(END, self.UserDB[row][4])
                self.EntryTable[row][4].grid(row = row + 1, column = 4) 

    def clear_window_table(self):
        try:
            self.canvas_table.pack_forget()
            self.frame_table.pack_forget()
            self.scrollbar_table.pack_forget()
            self.B_table = 0
        except Exception as ex:
            print(ex)


    #описывается сохранить
    def save(self):
        if self.B_table == 1:
            for row in range(self.count):
                self.UserDB[row][0] = self.EntryTable[row][0].get()

                self.UserDB[row][1] = self.EntryTable[row][1].get()

                self.UserDB[row][2] = self.EntryTable[row][2].get()

                self.UserDB[row][3] = self.EntryTable[row][3].get()

                self.UserDB[row][4] = self.EntryTable[row][4].get()
        self.input_file()

    def input_file(self):
        with open("DB\\Settings.txt","w") as f:
            f.write(str(self.select_index_Proxy) + "\n")
            f.write(str(self.CountUseProxy) + "\n")

            f.write(str(self.select_index_Delay) + "\n")
            f.write(self.Delay + "\n") 

            f.write(str(self.Num_Th) + "\n")


        try:
            json.dump(self.UserDB, open("DB\\User_DB.txt", "w"))
        except Exception as ex:
            print("Ошибка сохранения файла: input_file")


    #описывается создание ботов
    def Create_Bot(self, _type):

        if self.B_create_bot == 0:
            self.B_create_bot = 1
            self.clear_window_settings()
            self.clear_window_table()

            window = self.window


            self.LabelCreate_BotCount= Label(window,text = "Введите колличество ботов, которое нужно создать.")
            self.LabelCreate_BotCount.grid(row = 0,column = 0, pady = 5)

            self.EntryCreate_BotCount = Entry(window, justify = CENTER, relief = GROOVE)
            self.EntryCreate_BotCount.grid(row = 0, column = 1, padx = 5)


            self.ButtonCreate_BotOk = Button(window, text = "Ок", width = 20, relief = GROOVE, command = lambda: self.ScriptCreate_Bot(_type))  
            self.ButtonCreate_BotOk.grid(row = 2, column = 1, pady = 50)  

    def ScriptCreate_Bot(self, _type):
        window = self.window
        self.clear_window_Create_Bot()

        AllValue = int(self.EntryCreate_BotCount.get())
        for i in range(AllValue):
            b = 0
            self.Create_Progress_Bar(window,"init", AllValue, i)
            while b == 0:
                try:
                    print(f"Используемый прокси: {self.Ind_to_Proxy(i)}")
                    c_b = Create_Bot(self.Ind_to_Proxy(i),self.Delay)
                    c_b.Create_mail(12, _type)
                    c_b.close_browser()
                    b = 1
                except NoSuchElementException:
                    b = 0
                    c_b.close_browser()

            self.CreateBotDataBase()
            self.Create_Progress_Bar(window,"second", AllValue, i)
        b = 0
                    
    def clear_window_Create_Bot(self):
        self.B_create_bot = 0
        try:
            self.LabelCreate_BotCount.grid_remove()
            self.EntryCreate_BotCount.grid_remove()
            self.ButtonCreate_BotOk.grid_remove()
            
        except Exception as ex:
            print(ex)

    def CreateBotDataBase(self):

        f_Bot_DB = open("DB\\Bot_DB.txt", "a")
        f_Bot_DB.write(current_login)
        print("\n")
        print(current_login + "@yandex.ru")
        print("\n")
        f_Bot_DB.close()


    #описывается соединение прокси сервера с инициализацией браузера
    def Ind_to_Proxy(self, ind):
        
        for i in range(self.CountUseProxy-1):
            print(f"индекс до количества используемых ботов: {i}")
            if (ind % self.CountUseProxy) == i:
                return self.ProxyDBconverted[i]


    #описывается пргресс бар
    def Create_Progress_Bar(self, root, ootc, AllValue, current_value):

        if (ootc == "init") or (ootc == "Init"):
            print("It's progres BAR init")
            StyleInsertToUserDB = ttk.Style()  
            StyleInsertToUserDB.theme_use('default')  
            StyleInsertToUserDB.configure("green.Horizontal.TProgressbar", background = 'green')

            self.ProgressbarInsertToUserDB = Progressbar(root, length = 200, style = 'green.Horizontal.TProgressbar')  
            self.ProgressbarInsertToUserDB['value'] = int((current_value + 1)  * 100 / AllValue) 
            self.ProgressbarInsertToUserDB.grid(row = 1, column = 1, pady = 20) 

            self.LabelInsertToUserDBProcent = Label(root, text = str(self.ProgressbarInsertToUserDB['value']) + "%")
            self.LabelInsertToUserDBProcent.grid(row = 1, column = 2, pady = 5)
        else:
            print("It's progres BAR")
            self.ProgressbarInsertToUserDB['value'] =  int((current_value + 1)  * 100 / AllValue) 
            self.LabelInsertToUserDBProcent.config(text = str(self.ProgressbarInsertToUserDB['value']) + "%")
            root.update()
            print("Out is progress BAR")

    def clear_window_Progress_Bart(self):
        try:
            self.ProgressbarInsertToUserDB.grid_remove()
            self.LabelInsertToUserDBProcent.grid_remove()
            
        except Exception as ex:
            print(ex)


    #описывается параметры
    def settings(self):
        if self.B_settings == 0: 
            self.B_settings = 1

            window = self.window

            self.clear_window_Create_Bot()
            self.clear_window_Progress_Bart()
            self.clear_window_table()

            self.LabelSettingsProxy = Label(window,text = "Используемый proxy сервер:")
            self.LabelSettingsProxy.grid(row = 0,column=0, pady = 5)

            self.ComboBoxSettingsProxy = Combobox(window,values = ["Все", "Диапазон", "Один"],state = "readonly")
            self.ComboBoxSettingsProxy.current(self.select_index_Proxy)
            self.ComboBoxSettingsProxy.grid(row = 0, column = 1, padx = 10)


            self.LabelSettingsDelay = Label(window,text = "Используемая задержка:")
            self.LabelSettingsDelay.grid(row = 1,column=0, pady = 5)

            self.ComboBoxSettingsDelay = Combobox(window,values = ["Маленькая", "Нормальная", "Большая"],state = "readonly")
            self.ComboBoxSettingsDelay.current(self.select_index_Delay)
            self.ComboBoxSettingsDelay.grid(row = 1, column = 1, padx = 10)


            self.LabelSettingsThreds = Label(window,text = "Колличество используемых потоков:")
            self.LabelSettingsThreds.grid(row = 2,column=0, pady = 5)

            self.EntrySettingsThreds = Entry(window, bd = 1.5, justify = CENTER, relief = GROOVE)
            self.EntrySettingsThreds.insert(END,str(self.Num_Th))
            self.EntrySettingsThreds.grid(row = 2, column = 1, padx = 20)


            self.ButtonSettingsApplying_Settings = Button(window, text = "Применить настройки", width = 20, relief = GROOVE, command = self.ButtonFunctionSettingsSave)  
            self.ButtonSettingsApplying_Settings.grid(row = 3, column = 3, pady = 50)
            
    def ButtonFunctionSettingsSave(self):
        self.ProxyDBconverted = []

        if self.ComboBoxSettingsProxy.get() == "Все":
            self.select_index_Proxy = 0
            self.ProxyDBconverted = self.ProxyDBbasic
            self.CountUseProxy = len(self.ProxyDBconverted)
        elif self.ComboBoxSettingsProxy.get() == "Диапазон":
            if self.B_ButtonFunctionSettingsSave == 0:
                self.select_index_Proxy = 1
                self.B_ButtonFunctionSettingsSave = 1

                self.SettingsProxyChild_window = Toplevel()
                self.SettingsProxyChild_window.geometry('600x300')

            
                LabelButtonFunctionSettingsSave1 = Label(self.SettingsProxyChild_window, text = "Введиде диапазон от")
                LabelButtonFunctionSettingsSave1.grid(row = 0,column = 0, pady = 5)

                self.EntryButtonFunctionSettingsSave1 = Entry(self.SettingsProxyChild_window, justify = CENTER, relief = GROOVE)
                self.EntryButtonFunctionSettingsSave1.grid(row = 0,column = 1, pady = 5)

                LabelButtonFunctionSettingsSave2 = Label(self.SettingsProxyChild_window, text = "до")
                LabelButtonFunctionSettingsSave2.grid(row = 0,column = 2, pady = 5)

                self.EntryButtonFunctionSettingsSave2 = Entry(self.SettingsProxyChild_window, justify = CENTER, relief = GROOVE)
                self.EntryButtonFunctionSettingsSave2.grid(row = 0,column = 3, pady = 5)
            
                self.ButtonSettingsSave = Button(self.SettingsProxyChild_window, text="Ок", width = 20, relief = GROOVE, command = self.ButtonFunctionSettingsOkDiap)  
                self.ButtonSettingsSave.grid(row = 3, column = 3, pady = 5)
            
            
                self.SettingsProxyChild_window.protocol("WM_DELETE_WINDOW", self.ButtonFunctionSettingsSave_on_closing)
        elif self.ComboBoxSettingsProxy.get() == "Один":
            if self.B_ButtonFunctionSettingsSave == 0:
                self.select_index_Proxy = 2
                self.B_ButtonFunctionSettingsSave = 1

                self.SettingsProxyChild_window = Toplevel()
                self.SettingsProxyChild_window.geometry('600x300')

            
                LabelButtonFunctionSettingsSave1 = Label(self.SettingsProxyChild_window, text = "Введиде индекс IP")
                LabelButtonFunctionSettingsSave1.grid(row = 0,column = 0, pady = 5)

                self.EntryButtonFunctionSettingsSave1 = Entry(self.SettingsProxyChild_window, justify = CENTER, relief = GROOVE)
                self.EntryButtonFunctionSettingsSave1.grid(row = 0,column = 1, pady = 5)
            
                self.ButtonSettingsSave = Button(self.SettingsProxyChild_window, text="Ок", width = 20, relief = GROOVE, command = self.ButtonFunctionSettingsOkInd)  
                self.ButtonSettingsSave.grid(row = 3, column = 3, pady = 5)
            
            
                self.SettingsProxyChild_window.protocol("WM_DELETE_WINDOW", self.ButtonFunctionSettingsSave_on_closing)

        if self.ComboBoxSettingsDelay.get() == "Маленькая":
            self.select_index_Delay = 0
            self.Delay = "small"
        elif self.ComboBoxSettingsDelay.get() == "Нормальная":
            self.select_index_Delay = 1
            self.Delay = "normal"
        elif self.ComboBoxSettingsDelay.get() == "Большая":
            self.select_index_Delay = 2
            self.Delay = "huge"

        self.Num_Th = int(self.EntrySettingsThreds.get())

    def ButtonFunctionSettingsOkDiap(self):
        self.ProxyDBconverted = self.ProxyDBbasic[int(self.EntryButtonFunctionSettingsSave1.get()):int(self.EntryButtonFunctionSettingsSave2.get())]
        self.B_ButtonFunctionSettingsSave = 0
        self.CountUseProxy = len(self.ProxyDBconverted)
        self.SettingsProxyChild_window.destroy()

    def ButtonFunctionSettingsOkInd(self):
        self.ProxyDBconverted = self.ProxyDBbasic[int(self.EntryButtonFunctionSettingsSave1.get())]
        self.B_ButtonFunctionSettingsSave = 0
        self.CountUseProxy = 1
        self.SettingsProxyChild_window.destroy()

    def ButtonFunctionSettingsSave_on_closing(self):
        if messagebox.askokcancel("Закрыть", "Вы уверены что хотите закрыть?"):
            self.B_ButtonFunctionSettingsSave = 0
            self.SettingsProxyChild_window.destroy()

    def clear_window_settings(self):
        self.B_settings = 0
        try:
            self.LabelSettingsProxy.grid_remove()
            self.ComboBoxSettingsProxy.grid_remove()

            self.LabelSettingsDelay.grid_remove()
            self.ComboBoxSettingsDelay.grid_remove()

            self.LabelSettingsThreds.grid_remove()
            self.EntrySettingsThreds.grid_remove()

            self.ButtonSettingsApplying_Settings.grid_remove()
            
        except Exception as ex:
            print(ex)


    #описывается закрыть
    def close_window(self):
        window = self.window
        window.destroy() 

    def finalize_window(self):
        window = self.window
        window.mainloop()






def main():
    guiw = gui1()
    guiw.menu()
    guiw.finalize_window()
   




if __name__ == '__main__':
     main()

