import sys
import os

sys.path.insert(0, os.path.join('deps', 'paver-minilib.zip'))

import paver.tasks
paver.tasks.main()
