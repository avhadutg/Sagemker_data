import os
import time

os.system("git status & git add .")
time.sleep(1)
inp=input("Enter the commit tag ")
os.system('git commit -m inp')
os.system("git push" )
