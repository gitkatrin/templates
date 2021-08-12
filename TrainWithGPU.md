# Training neuronaler Netze mit GPU

## Allgemeine Informationen
- [Kompatible Versionen: Tensorflow, Python, cuDNN, CUDA](https://www.tensorflow.org/install/source#tested_build_configurations)
- [Kompatible Versionen: NVIDIA Treiber und CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
- [GPU Support (Tensorflow Anleitung)](https://www.tensorflow.org/install/gpu)

## Versionen abfragen
- **Nvidia Treiber** (Version: 455.23.05)
  - ```modinfo nvidia | grep "^version:" | sed 's/^version: *//;' ```
- **CUDA** (Version: 11.1) brauche 10.1
  - ```nvidia-smi```  
- **Tensorflow, Tensorflow-gpu** (Version: 2.3.1)
  - ```pip list | grep tensorflow```  



# Ablauf
1. [NVIDIA Treiber](https://www.nvidia.com/download/index.aspx?lang=en-us) installieren
2. [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) installieren

