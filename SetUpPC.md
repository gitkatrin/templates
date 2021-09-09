



**NVIDIA Driver Version anzeigen:**
- ```modinfo nvidia | grep "^version:" | sed 's/^version: *//;'```

**CuDa Version anzeigen:**
- ```nvidia-smi```

**NVIDIA CuDa Toolkit:**
- Version anzeigen: ```nvcc --version```
- Installieren: [hier](https://developer.nvidia.com/cuda-toolkit-archive) herunterladen und Anweisungen folgen (.run-Datei)

**Pip:**
- Version anzeigen: ```pip3 --version```
- Installieren: ```python3 get-pip.py --user```

**Tensorflow:**
- Version anzeigen: ```pip list | grep tensorflow```
- Installieren:
    - ```pip3 install tensorflow```
    - ```pip3 install tensorflow-gpu```