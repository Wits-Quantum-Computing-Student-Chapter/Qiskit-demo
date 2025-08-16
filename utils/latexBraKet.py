"""
A series of function to do braket formatting in latex
"""

from typing import Literal, Optional, Any

from utils.enclose_latex import enclose

def bra(val:str|Any, enclosure:Optional[Literal['equation', 'eqn','in-text', '$']] = None, cmd:Optional[str]=None):
    """
    Formats the given string as a latex bra '< |'
    """
    bra_str = f"\\left\\langle {val}\\right|"

    if enclosure is not None:
        bra_str = enclose(bra_str, enclosure, cmd)

    return bra_str

def ket(val:str|Any, enclosure:Optional[Literal['equation', 'eqn','in-text', '$']] = None, cmd:Optional[str]=None):
    """
    Formats the given string as a latex ket '| >'
    """
    ket_str = f"\\left|{val}\\right\\rangle"
    if enclosure is not None:
        ket_str = enclose(ket_str, enclosure, cmd)

    return ket_str

def braket(bra_val:str|Any, ket_val:str|Any, enclosure:Optional[Literal['equation', 'eqn','in-text', '$']] = None, cmd:Optional[str]=None):
    """
    Formats the given string as a latex bra-ket '<bra|ket>'
    """
    bra_ket_str = f"\\left\\langle {bra_val}\\middle| {ket_val}\\right\\rangle"
    if enclosure is not None:
        bra_ket_str = enclose(bra_ket_str, enclosure, cmd)
    return bra_ket_str

def ketbra(ket_val:str|Any, bra_val:str|Any, enclosure:Optional[Literal['equation', 'eqn','in-text', '$']] = None, cmd:Optional[str]=None):
    """
    Formats the given string as a latex ket-bre '|ket><bra|'
    """
    ket_bra_str = ket(ket_val,None)+bra(bra_val,None)
    if enclosure is not None:
        ket_bra_str = enclose(ket_bra_str, enclosure, cmd)
    return ket_bra_str