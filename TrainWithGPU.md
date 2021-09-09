# Training neuronaler Netze mit GPU

## Allgemeine Informationen
- [Kompatible Versionen: Tensorflow, Python, cuDNN, CUDA](https://www.tensorflow.org/install/source#tested_build_configurations)
- [Kompatible Versionen: NVIDIA Treiber und CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
- [GPU Support (Tensorflow Anleitung)](https://www.tensorflow.org/install/gpu)
- [Nützliche Anleitung mit Test](https://gist.github.com/matheustguimaraes/43e0b65aa534db4df2918f835b9b361d)

## Versionen abfragen
- **Nvidia Treiber** (Version: 455.23.05) jetzt 455.45.01
  - ```modinfo nvidia | grep "^version:" | sed 's/^version: *//;' ```
- **CUDA** (Version: 11.4) brauche 10.1
  - ```nvidia-smi```  

- **CuDNN**
  - ```function lib_installed() { /sbin/ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep $1; }```
  - ```function check() { lib_installed $1 && echo "$1 is installed" || echo "ERROR: $1 is NOT installed"; }```
  - ```check libcudnn ```
- **nvcc (Nvidia Toolkit)** (Version: V9.1.85)
  -  ```nvcc  --version```
- **Tensorflow, Tensorflow-gpu** (Version: 2.3.1)
  - ```pip list | grep tensorflow```  
- **Python** (Version: 3.6.9)
  - ```python3 --version```

# Ablauf
1. **NVIDIA Treiber installieren/aktivieren**
    - [installieren](https://www.nvidia.com/download/index.aspx?lang=en-us)
    - aktivieren unter: Anwendungen & Aktualisierungen > Zusätzliche Treiber > NVIDIA driver metapackage nvidia-driver-470...
 
2. **[CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) installieren**
    - die .run Datei runterladen
    - Nvidia Driver nicht mit installieren
    - Nach Installation PATH ändern und Umgebungsvariablen ändern
      - ```export PATH=/usr/local/cuda-11.4/bin${PATH:+:${PATH}}```
      - ```export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64\```  
          ```${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}```

3. **[cuDNN](https://developer.nvidia.com/rdp/cudnn-archive) installieren**
    - Konto anlegen oder login bei https://developer.nvidia.com/cudnn
    - Passende .deb-Dateien downloaden
      - cuDNN Runtime Library for Ubuntu20.04 x86_64 (Deb)
      - cuDNN Developer Library for Ubuntu20.04 x86_64 (Deb)
      - cuDNN Code Samples and User Guide for Ubuntu20.04 x86_64 (Deb) 
    - in den Download Ordner navigieren
      - ```cd Downloads```
    - Pakete entpacken und installieren
      - ```sudo dpkg -i libcudnn8_8.2.4.15-1+cuda11.4_amd64.deb```
      - ```sudo dpkg -i libcudnn8-dev_8.2.4.15-1+cuda11.4_amd64.deb```
      - ```sudo dpkg -i libcudnn8-samples_8.2.4.15-1+cuda11.4_amd64.deb```
    - Cuda path exportieren
      - ```export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH```
      - ```export PATH=/usr/local/cuda-11.4/bin:$PATH```

//    - ```tar -xzvf cudnn-10.1-linux-x64-v7.6.5.32.tgz```
    - ``` sudo cp cuda/include/cudnn*.h /usr/local/cuda/include```
    - ``` sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64```
    - ``` sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*```
//5. sudo apt install nvidia-cuda-toolkit
//6. Separates **cublas lib** Paket installieren und manuell zu installieren:
//  - entweder download:
      - https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/libcublas10_10.1.0.105-1_amd64.deb
      - ```sudo dpkg -i libcublas10_10.1.0.105-1_amd64.deb```
    - oder kopieren:
      - Terminal aus folgendem Ordner öffnen: /usr/loal/cuda-10.2/lib64
      - ```sudo cp /libcublas.so.10 /usr/local/cuda-10.1/lib64/```
    - oder:
      - im Terminal: ```cd /``` um in ~/.bashrc zu kommen
      - ```export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}```
      
4. **TensorFlow installieren**
    - ```pip install tensorflow```
      - bei dieser Fehlermeldung: ERROR launchpadlib 1.10.6 requires testresources which is not installed  
        ```sudo apt install python3-testresources```
    - ```pip install tensorflow-gpu``` 


sudo apt-get purge nvidia-*
sudo apt-get autoremove
sudo apt-get install cuda

- REMOVE -----------------------------------------------
# Remove existing CuDA versions
1. ```sudo apt --purge remove "cublas*" "cuda*"```
2. ```sudo apt --purge remove "nvidia*"```
3. ```rm -rf /usr/local/cuda*```
4. ```sudo apt-get autoremove && sudo apt-get autoclean```

# Reboot to remove cached files 
5. ```reboot```

/usr/local/cuda/bin/cuda-uninstaller
rm -rf /usr/local/cuda-10.0


