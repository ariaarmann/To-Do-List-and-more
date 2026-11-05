from functions import *
from classes import *

print("Welcome to TO-Do list organizer!\n")
l = todolist()
while True:
    terminal_clearer()
    menu0 = menu()

    if menu0 == 1 :
        terminal_clearer()
        inp = input("<Adding task> press 0 to continue... Q for menu... ")
        if inp =="0":
            pass
        elif inp.lower() == "q" :
            
            continue
        else:
            break
        
        name = input("Enter your tasks name: ")
        exp = input("Enter your tasks explainations: ")
        while True:
            try:
                per = int(input("Enter your tasks priority: "))
                while per <1 :
                    print("periority should be a positive number!")
                    per = int(input("Enter your tasks priority: "))
                break
            except:
                print("Wrong data! priority should be a number!")
                
        l.add_task(name , exp , per)
        pbar(1 , "Adding...")
        print("Added.")
        time.sleep(1)
        
    if menu0 == 2 :
        terminal_clearer()
        inp = input("<Removing task> press 0 to continue... Q for menu... ")
        if inp =="0":
            pass
        elif inp.lower() == "q" : 
            continue
        else:
            break
                
        name = input("Enter your tasks name: ")
        r = l.remove_task(name)
        if r == None:
            print("Task Doesn't EXIST!")
            time.sleep(2)
        else:
            pbar(1 , "Removing...")
            print("Removed.")
            time.sleep(1)
    if menu0 == 3 :
        terminal_clearer()
        if len(l.tasks) == 0 :
            print("No tasks to show!")
            time.sleep(2)
            continue
        inp = input("<Task infos> press 0 to continue... Q for menu... ")
        if inp =="0":
            pass
        elif inp.lower() == "q" :
            continue
        else:
            break
        name = input("Enter your tasks name: ")
        print()
        r = l.task_info(name)
        if r == None:
            print("Task Doesn't EXIST!")
            time.sleep(2)
            continue
        
        inp = input("press any keys to continue...")

        
    if menu0 == 4 :
        terminal_clearer()
        if len(l.tasks) == 0 :
            print("No tasks to show!")
            time.sleep(2)
            continue
        l.show_tasks()
        inp = input("press 0 to sort tasks by priority... press q to menu...")
        if inp == "0" :
            terminal_clearer()
            l.task_sort()
            l.show_tasks()
            inp = input("press any keys to continue...")
            
        elif inp.lower() == "q" :
            continue
        else:
            break

    if menu0 == 5 :
        terminal_clearer()
        inp = input("<CSV task read> press 0 to continue... Q for menu... ")
        if inp =="0":
            pass
        elif inp.lower() == "q" :
            continue
        else:
            break


        inp = input("Enter your CSV file name: ")
        
        r = l.CSV_Read(inp)
        if r == True :
            pbar(2 , "Reading CSV file...")
            print("Completed.")
            time.sleep(1)
        elif r == None:
            inp = input("press any keys to continue...")
            continue
        else:
            print("File was empty!")
            inp = input("press any keys to continue...")
            continue
    if menu0 == 6 :
        terminal_clearer()
        inp = input("<Write over csv file> press 0 to continue... Q for menu... ")
        if inp =="0":
            pass
        elif inp.lower() == "q" :
            continue
        else:
            break
        if len(l.tasks) == 0 :
            print("No tasks to export!")
            inp = input("press any keys to continue...")
            continue
        inp = input("Enter CSV file name: ")
        r = l.CSV_Write(inp)
        if r == True :
            pbar(2 , "Proccecing...")
            print("Completed.")
            time.sleep(1)

        else : 
            inp = input("press any keys to continue...")
            continue
    if menu0 == 0 :
        print("Hope to see you again...")
        time.sleep(1.5)
        break        