import pickle
from dataclasses import dataclass
from feminterface.fem.write import WRITE
from feminterface.fem.fem_modification import UPDATE

from feminterface.func.node_func import NODE_FUNC
from feminterface.func.element_func import ELEMENT_FUNC
from feminterface.func.set_func import SET_FUNC
from feminterface.func.load_func import LOAD_FUNC

#from fem_base import FEM_BASE
from feminterface.fem.read import READ
@dataclass(frozen=False)
class FEM(READ,WRITE,NODE_FUNC,ELEMENT_FUNC,UPDATE,SET_FUNC,LOAD_FUNC):


    def save_obj(self,name:str)->None:
        with open(f'{name}', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
    
def load_obj(name)->FEM:   
    with open(f'{name}', 'rb') as f:
        return pickle.load(f) 

