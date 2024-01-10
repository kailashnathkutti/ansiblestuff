#To install Apache 3 in EC2 instances
#!/usr/bin/python3

import subprocess

#Following will be the ansible group names
group1Name = "AnsibleGroup1"
group2Name = "AnsibleGroup2"

try:
    print("\n =================== Ansible Apache Installer playbook =================== \n")
    selectedOption = int(input('\nPlease enter 1 to install Apache on first group of server. Enter 2 For the other group : '))
    if selectedOption ==1 : 
        
        ansibleCommand="ansible-playbook AnsibleApachePlaybook.yml --extra-vars \"grouping=_AnsibleGroup1\""

    elif selectedOption == 2:

        ansibleCommand="ansible-playbook AnsibleApachePlaybook.yml --extra-vars \"grouping=_AnsibleGroup2\""

        print("\nPlayng ansible playbook for Apache install "+ansibleCommand+"\n")                    
    else:
        print("\nPlease enter 1 or two \n")

    ansibleCommand1ReturnCode = subprocess.call(ansibleCommand, shell=True)
    
except ValueError as err:
    print("\nPlease enter 1 or two \n")