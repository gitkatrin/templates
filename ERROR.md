

**1. Error:**  
Errors were encountered while processing:  
 /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_i386.deb  
 /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_amd64.deb  
E: Sub-process /usr/bin/dpkg returned an error code (1)  
    - [Solution](https://askubuntu.com/questions/1035409/installing-nvidia-drivers-on-18-04):
      - ```LC_MESSAGES=C dpkg-divert --list '*nvidia-340*' | sed -nre 's/^diversion of (.*) to .*/\1/p' | xargs -rd'\n' -n1 -- sudo dpkg-divert --remove```
      - ```sudo apt --fix-broken install```
    
    
## 2. Error:
- **Eingabe:** ```sudo apt-get update && sudo apt-get dist-upgrade```
- **Ausgabe:** ```OK:2 http://de.archive.ubuntu.com/ubuntu bionic InRelease                      
OK:3 http://dl.google.com/linux/chrome/deb stable InRelease                    
OK:4 http://de.archive.ubuntu.com/ubuntu bionic-security InRelease             
OK:5 http://de.archive.ubuntu.com/ubuntu bionic-updates InRelease              
OK:6 http://de.archive.ubuntu.com/ubuntu bionic-proposed InRelease             
OK:7 https://packages.microsoft.com/repos/ms-teams stable InRelease            
OK:8 http://de.archive.ubuntu.com/ubuntu bionic-backports InRelease            
OK:1 https://mirror.dogado.de/tex-archive/systems/win32/miktex/setup/deb bionic InRelease
sh: 1: /usr/lib/cnf-update-db: not found            
Paketlisten werden gelesen... Fertig
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code```
- **[Lösung](https://unix.stackexchange.com/questions/464445/problem-with-appstreamcli-when-running-apt-update):** 
   -  ```cd /etc/apt/apt.conf.d/```
   -  ```sudo nano ./50command-not-found```
   -  Letzen Zeilen auskommentieren:
      ```# Refresh AppStream cache when APT's cache is updated (i.e. apt update)  
      #APT::Update::Post-Invoke-Success {
      #    "if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi";
      #};```
    
