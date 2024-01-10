#!/usr/bin/python3
import sys
import subprocess

#Setting default count to 1 
countGroup1 = 1
countGroup2 = 1
#Following will be the ansible group names
group1Name = "AnsibleGroup1"
group2Name = "AnsibleGroup2"

print("\n =================== Ansible EC2 maker playbook =================== \n")
try:
    if len(sys.argv) >= 3 and int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 3 and int(sys.argv[2]) >= 1 and int(sys.argv[2]) <= 3:

        print ('Argument List:', str(sys.argv[1]),'  ',str(sys.argv[2]))

        countGroup1 = int(sys.argv[1])
        countGroup2 = int(sys.argv[2])

        ansibleCommandGroup1="ansible-playbook AnsibleEC2Playbook.yml  --extra-vars \"grouping="+group1Name+" count="+str(countGroup1)+"\""
        ansibleCommandGroup2="ansible-playbook AnsibleEC2Playbook.yml  --extra-vars \"grouping="+group2Name+" count="+str(countGroup1)+"\""

        print("\nPlayng ansible playbook for group 1 "+ansibleCommandGroup1+"\n")
        print("\nPlayng ansible playbook for group 2 "+ansibleCommandGroup2+"\n")

        ansibleCommand1ReturnCode = subprocess.call(ansibleCommandGroup1, shell=True)
        ansibleCommand2ReturnCode = subprocess.call(ansibleCommandGroup2, shell=True)
    else:
        print("\nPlease enter two numbers less than 3 with a space as parameters\n")
except ValueError as err:
    print("\nPlease enter two numbers less than 3 with a space as parameters\n")
