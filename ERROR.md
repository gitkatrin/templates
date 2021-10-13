## Inhalt
1. [Error: E: Sub-process /usr/bin/dpkg returned an error code (1)](https://github.com/gitkatrin/templates/blob/master/ERROR.md#1-error)
2. [Error: E: Sub-process returned an error code](https://github.com/gitkatrin/templates/blob/master/ERROR.md#2-error)
3. [Error: E: Sub-process /usr/bin/dpkg returned an error code (1)](https://github.com/gitkatrin/templates/blob/master/ERROR.md#3-error-e-sub-process-usrbindpkg-returned-an-error-code-1)

## 1. Error: E: Sub-process /usr/bin/dpkg returned an error code (1)
- **Ausgabe:**
  ```
  Errors were encountered while processing:  
   /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_i386.deb  
   /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_amd64.deb  
  E: Sub-process /usr/bin/dpkg returned an error code (1)  
  ```
- **[Lösung](https://askubuntu.com/questions/1035409/installing-nvidia-drivers-on-18-04):**
   - ```LC_MESSAGES=C dpkg-divert --list '*nvidia-340*' | sed -nre 's/^diversion of (.*) to .*/\1/p' | xargs -rd'\n' -n1 -- sudo dpkg-divert --remove```
      - ```sudo apt --fix-broken install```
    
    
## 2. Error: E: Sub-process returned an error code
- **Eingabe:** ```sudo apt-get update && sudo apt-get dist-upgrade```
- **Ausgabe:** 
  ```
  OK:2 http://de.archive.ubuntu.com/ubuntu bionic InRelease                      
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
  E: Sub-process returned an error code
  ```
- **[Lösung](https://unix.stackexchange.com/questions/464445/problem-with-appstreamcli-when-running-apt-update):** 
   -  ```cd /etc/apt/apt.conf.d/```
   -  ```sudo nano ./50command-not-found```
   -  Letzen Zeilen auskommentieren:
      ```
      # Refresh AppStream cache when APT's cache is updated (i.e. apt update)  
      #APT::Update::Post-Invoke-Success {
      #    "if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi";
      #};
      ```
    
## 3. Error: E: Sub-process /usr/bin/dpkg returned an error code (1)
- **Eingabe:** ```sudo apt upgrade```
- **Ausgabe:** 
  ``` 
   ...  
   Fehler traten auf beim Bearbeiten von:  
     python3  
     python3-update-manager  
     software-properties-kde  
     apport-gtk  
     ubuntu-release-upgrader-core  
     python3-apport  
   Bearbeitung wurde angehalten, da zu viele Fehler auftraten.  
   E: Sub-process /usr/bin/dpkg returned an error code (1)
   ```
- **[Lösung](https://forum.ubuntuusers.de/topic/sub-process-usr-bin-dpkg-returned-an-error-cod-7/):**  
   - Aufräumen: ```sudo rm /var/crash/*```
   - Datei mit nano bearbeiten: ```sudo edit /etc/default/apport```
   - Wert 1 auf 0 setzten:
   ```
    # set this to 0 to disable apport, or to 1 to enable it  
    # you can temporarily override this with  
    # sudo service apport start force_start=1  
    enabled=0
    ```
    - ```sudo sed -i s,//de.archive,//archive,g  /etc/apt/sources.list```
    - ```sudo apt update && sudo apt install --reinstall hplip-data```
    - wenn die vorherigen beiden Schritte nicht gehen:
      - ```wget -c http://mirrors.kernel.org/ubuntu/pool/main/h/hplip/hplip-data_3.17.10+repack0-5_all.deb```
      - ```sudo dpkg -i hplip-data_3.17.10+repack0-5_all.deb```


## Notes
- https://blog.desdelinux.net/de/Ersetzen-Sie-Python-3-durch-Python-2-Linux/
- https://qastack.com.de/programming/11068419/check-if-file-is-symlink-in-python
- https://askubuntu.com/questions/448926/how-to-fix-python-installation-is-corrupted
- https://qastack.com.de/ubuntu/448926/how-to-fix-python-installation-is-corrupted
- https://www.cyberciti.biz/faq/upgrade-ubuntu-18-04-to-20-04-lts-using-command-line/
- https://bugs.launchpad.net/ubuntu/+source/gnome-control-center/+bug/133130/comments/3
- https://debianforum.de/forum/viewtopic.php?f=29&t=155566&sid=bcebe1cd39b5a451fd55c69a4c405650&start=15 !!
- http://www.ubuntu-forum.de/artikel/55447/terminal-startet-nicht.html
- https://forum.ubuntuusers.de/topic/aktualisierungsverwaltung-zeigt-auf-meinem-rec/
- https://askubuntu.com/questions/1082881/software-updater-is-not-working-properly
- https://itectec.com/ubuntu/ubuntu-software-updater-software-updates-not-working/
- https://ubuntuhandbook.org/index.php/2020/06/gnome-software-as-ubuntu-software-ubuntu-20-04/
- https://www.cyberciti.biz/faq/ubuntu-bash-do-release-upgrade-command-not-found/
- https://forum.ubuntuusers.de/topic/systemeinstellungen-verschwunden/ !!!
- https://askubuntu.com/questions/480908/problem-with-update-manager-no-module-named-apt-pkg-in-ubuntu-13-10-having-i
- https://qastack.com.de/ubuntu/448926/how-to-fix-python-installation-is-corrupted
- https://qastack.com.de/ubuntu/1104052/your-python3-install-is-corrupted !!
- https://forum.ubuntuusers.de/topic/upgrade-klemmt-wegen-verknuepfung-von-python/ !!
- https://www.cyber-neurones.org/2021/01/ubuntu-crash-de-update-manager/ !!!



- https://forum.ubuntuusers.de/topic/sub-process-usr-bin-dpkg-returned-an-error-cod-8/2/
