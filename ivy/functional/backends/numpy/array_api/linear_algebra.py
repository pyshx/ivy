# global
import numpy as np
import ivy as _ivy
from typing import Union, Optional, Tuple, Literal
from collections import namedtuple

# local
from ivy import inf


# noinspection PyUnusedLocal,PyShadowingBuiltins
def vector_norm(x: np.ndarray,
                axis: Optional[Union[int, Tuple[int]]] = None,
                keepdims: bool = False,
                ord: Union[int, float, Literal[inf, - inf]] = 2)\
                 -> np.ndarray:

    if axis is None:
        np_normalized_vector = np.linalg.norm(x.flatten(), ord, axis, keepdims)

    else:
        np_normalized_vector = np.linalg.norm(x, ord, axis, keepdims)

    if np_normalized_vector.shape == tuple():
        return np.expand_dims(np_normalized_vector, 0)
    return np_normalized_vector


def svd(x:np.ndarray,full_matrices: bool = True) -> Union[np.ndarray, Tuple[np.ndarray,...]]:
    results=namedtuple("svd", "U S Vh")
    U, D, VT=np.linalg.svd(x, full_matrices=full_matrices)
    res=results(U, D, VT)
    return res
  
def diagonal(x: np.ndarray,
             offset: int = 0,
             axis1: int = -2,
             axis2: int = -1) -> np.ndarray:
    return np.diagonal(x, offset=offset, axis1=axis1, axis2=axis2)
