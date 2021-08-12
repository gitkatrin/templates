# Training neuronaler Netze mit GPU

## Allgemeine Informationen
- [Kompatible Versionen: Tensorflow, Python, cuDNN, CUDA](https://www.tensorflow.org/install/source#tested_build_configurations)
- [Kompatible Versionen: NVIDIA Treiber und CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
- [GPU Support (Tensorflow Anleitung)](https://www.tensorflow.org/install/gpu)

## Versionen abfragen
- **Nvidia Treiber** (Version: 455.23.05) jetzt 455.45.01
  - ```modinfo nvidia | grep "^version:" | sed 's/^version: *//;' ```
- **CUDA** (Version: 11.4) brauche 10.1
  - ```nvidia-smi```  
- **cuDNN** (Version: ) brauche 7.6
  - ```einfügen```
- **nvcc** (Version: V9.1.85)
  -  ```nvcc  --version```
- **Tensorflow, Tensorflow-gpu** (Version: 2.3.1)
  - ```pip list | grep tensorflow```  
- **Python** (Version: 3.6.9)
  - ```python3 --version```




# Ablauf
1. [NVIDIA Treiber](https://www.nvidia.com/download/index.aspx?lang=en-us) installieren
2. [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) installieren
  - den Anweisungen folgen und als letzten Befehl nicht ```sudo apt-get -y install cuda``` ausführen, sondern: ```sudo apt install cuda-10.1```
4. [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive) installieren
  - ```tar -xzvf cudnn-10.1-linux-x64-v7.6.5.32.tgz```
  - ``` sudo cp cuda/include/cudnn*.h /usr/local/cuda/include```
  - ``` sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64```
  - ``` sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*```
5. sudo apt install nvidia-cuda-toolkit


sudo apt-get purge nvidia-*
sudo apt-get autoremove
sudo apt-get install cuda

- REMOVE -----------------------------------------------
# Remove existing CuDA versions
sudo apt --purge remove "cublas*" "cuda*"
sudo apt --purge remove "nvidia*"
rm -rf /usr/local/cuda*
sudo apt-get autoremove && sudo apt-get autoclean

# Reboot to remove cached files 
reboot

/usr/local/cuda/bin/cuda-uninstaller
rm -rf /usr/local/cuda-10.0


