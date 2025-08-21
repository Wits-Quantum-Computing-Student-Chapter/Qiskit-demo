from typing import Literal, List, Any, Iterable
import numpy as np

def array2latex(array:np.ndarray|Iterable|Iterable[Iterable], matrix_type:Literal['b', '']='b', fmt_str:str = "{}")->str:
    matrix_str = f"\\begin{{{matrix_type}matrix}}\n"
    for row in array:
        if isinstance(row, Iterable):
            matrix_str += " & ".join([fmt_str.format(v) for v in row]) + '\\\\ \n'
        else:
            matrix_str += f'{row} \\\\ \n'
    matrix_str += f"\\end{{{matrix_type}matrix}}"
    return matrix_str

if __name__=="__main__":
    mat = np.array([[1,2],[3,4]])

    print(array2latex(mat))