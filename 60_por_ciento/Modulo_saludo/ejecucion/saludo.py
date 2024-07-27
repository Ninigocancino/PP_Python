import sys
import os

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_padre = os.path.dirname(dir_actual)

sys.path.append(os.path.join(dir_padre, 'modulo'))

from utilidad import saludar

#saludar()
