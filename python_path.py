import sys

for p in sys.path:
    print(p)

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
