#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector


# In[3]:


mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="",
        database = "emr"
)


# In[4]:


cursor = mydb.cursor()
cursor.execute("SELECT * FROM EMPLOYEE")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
mydb.close()


# In[ ]:


mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="",
        database = "emr"
)
def search(Id):
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE WHERE EMP_ID LIKE '%{}'".format(Id)
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        return True
    else:
        return False
    cursor.close()
    

        
def add_employee(Id,Name,Salary,Department,Email):
    cursor = mydb.cursor()
    query =  "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s)"
    values = (Id,Name,Salary,Department,Email)
    cursor.execute(query,values)
    mydb.commit()
    print("Employee Added Successfully ")
    cursor.close()
    
    
        
def update_employee(Name,Salary,Department,Email):
    cursor = mydb.cursor()
    query =  "UPDATE EMPLOYEE SET EMP_NAME=%s,EMP_SALARY=%s,EMP_DEPT=%s,EMAIL=%s WHERE EMP_ID=%s"
    values = (Name,Salary,Department,Email,Id)
    cursor.execute(query,values)
    mydb.commit()
    print("Employee Updated Successfully ")
    cursor.close()
    
def delete_employee(Id):
    cursor = mydb.cursor()
    query = "DELETE FROM EMPLOYEE WHERE EMP_ID LIKE '%{}'".format(Id)
    cursor.execute(query)
    mydb.commit()
    print("Deleted..")
    cursor.close()
    
def list_all():
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Employee Details : ")
        print("-------------------")
        for row in result:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Salary : ",row[2])
            print("Department : ",row[3])
            print("Email : ",row[4])
            print("---------------------")
    else:
        print("Empty!!")
    cursor.close()
    
def sort_dept():
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE ORDER BY EMP_DEPT"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Employee Details : ")
        print("-------------------")
        for row in result:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Salary : ",row[2])
            print("Department : ",row[3])
            print("Email : ",row[4])
            print("---------------------")
    else:
        print("Empty!!")
    cursor.close()
    
def sort_salary():
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE ORDER BY EMP_SALARY"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Employee Details : ")
        print("-------------------")
        for row in result:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Salary : ",row[2])
            print("Department : ",row[3])
            print("Email : ",row[4])
            print("---------------------")
    else:
        print("Empty!!")
    cursor.close()
    
def filter_dept(dept):
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE WHERE EMP_DEPT LIKE '%{}'".format(dept)
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("Employee Details : ")
        print("-------------------")
        for row in result:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Salary : ",row[2])
            print("Department : ",row[3])
            print("Email : ",row[4])
            print("---------------------")
    else:
        print("Empty!!")
    cursor.close()
    
def  filter_salary(mini,maxi):
    cursor = mydb.cursor()
    query = "SELECT * FROM EMPLOYEE WHERE EMP_SALARY BETWEEN %s AND %s"
    values = (mini,maxi)
    cursor.execute(query,values)
    result=cursor.fetchall()
    if result:
        print("Employees with salary in given range")
        print("------------------------------------")
        for row in result:
            print("Name : ",row[0])
            print("Salary : ",row[1])
            print("Salary : ",row[2])
            print("Department : ",row[3])
            print("Email : ",row[4])
            print("-------------------------------")
    else:
        print("No employees in this salary range")
    cursor.close()

    
if __name__=="__main__":
    while True:
        print("Employee Management System")
        print("---------------------------")
        print("1. Add new Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. List all Employees")
        print("5. Sort Employees")
        print("6. Filter Employees")
        print("7. Exit\n")
        ch=int(input("Enter your Choice: "))
        if ch == 1:
            Id=int(input("Employee Id : "))
            exist=search(Id)
            if exist==True:
                print("Employee Id already exist!\n")
            else:
                Name=input("Name : ")
                Salary=float(input("Salary : "))
                Department=input("Department : ")
                Email=input("Email : ")
                add_employee(Id,Name,Salary,Department,Email)
        elif ch == 2:
            Id=input("Employee Id : ")
            exist=search(Id)
            if exist==True:
                cursor = mydb.cursor()
                query = "SELECT * FROM EMPLOYEE WHERE EMP_ID LIKE '%{}'".format(Id)
                cursor.execute(query)
                result=cursor.fetchall()
                if result:
                    for row in result:
                        print("Name : ",row[1])
                        print("Salary : ",row[2])
                        print("Department : ",row[3])
                        print("Email : ",row[4])
                        print("----------------------")
                cursor.close()
                Name=input("Name : ")
                Salary=float(input("Salary : "))
                Department=input("Department : ")
                Email=input("Email : ")
                update_employee(Name,Salary,Department,Email)
            else:
                print("Employee Id not exist!!!\n")
        
        elif ch == 3:
            Id = int(input("Employee Id to be deleted : "))
            exist = search(Id)
            if exist==True:
                delete_employee(Id)
            else:
                print("Employee Id not exist!!!\n")
        elif ch == 4:
            list_all()
        elif ch == 5:
            print("\t1.Based on Department")
            print("\t2.Based on Salary")
            choice=int(input("Enter your choice : "))
            if choice==1:
                sort_dept()
            elif choice==2:
                sort_salary()
            else:
                print("Invalid choice\n")
        elif ch == 6:
            print("\t1.Based on Department")
            print("\t2.Based on Salary")
            choice=int(input("Enter your choice : "))
            if choice==1:
                dept=input("Enter the Department : ")
                filter_dept(dept)
            elif choice==2:
                mini=float(input("Enter minimum salary range : "))
                maxi=float(input("Enter maximum salary range : "))
                filter_salary(mini,maxi)
            else:
                print("Invalid choice\n")
            
        elif ch == 7:
            break
        else:
            print("Invalid choice. Please try again")
mydb.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




