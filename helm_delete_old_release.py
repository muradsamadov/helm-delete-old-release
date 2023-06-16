# Import Required Library
import os, time
from datetime import datetime

# Set helm_namespace name and rotate_date
helm_namespace = 'preprod'
rotate_date = 20

# Setting some necessary variables
helm_release_name = os.popen("helm ls --namespace %s | sed  1d | awk -F ' '  '{ print $1 }'" % helm_namespace).read()
helm_release_date = os.popen("helm ls --namespace %s | sed  1d | awk -F ' '  '{ print $4 }'" % helm_namespace).read()
old_value = helm_release_date.replace("-","/")
new_value = old_value.strip()

# current date and time
now = datetime.now() 
current_date = now.strftime("%Y/%m/%d")


list_1 = new_value.split()
list_2 = helm_release_name.split()

res = {}
# Catching helm release names with loop
for i in range(len(list_2)):
    # Catching helm release dates with loop
    for y in range(len(list_1)):
        res[list_2[i]] = list_1[y]
        
        date_1 = datetime.strptime(list_1[y],"%Y/%m/%d")
        date_2 = datetime.strptime(current_date, "%Y/%m/%d")
        common_date = date_2 - date_1
        
        if   rotate_date <= common_date.days:
            os.system('helm uninstall {} --namespace {}'.format(list_2[i],helm_namespace))
            
        del list_1[y]

        break
