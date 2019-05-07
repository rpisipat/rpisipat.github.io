import sys
import os

command1 = "python final_submission_script.py " + sys.argv[1]  + " "+ sys.argv[2] + " " + sys.argv[3]
command2 = "python final_submission_script2.py " + sys.argv[1]  + " "+ sys.argv[2] + " " + sys.argv[3]


os.system(command1)
os.system(command2)
