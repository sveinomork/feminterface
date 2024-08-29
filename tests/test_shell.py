from feminterface.fem.fem import FEM
from feminterface.fem.shell import SHELL
fem_obj_3d=FEM()
fem_obj_2d=FEM()
fem_obj_3d.read_fem(r'T100.fem')

sh=SHELL(fem_obj_3d,fem_obj_2d)

