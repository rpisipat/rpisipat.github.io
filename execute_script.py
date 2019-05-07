import sys

command1 = "final_submission_script.py" + sys.argv[1] + sys.argv[2] + sys.argv[3]
command2 = "final_submission_script2.py" + sys.argv[1] + sys.argv[2] + sys.argv[3]


execfile(command1)
execfile(command2)
