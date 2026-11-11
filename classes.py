import csv

class task:
    def __init__(self , name , explanation , periority):
        self.name = name
        self.exp = explanation
        self.per = periority


class todolist:
    def __init__(self):
        self.tasks = []
        
        

    def add_task(self , name , explanation , periority):
        self.tasks.append(task(name , explanation , periority))

    def remove_task(self , name):
        for task in self.tasks:
            if task.name == name :
                self.tasks.remove(task)
                return True

    def show_tasks(self):
        for task in self.tasks: 
            print(f"Task name: {task.name}")
            print(f"Task explanations: {task.exp}")
            print(f"Task periority: ({task.per})\n")

    def task_sort(self):
        self.tasks_sort = self.tasks.copy()
        self.tasks.clear()
        self.perio = set()
        for task in self.tasks_sort:
            self.perio.add(task.per)
            
        sort_set = set(self.perio)
        
        self.perio = sorted(sort_set)

        sort_set.clear()
        
        for i in range(len(self.perio)):
            for task in self.tasks_sort:
                if self.perio[i] == task.per:
                    self.tasks.append(task)
                    

    def task_info(self , name):
        for task in self.tasks:
            if task.name == name : 
                print(f"Task name: {task.name}")
                print(f"Task explanations: {task.exp}")
                print(f"Task periority: ({task.per})\n")
                return True

    def CSV_Write(self , filename):
        try:
            with open(f"{filename}.csv" , "w" , newline="" , encoding="utf-8") as file:

                
                writer = csv.writer(file)
                tasks = []
                for task in self.tasks:
                    tasks.append([task.name ,task.exp , task.per ])
                writer.writerows(tasks)
                return True
        except:
            print("An unexpected error happend!")
            return None
    def CSV_Read(self , filename):
        try:
            with open(f"{filename}.csv" , "r" , newline="" , encoding="utf-8") as file:
                reader = csv.reader(file)
                rows = list(reader)
                
                if len(rows) == 0 :
                    return False 
            for i in rows:
                self.tasks.append(task(i[0] , i[1] , int(i[2])))
        except:
            print("An error happened! check your file name!")
            return None
        return True    
l = todolist()
# l.add_task("hello0" ,"say hello to cows0" , 1)
# l.add_task("hello1" ,"say hello to cows1" , 2)
# l.add_task("hello2" ,"say hello to cows2" , 3)
# l.add_task("hello3" ,"say hello to cows3" , 1)
# l.add_task("hello4" ,"say hello to cows4" , 2)
# l.add_task("hello5" ,"say hello to cows5" , 2)
# l.add_task("hello6" ,"say hello to cows6" , 3)

l.task_sort()

# l.remove_task("hello0")
# l.show_tasks()
# l.task_info("hello1")

l.CSV_Write("name")
