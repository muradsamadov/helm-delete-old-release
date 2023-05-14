# Helm delete release older than some date
This script is made in Python and allows you to delete releases older than some date.

### How to use the script
Change a variable value in a Python script:
```
# Set helm_namespace name and rotate_date
helm_namespace = 'preprod'
rotate_date = 20
```
### How to run the script
In this case, Helm will delete releases in 'preprod' namespace that have been running for more than 20 days:
```
python helm_delete_old_release.py
```
### Result
The current date is 2023/05/14 and all releases were deployed on the same day. Before executing the script:
```
helm ls --namespace preprod
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
apache  preprod         1               2023-05-14 10:31:05.1748444 +0400 +04   deployed        apache-9.5.3    2.4.57
nginx   preprod         1               2023-05-14 10:31:13.1972234 +0400 +04   deployed        apache-9.5.3    2.4.57
```
I want to delete releases in 'preprod' namespace older than 20 dates. After executing the script:
```
python helm_delete_old_release.py
release "apache" uninstalled
release "nginx" uninstalled

helm ls --namespace preprod
NAME    NAMESPACE       REVISION        UPDATED STATUS  CHART   APP VERSION
```
