import os
import sys

# two-step(..) back for root directory
project_root = os.path.join(os.path.dirname(__file__), '..')
print("Project root: {}".format(project_root))
sys.path.insert(0, project_root)
print("sys.path: {}".format(sys.path)) 