# 1
# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# m = int(input("Enter the m: "))
# n = int(input("Enter the n: "))
# a = []
# print("Palindromes in the interval [{}, {}]: ".format(m, n))
# for i in range(m, n+1):
#     if is_palindrome(i):
#         print(i)

# 2
# def check():
#     while True:
#         try:
#             file_path = input("Enter a file path: ")
#             with open(file_path,'r'):
#                 pass
#             break 
#         except:
#             print("Please enter a file path")
#     return file_path

# def is_disordered():
#     a = []
#     file_path = check()
#     with open(file_path,'r') as f:
#         for line in f:
#             words = line.strip().split()
#             for word in words:
#                 for i in range(len(word) - 1):
#                     if word[i] > word[i+1]:
#                         a.append(word)
#                         s = " ".join(a)
#     print(s)
# is_disordered()
# 3
# def savetoDB(studentID,studentname,GPA,rank):
#     import sqlite3
#     conn = sqlite3.connect('STUDENTS.sqlite')
#     c = conn.cursor()
#     try:
#         c.executescript('''
#         create table student(studentID TEXT, studentname TEXT, GPA number, Rank TEXT);''')
#     except:
#         pass
#         c.execute('insert into student values(?,?,?,?)',(studentID,studentname,GPA,rank))
#     conn.commit()
#     conn.close()

# class student:
#     studentID = ''
#     Rank = ''
#     studentname = ''
#     GPA = ''
#     def __init__(self,studentID,studentname,Mark1,Mark2,Mark3,Mark4):
#         self.studentID = studentID
#         self.studentname = studentname 
#         self.Mark1 = Mark1
#         self.Mark2 = Mark2
#         self.Mark3 = Mark3
#         self.Mark4 = Mark4
        
#     def cal_GPA(self):
#         self.GPA = float((self.Mark1 + self.Mark2 + self.Mark3 + self.Mark4) / 4)
        
#     def cal_Rank(self):
#         if float(self.GPA) > 8:
#             self.Rank = 'excelent'        
#         elif float(self.GPA) > 6:
#             self.Rank = 'good'           
#         else:
#             self.Rank = 'bad'
#         print(f"{self.studentname},{self.studentID}, GPA is {self.GPA}, Rank is {self.Rank}")

#     def saveDB(self):
#         savetoDB(self.studentID,self.studentname,self.GPA,self.Rank)

# a = student('DE170256', 'Hoang Minh Duc',9, 9, 9, 9)
# a.cal_GPA()
# a.cal_Rank()
# a.saveDB()


