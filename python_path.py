import sys

for p in sys.path:
    print(p)

"""
C:\Users\<USER>>\projects\main           ← directory of the script you ran
C:\Python312\python312.zip            ← standard library zip
C:\Python312\Lib                      ← standard library folder
C:\Python312\DLLs                     ← C extension modules
C:\Python312                          ← Python install root
C:\Python312\Lib\site-packages        ← third-party packages (pip installs here)
"""

"""The robust pattern is to anchor the path to the script's own location:
project\
├── main\
│   └── main.py      
└── modules\
    └── module.py

"""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(script_dir, '..', 'modules')
sys.path.append(modules_dir)

import module


"""The robust pattern is to anchor the path to the script's own location:
project\
├── main\
│   └── main.py      
└── modules\
    └── module.py
    """
import sys
from pathlib import Path

modules_dir = Path(__file__).resolve().parent.parent / 'modules'
sys.path.append(str(modules_dir))

import module
