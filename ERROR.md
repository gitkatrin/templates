

1. Error:  
Errors were encountered while processing:  
 /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_i386.deb  
 /var/cache/apt/archives/libnvidia-gl-390_390.48-0ubuntu3_amd64.deb  
E: Sub-process /usr/bin/dpkg returned an error code (1)
    - [Solution](https://askubuntu.com/questions/1035409/installing-nvidia-drivers-on-18-04):
      - ```LC_MESSAGES=C dpkg-divert --list '*nvidia-340*' | sed -nre 's/^diversion of (.*) to .*/\1/p' | xargs -rd'\n' -n1 -- sudo dpkg-divert --remove```
      - ```sudo apt --fix-broken install```
    
    
