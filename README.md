# Helm delete release older than some date
This script is made in python and allow you delete releases older than some date.

### How to use the script
Change a variable value in a python script:
```
# Set helm_namespace name and rotate_date
helm_namespace = 'preprod'
rotate_date = 20
```
### How to run the script
```
python helm_delete_old_release.py
```
