



**NVIDIA Driver Version anzeigen:**
- ```modinfo nvidia | grep "^version:" | sed 's/^version: *//;'```

**CuDa Version anzeigen:**
- ```nvidia-smi```

**NVIDIA CuDa Toolkit:**
- Version anzeigen: ```nvcc --version```
- Installieren: [hier](https://developer.nvidia.com/cuda-toolkit-archive) herunterladen und Anweisungen folgen (.run-Datei)
- weitere Infos gibts [hier](https://github.com/gitkatrin/templates/blob/master/TrainWithGPU.md)

**CuDNN Version anzeigen:**
  - ```function lib_installed() { /sbin/ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep $1; }```
  - ```function check() { lib_installed $1 && echo "$1 is installed" || echo "ERROR: $1 is NOT installed"; }```
  - ```check libcudnn ```
  
**Pip:**
- Version anzeigen: ```pip3 --version```
- Installieren: ```python3 get-pip.py --user```

**Tensorflow:**
- Version anzeigen: ```pip list | grep tensorflow```
- Installieren:
    - ```pip3 install tensorflow```
        - bei dieser Fehlermeldung: ERROR launchpadlib 1.10.6 requires testresources which is not installed
        - ```sudo apt install python3-testresources```
    - ```pip3 install tensorflow-gpu```

**Matplot:**
- Installieren: ```pip3 install matplotlib```

**Sklearn:**
- Installieren: ```pip3 install -U scikit-learn scipy matplotlib```
