from typing import Literal, Optional

def enclose(string:str, enclosure:Literal['equation', 'eqn','in-text', '$'], cmd:Optional[str] = None):
    if enclosure in ['equation', 'eqn']:
        if cmd is None:
            cmd = ""
        else:
            cmd = '\\' + cmd.strip('\\')
    
            
        return "\n\\begin{equation}\n " + string + cmd + "\n\\end{equation}"
    elif enclosure in ['eqn-no-number', 'no-number']:
        return "\n\\[\n " + string + "\n\\]\n"
    elif enclosure in ['in-text', '$']:
        return "$" + string + "$"
    else:
        raise ValueError(f"Enclosure type '{enclosure}' is not a valid enclosure type.")