from dataclasses import dataclass,field
import logging
from yaml import Loader
from yaml import load
import math
logger = logging.getLogger(__name__)


@dataclass
class Analysis:
    fem:int=0
    support:int=0
    p1:tuple[float,float,float]=field(default_factory=tuple)
    v1:tuple[float,float,float]=field(default_factory=tuple)

   
    





@dataclass
class Input:
    analysises:list[Analysis]
    work_folder:str
    sestra_init:str
    sestra_final:str
   
    
def read(file:str)->Input:
    
    pass   