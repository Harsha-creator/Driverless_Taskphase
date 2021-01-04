import pandas as pd
class student():
    column = ['Name', 'Admissionnumber', 'Rollnumber', 'Class', 'Sciencemarks', 'Mathsmarks', 'Socialstudiesmarks','Englishmarks']
    row = [[0]*8]

    def __init__(self, df):
        self.df = df

    def addrow(self):
        for i in range(len(column)):
            if (column[i] == 'Name'):
                e=0
                while (e==0):
                    row[0][i] = input("enter %s of the student" %column[i])
                    contains_digit = any(map(str.isdigit, row[0][i]))
                    if (contains_digit):
                        e = input("Your name contains numbers ,invalid \nif you want to try again press 0")
                    else:
                        e = 1
            else:
                z=0
                while (z==0):
                    row[0][i] = input("enter %s of the student" %column[i])
                    if ((row[0][i]).isdigit()):
                        z = 1
                    else:
                        z = input("Your %s contains alphabets, invalid \nif you want to try again press 0")
            
        df2 = pd.DataFrame(row , columns = column)
        x = (self.df).append(df2, ignore_index = True)
        x = x.infer_objects() 
        return student(x) 

    def update(self):
        (self.df).to_csv('/home/harsha/Desktop/miniproject.csv')   

    def display(self):
        print((self.df).to_string(index=False))
    
    def search(self):
        choice = int(input("1 for search by name \n2 for search by roll number \n3 for search by class"))
        if (choice == 1):
            sub = input("enter Name")
            contains_digit = any(map(str.isdigit, sub))
            d=0
            while (d == 0):
                if (contains_digit): 
                    print ("input should have only alphabets")
                    d = input("want to try again press 0") 
                else:
                    d=1
            
            y = (self.df).loc[(self.df)['Name'] == sub] 
        if (choice == 2):
            d=0
            while (d == 0):
                try: 
                    sub = int(input("enter RollNumber"))
                    d = 1
                except: 
                    print ("input should have only digits")
                    d = input("want to try again press 0")
            
            y = (self.df).loc[(self.df)['RollNumber'] == sub]
        if (choice == 3):
            d=0
            while (d == 0):
                try: 
                    sub = int(input("enter Class"))
                    d = 1
                except: 
                    print ("input should have only digits")
                    d = input("want to try again press 0")
            
            y = (self.df).loc[(self.df)['Class'].isin(sub)]
        else :
            print("invalid input")
        if (y.empty):
            print("not found")
        else:
            print((y.loc[:,['Name','Sciencemarks', 'Mathsmarks', 'Socialstudiesmarks','Englishmarks']]).to_string(index=False))
    
    def Compute_ranks(self):
        g =  pd.DataFrame((self.df['Sciencemarks']+self.df['Mathsmarks']+self.df['Socialstudiesmarks']+self.df['Englishmarks'])/4,columns = ['Average'])
        g['Name'] = self.df['Name']
        g.sort_values(by=['Average'],ascending = False, inplace = True, na_position ='last')        
        print ("top ten students \n")
        print (g.head(10))
    
    def Merit_students(self):
        g =  (self.df).loc[:,['Name','Sciencemarks', 'Mathsmarks', 'Socialstudiesmarks','Englishmarks']]
        for i in range(1,4):
            x = g[column[i+4]] > 90
            g = g[x]
        print(g.to_string(index=False))


def menu(c,a):
    if(c==1):
        a = a.addrow()
        a.update()
    if(c==2):
        a.Compute_ranks()
    if(c==3):
        a.Merit_students()
    if(c==4):
        a.search()
    else:
        print("invalid choice")
if __name__ == "__main__": 
    column = ['Name', 'Admissionnumber', 'Rollnumber', 'Class', 'Sciencemarks', 'Mathsmarks', 'Socialstudiesmarks','Englishmarks']
    row = [[0]*8]
    a = student(pd.read_csv('/home/harsha/Desktop/miniproject.csv',index_col=0))
    c = int(input("enter 1 for adding a details of a student and updating the csv file \n enter 2 for printing top 10 students list \n enter 3 for printing merit students list \n enter 4 to search for a student"))
    menu(c,a)
