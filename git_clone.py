import os

os.system("git status & git add .")
inp=input("Enter the commit tag ")
os.system('git commit -m inp')
os.system("git push" )
