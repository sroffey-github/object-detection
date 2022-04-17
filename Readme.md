
# Object Detection

A git repository containing a python script that can detect objects in an image


## Installation

Install object-detection with bash. First download the `h5` file [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5/)

```bash
  cd object-detection
  pip3 install -r requirements.txt
  pip3 install imageai --upgrade
  python3 app.py <filename>
```

Note: `imageai` will only work with `python <= 3.8`