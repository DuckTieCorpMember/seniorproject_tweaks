import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.base as _mod_scipy_sparse_base
import scipy.sparse.csc as _mod_scipy_sparse_csc

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
SparseEfficiencyWarning = _mod_scipy_sparse_base.SparseEfficiencyWarning
__builtins__ = {}
__doc__ = None
__file__ = '/usr/lib/python3/dist-packages/scipy/sparse/csgraph/_reordering.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.csgraph._reordering'
__package__ = 'scipy.sparse.csgraph'
__test__ = _mod_builtins.dict()
def _maximum_bipartite_matching(inds, ptrs, n):
    '\n    Maximum bipartite matching of a graph in CSC format.\n    '
    pass

def _reverse_cuthill_mckee(ind, ptr, num_rows):
    '\n    Reverse Cuthill-McKee ordering of a sparse symmetric CSR or CSC matrix.  \n    We follow the original Cuthill-McKee paper and always start the routine\n    at a node of lowest degree for each connected component.\n    '
    pass

csc_matrix = _mod_scipy_sparse_csc.csc_matrix
def isspmatrix(x):
    pass

def isspmatrix_coo(x):
    pass

def isspmatrix_csc(x):
    pass

def isspmatrix_csr(x):
    pass

def maximum_bipartite_matching():
    '\n    maximum_bipartite_matching(graph, perm_type=\'row\')\n    \n    Returns an array of row or column permutations that makes\n    the diagonal of a nonsingular square CSC sparse matrix zero free.  \n    \n    Such a permutation is always possible provided that the matrix \n    is nonsingular. This function looks at the structure of the matrix \n    only. The input matrix will be converted to CSC matrix format if\n    necessary.\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSC format\n    perm_type : str, {\'row\', \'column\'}\n        Type of permutation to generate.\n\n    Returns\n    -------\n    perm : ndarray\n        Array of row or column permutations.\n\n    Notes\n    -----\n    This function relies on a maximum cardinality bipartite matching \n    algorithm based on a breadth-first search (BFS) of the underlying \n    graph.\n\n    .. versionadded:: 0.15.0\n\n    References\n    ----------\n    I. S. Duff, K. Kaya, and B. Ucar, "Design, Implementation, and \n    Analysis of Maximum Transversal Algorithms", ACM Trans. Math. Softw.\n    38, no. 2, (2011).\n\n    '
    pass

def reverse_cuthill_mckee():
    '\n    reverse_cuthill_mckee(graph, symmetric_mode=False)\n    \n    Returns the permutation array that orders a sparse CSR or CSC matrix\n    in Reverse-Cuthill McKee ordering.  \n    \n    It is assumed by default, ``symmetric_mode=False``, that the input matrix \n    is not symmetric and works on the matrix ``A+A.T``. If you are \n    guaranteed that the matrix is symmetric in structure (values of matrix \n    elements do not matter) then set ``symmetric_mode=True``.\n    \n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSC or CSR sparse matrix format.\n    symmetric_mode : bool, optional\n        Is input matrix guaranteed to be symmetric.\n\n    Returns\n    -------\n    perm : ndarray\n        Array of permuted row and column indices.\n \n    Notes\n    -----\n    .. versionadded:: 0.15.0\n\n    References\n    ----------\n    E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",\n    ACM \'69 Proceedings of the 1969 24th national conference, (1969).\n    \n    '
    pass

def structural_rank():
    '\n    structural_rank(graph)\n    \n    Compute the structural rank of a graph (matrix) with a given \n    sparsity pattern.\n\n    The structural rank of a matrix is the number of entries in the maximum \n    transversal of the corresponding bipartite graph, and is an upper bound \n    on the numerical rank of the matrix. A graph has full structural rank \n    if it is possible to permute the elements to make the diagonal zero-free.\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse matrix.\n\n    Returns\n    -------\n    rank : int\n        The structural rank of the sparse graph.\n\n    .. versionadded:: 0.19.0\n    \n    References\n    ----------\n    .. [1] I. S. Duff, "Computing the Structural Index", SIAM J. Alg. Disc. \n            Meth., Vol. 7, 594 (1986).\n    \n    .. [2] http://www.cise.ufl.edu/research/sparse/matrices/legend.html\n    '
    pass

def warn():
    'Issue a warning, or maybe ignore it or raise an exception.'
    pass

