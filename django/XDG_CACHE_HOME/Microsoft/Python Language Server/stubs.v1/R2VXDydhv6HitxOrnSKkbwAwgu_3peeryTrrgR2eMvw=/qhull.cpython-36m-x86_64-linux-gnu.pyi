import builtins as _mod_builtins

class ConvexHull(_QhullUser):
    '\n    ConvexHull(points, incremental=False, qhull_options=None)\n\n    Convex hulls in N dimensions.\n\n    .. versionadded:: 0.12.0\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to construct a convex hull from\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qx" for ndim > 4 and "" otherwise)\n        Option "Qt" is always enabled.\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    vertices : ndarray of ints, shape (nvertices,)\n        Indices of points forming the vertices of the convex hull.\n        For 2-D convex hulls, the vertices are in counterclockwise order.\n        For other dimensions, they are in input order.\n    simplices : ndarray of ints, shape (nfacet, ndim)\n        Indices of points forming the simplical facets of the convex hull.\n    neighbors : ndarray of ints, shape (nfacet, ndim)\n        Indices of neighbor facets for each facet.\n        The kth neighbor is opposite to the kth vertex.\n        -1 denotes no neighbor.\n    equations : ndarray of double, shape (nfacet, ndim+1)\n        [normal, offset] forming the hyperplane equation of the facet\n        (see `Qhull documentation <http://www.qhull.org/>`__  for more).\n    coplanar : ndarray of int, shape (ncoplanar, 3)\n        Indices of coplanar points and the corresponding indices of\n        the nearest facets and nearest vertex indices.  Coplanar\n        points are input points which were *not* included in the\n        triangulation due to numerical precision issues.\n\n        If option "Qc" is not specified, this list is not computed.\n    area : float\n        Area of the convex hull\n    volume : float\n        Volume of the convex hull\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The convex hull is computed using the \n    `Qhull library <http://www.qhull.org/>`__.\n\n    Examples\n    --------\n\n    Convex hull of a random set of points:\n\n    >>> from scipy.spatial import ConvexHull\n    >>> points = np.random.rand(30, 2)   # 30 random points in 2-D\n    >>> hull = ConvexHull(points)\n\n    Plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> plt.plot(points[:,0], points[:,1], \'o\')\n    >>> for simplex in hull.simplices:\n    ...     plt.plot(points[simplex, 0], points[simplex, 1], \'k-\')\n\n    We could also have directly used the vertices of the hull, which\n    for 2-D are guaranteed to be in counterclockwise order:\n\n    >>> plt.plot(points[hull.vertices,0], points[hull.vertices,1], \'r--\', lw=2)\n    >>> plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], \'ro\')\n    >>> plt.show()\n\n    References\n    ----------\n    .. [Qhull] http://www.qhull.org/\n\n    '
    __class__ = ConvexHull
    def __del__(self):
        return None
    
    __dict__ = {}
    def __init__(self, points, incremental, qhull_options):
        '\n    ConvexHull(points, incremental=False, qhull_options=None)\n\n    Convex hulls in N dimensions.\n\n    .. versionadded:: 0.12.0\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to construct a convex hull from\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qx" for ndim > 4 and "" otherwise)\n        Option "Qt" is always enabled.\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    vertices : ndarray of ints, shape (nvertices,)\n        Indices of points forming the vertices of the convex hull.\n        For 2-D convex hulls, the vertices are in counterclockwise order.\n        For other dimensions, they are in input order.\n    simplices : ndarray of ints, shape (nfacet, ndim)\n        Indices of points forming the simplical facets of the convex hull.\n    neighbors : ndarray of ints, shape (nfacet, ndim)\n        Indices of neighbor facets for each facet.\n        The kth neighbor is opposite to the kth vertex.\n        -1 denotes no neighbor.\n    equations : ndarray of double, shape (nfacet, ndim+1)\n        [normal, offset] forming the hyperplane equation of the facet\n        (see `Qhull documentation <http://www.qhull.org/>`__  for more).\n    coplanar : ndarray of int, shape (ncoplanar, 3)\n        Indices of coplanar points and the corresponding indices of\n        the nearest facets and nearest vertex indices.  Coplanar\n        points are input points which were *not* included in the\n        triangulation due to numerical precision issues.\n\n        If option "Qc" is not specified, this list is not computed.\n    area : float\n        Area of the convex hull\n    volume : float\n        Volume of the convex hull\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The convex hull is computed using the \n    `Qhull library <http://www.qhull.org/>`__.\n\n    Examples\n    --------\n\n    Convex hull of a random set of points:\n\n    >>> from scipy.spatial import ConvexHull\n    >>> points = np.random.rand(30, 2)   # 30 random points in 2-D\n    >>> hull = ConvexHull(points)\n\n    Plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> plt.plot(points[:,0], points[:,1], \'o\')\n    >>> for simplex in hull.simplices:\n    ...     plt.plot(points[simplex, 0], points[simplex, 1], \'k-\')\n\n    We could also have directly used the vertices of the hull, which\n    for 2-D are guaranteed to be in counterclockwise order:\n\n    >>> plt.plot(points[hull.vertices,0], points[hull.vertices,1], \'r--\', lw=2)\n    >>> plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], \'ro\')\n    >>> plt.show()\n\n    References\n    ----------\n    .. [Qhull] http://www.qhull.org/\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_points(self, points, restart, interior_point):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def _update(self, qhull):
        pass
    
    def add_points(self, points, restart):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def close(self):
        '\n        close()\n\n        Finish incremental processing.\n\n        Call this to free resources taken up by Qhull, when using the\n        incremental mode. After calling this, adding more points is no\n        longer possible.\n        '
        pass
    
    points = _mod_builtins.property()
    vertices = _mod_builtins.property()

class Delaunay(_QhullUser):
    '\n    Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)\n\n    Delaunay tesselation in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to triangulate\n    furthest_site : bool, optional\n        Whether to compute a furthest-site Delaunay triangulation.\n        Default: False\n\n        .. versionadded:: 0.12.0\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual for\n        details. Option "Qt" is always enabled.\n        Default:"Qbb Qc Qz Qx Q12" for ndim > 4 and "Qbb Qc Qz Q12" otherwise.\n        Incremental mode omits "Qz".\n\n        .. versionadded:: 0.12.0\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    simplices : ndarray of ints, shape (nsimplex, ndim+1)\n        Indices of the points forming the simplices in the triangulation.\n        For 2-D, the points are oriented counterclockwise.\n    neighbors : ndarray of ints, shape (nsimplex, ndim+1)\n        Indices of neighbor simplices for each simplex.\n        The kth neighbor is opposite to the kth vertex.\n        For simplices at the boundary, -1 denotes no neighbor.\n    equations : ndarray of double, shape (nsimplex, ndim+2)\n        [normal, offset] forming the hyperplane equation of the facet\n        on the paraboloid\n        (see `Qhull documentation <http://www.qhull.org/>`__ for more).\n    paraboloid_scale, paraboloid_shift : float\n        Scale and shift for the extra paraboloid dimension\n        (see `Qhull documentation <http://www.qhull.org/>`__ for more).\n    transform : ndarray of double, shape (nsimplex, ndim+1, ndim)\n        Affine transform from ``x`` to the barycentric coordinates ``c``.\n        This is defined by::\n\n            T c = x - r\n\n        At vertex ``j``, ``c_j = 1`` and the other coordinates zero.\n\n        For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains\n        inverse of the matrix ``T``, and ``transform[i,ndim,:]``\n        contains the vector ``r``.\n\n        If the simplex is degenerate or nearly degenerate, its\n        barycentric transform contains NaNs.\n    vertex_to_simplex : ndarray of int, shape (npoints,)\n        Lookup array, from a vertex, to some simplex which it is a part of.\n        If qhull option "Qc" was not specified, the list will contain -1\n        for points that are not vertices of the tesselation.\n    convex_hull : ndarray of int, shape (nfaces, ndim)\n        Vertices of facets forming the convex hull of the point set.\n        The array contains the indices of the points belonging to\n        the (N-1)-dimensional facets that form the convex hull\n        of the triangulation.\n\n        .. note::\n\n           Computing convex hulls via the Delaunay triangulation is\n           inefficient and subject to increased numerical instability.\n           Use `ConvexHull` instead.\n    coplanar : ndarray of int, shape (ncoplanar, 3)\n        Indices of coplanar points and the corresponding indices of\n        the nearest facet and the nearest vertex.  Coplanar\n        points are input points which were *not* included in the\n        triangulation due to numerical precision issues.\n\n        If option "Qc" is not specified, this list is not computed.\n\n        .. versionadded:: 0.12.0\n    vertices\n        Same as `simplices`, but deprecated.\n    vertex_neighbor_vertices : tuple of two ndarrays of int; (indices, indptr)\n        Neighboring vertices of vertices. The indices of neighboring\n        vertices of vertex `k` are ``indptr[indices[k]:indices[k+1]]``.\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The tesselation is computed using the Qhull library \n    `Qhull library <http://www.qhull.org/>`__.\n\n    .. note::\n\n       Unless you pass in the Qhull option "QJ", Qhull does not\n       guarantee that each input point appears as a vertex in the\n       Delaunay triangulation. Omitted points are listed in the\n       `coplanar` attribute.\n\n    Examples\n    --------\n    Triangulation of a set of points:\n\n    >>> points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])\n    >>> from scipy.spatial import Delaunay\n    >>> tri = Delaunay(points)\n\n    We can plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> plt.triplot(points[:,0], points[:,1], tri.simplices.copy())\n    >>> plt.plot(points[:,0], points[:,1], \'o\')\n    >>> plt.show()\n\n    Point indices and coordinates for the two triangles forming the\n    triangulation:\n\n    >>> tri.simplices\n    array([[2, 3, 0],                 # may vary\n           [3, 1, 0]], dtype=int32)\n\n    Note that depending on how rounding errors go, the simplices may\n    be in a different order than above.\n\n    >>> points[tri.simplices]\n    array([[[ 1. ,  0. ],            # may vary\n            [ 1. ,  1. ],\n            [ 0. ,  0. ]],\n           [[ 1. ,  1. ],\n            [ 0. ,  1.1],\n            [ 0. ,  0. ]]])\n\n    Triangle 0 is the only neighbor of triangle 1, and it\'s opposite to\n    vertex 1 of triangle 1:\n\n    >>> tri.neighbors[1]\n    array([-1,  0, -1], dtype=int32)\n    >>> points[tri.simplices[1,1]]\n    array([ 0. ,  1.1])\n\n    We can find out which triangle points are in:\n\n    >>> p = np.array([(0.1, 0.2), (1.5, 0.5), (0.5, 1.05)])\n    >>> tri.find_simplex(p)\n    array([ 1, -1, 1], dtype=int32)\n\n    We can also compute barycentric coordinates in triangle 1 for\n    these points:\n\n    >>> b = tri.transform[1,:2].dot(np.transpose(p - tri.transform[1,2]))\n    >>> np.c_[np.transpose(b), 1 - b.sum(axis=0)]\n    array([[ 0.1       ,  0.09090909,  0.80909091],\n           [ 1.5       , -0.90909091,  0.40909091],\n           [ 0.5       ,  0.5       ,  0.        ]])\n\n    The coordinates for the first point are all positive, meaning it\n    is indeed inside the triangle. The third point is on a vertex,\n    hence its null third coordinate.\n\n    '
    __class__ = Delaunay
    def __del__(self):
        return None
    
    __dict__ = {}
    def __init__(self, points, furthest_site, incremental, qhull_options):
        '\n    Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)\n\n    Delaunay tesselation in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to triangulate\n    furthest_site : bool, optional\n        Whether to compute a furthest-site Delaunay triangulation.\n        Default: False\n\n        .. versionadded:: 0.12.0\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual for\n        details. Option "Qt" is always enabled.\n        Default:"Qbb Qc Qz Qx Q12" for ndim > 4 and "Qbb Qc Qz Q12" otherwise.\n        Incremental mode omits "Qz".\n\n        .. versionadded:: 0.12.0\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    simplices : ndarray of ints, shape (nsimplex, ndim+1)\n        Indices of the points forming the simplices in the triangulation.\n        For 2-D, the points are oriented counterclockwise.\n    neighbors : ndarray of ints, shape (nsimplex, ndim+1)\n        Indices of neighbor simplices for each simplex.\n        The kth neighbor is opposite to the kth vertex.\n        For simplices at the boundary, -1 denotes no neighbor.\n    equations : ndarray of double, shape (nsimplex, ndim+2)\n        [normal, offset] forming the hyperplane equation of the facet\n        on the paraboloid\n        (see `Qhull documentation <http://www.qhull.org/>`__ for more).\n    paraboloid_scale, paraboloid_shift : float\n        Scale and shift for the extra paraboloid dimension\n        (see `Qhull documentation <http://www.qhull.org/>`__ for more).\n    transform : ndarray of double, shape (nsimplex, ndim+1, ndim)\n        Affine transform from ``x`` to the barycentric coordinates ``c``.\n        This is defined by::\n\n            T c = x - r\n\n        At vertex ``j``, ``c_j = 1`` and the other coordinates zero.\n\n        For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains\n        inverse of the matrix ``T``, and ``transform[i,ndim,:]``\n        contains the vector ``r``.\n\n        If the simplex is degenerate or nearly degenerate, its\n        barycentric transform contains NaNs.\n    vertex_to_simplex : ndarray of int, shape (npoints,)\n        Lookup array, from a vertex, to some simplex which it is a part of.\n        If qhull option "Qc" was not specified, the list will contain -1\n        for points that are not vertices of the tesselation.\n    convex_hull : ndarray of int, shape (nfaces, ndim)\n        Vertices of facets forming the convex hull of the point set.\n        The array contains the indices of the points belonging to\n        the (N-1)-dimensional facets that form the convex hull\n        of the triangulation.\n\n        .. note::\n\n           Computing convex hulls via the Delaunay triangulation is\n           inefficient and subject to increased numerical instability.\n           Use `ConvexHull` instead.\n    coplanar : ndarray of int, shape (ncoplanar, 3)\n        Indices of coplanar points and the corresponding indices of\n        the nearest facet and the nearest vertex.  Coplanar\n        points are input points which were *not* included in the\n        triangulation due to numerical precision issues.\n\n        If option "Qc" is not specified, this list is not computed.\n\n        .. versionadded:: 0.12.0\n    vertices\n        Same as `simplices`, but deprecated.\n    vertex_neighbor_vertices : tuple of two ndarrays of int; (indices, indptr)\n        Neighboring vertices of vertices. The indices of neighboring\n        vertices of vertex `k` are ``indptr[indices[k]:indices[k+1]]``.\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The tesselation is computed using the Qhull library \n    `Qhull library <http://www.qhull.org/>`__.\n\n    .. note::\n\n       Unless you pass in the Qhull option "QJ", Qhull does not\n       guarantee that each input point appears as a vertex in the\n       Delaunay triangulation. Omitted points are listed in the\n       `coplanar` attribute.\n\n    Examples\n    --------\n    Triangulation of a set of points:\n\n    >>> points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])\n    >>> from scipy.spatial import Delaunay\n    >>> tri = Delaunay(points)\n\n    We can plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> plt.triplot(points[:,0], points[:,1], tri.simplices.copy())\n    >>> plt.plot(points[:,0], points[:,1], \'o\')\n    >>> plt.show()\n\n    Point indices and coordinates for the two triangles forming the\n    triangulation:\n\n    >>> tri.simplices\n    array([[2, 3, 0],                 # may vary\n           [3, 1, 0]], dtype=int32)\n\n    Note that depending on how rounding errors go, the simplices may\n    be in a different order than above.\n\n    >>> points[tri.simplices]\n    array([[[ 1. ,  0. ],            # may vary\n            [ 1. ,  1. ],\n            [ 0. ,  0. ]],\n           [[ 1. ,  1. ],\n            [ 0. ,  1.1],\n            [ 0. ,  0. ]]])\n\n    Triangle 0 is the only neighbor of triangle 1, and it\'s opposite to\n    vertex 1 of triangle 1:\n\n    >>> tri.neighbors[1]\n    array([-1,  0, -1], dtype=int32)\n    >>> points[tri.simplices[1,1]]\n    array([ 0. ,  1.1])\n\n    We can find out which triangle points are in:\n\n    >>> p = np.array([(0.1, 0.2), (1.5, 0.5), (0.5, 1.05)])\n    >>> tri.find_simplex(p)\n    array([ 1, -1, 1], dtype=int32)\n\n    We can also compute barycentric coordinates in triangle 1 for\n    these points:\n\n    >>> b = tri.transform[1,:2].dot(np.transpose(p - tri.transform[1,2]))\n    >>> np.c_[np.transpose(b), 1 - b.sum(axis=0)]\n    array([[ 0.1       ,  0.09090909,  0.80909091],\n           [ 1.5       , -0.90909091,  0.40909091],\n           [ 0.5       ,  0.5       ,  0.        ]])\n\n    The coordinates for the first point are all positive, meaning it\n    is indeed inside the triangle. The third point is on a vertex,\n    hence its null third coordinate.\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_points(self, points, restart, interior_point):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def _update(self, qhull):
        pass
    
    def add_points(self, points, restart):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def close(self):
        '\n        close()\n\n        Finish incremental processing.\n\n        Call this to free resources taken up by Qhull, when using the\n        incremental mode. After calling this, adding more points is no\n        longer possible.\n        '
        pass
    
    convex_hull = _mod_builtins.property()
    def find_simplex(self, xi, bruteforce, tol):
        "\n        find_simplex(self, xi, bruteforce=False, tol=None)\n\n        Find the simplices containing the given points.\n\n        Parameters\n        ----------\n        tri : DelaunayInfo\n            Delaunay triangulation\n        xi : ndarray of double, shape (..., ndim)\n            Points to locate\n        bruteforce : bool, optional\n            Whether to only perform a brute-force search\n        tol : float, optional\n            Tolerance allowed in the inside-triangle check.\n            Default is ``100*eps``.\n\n        Returns\n        -------\n        i : ndarray of int, same shape as `xi`\n            Indices of simplices containing each point.\n            Points outside the triangulation get the value -1.\n\n        Notes\n        -----\n        This uses an algorithm adapted from Qhull's ``qh_findbestfacet``,\n        which makes use of the connection between a convex hull and a\n        Delaunay triangulation. After finding the simplex closest to\n        the point in N+1 dimensions, the algorithm falls back to\n        directed search in N dimensions.\n\n        "
        pass
    
    def lift_points(self, x):
        '\n        lift_points(self, x)\n\n        Lift points to the Qhull paraboloid.\n\n        '
        pass
    
    def plane_distance(self, xi):
        '\n        plane_distance(self, xi)\n\n        Compute hyperplane distances to the point `xi` from all simplices.\n\n        '
        pass
    
    points = _mod_builtins.property()
    transform = _mod_builtins.property()
    vertex_neighbor_vertices = _mod_builtins.property()
    vertex_to_simplex = _mod_builtins.property()

class HalfspaceIntersection(_QhullUser):
    '\n    HalfspaceIntersection(halfspaces, interior_point, incremental=False, qhull_options=None)\n\n    Halfspace intersections in N dimensions.\n\n    .. versionadded:: 0.19.0\n\n    Parameters\n    ----------\n    halfspaces : ndarray of floats, shape (nineq, ndim+1)\n        Stacked Inequalities of the form Ax + b <= 0 in format [A; b]\n    interior_point : ndarray of floats, shape (ndim,)\n        Point clearly inside the region defined by halfspaces. Also called a feasible\n        point, it can be obtained by linear programming.\n    incremental : bool, optional\n        Allow adding new halfspaces incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qx" for ndim > 4 and "" otherwise)\n        Option "H" is always enabled.\n\n    Attributes\n    ----------\n    halfspaces : ndarray of double, shape (nineq, ndim+1)\n        Input halfspaces.\n    interior_point :ndarray of floats, shape (ndim,)\n        Input interior point.\n    intersections : ndarray of double, shape (ninter, ndim)\n        Intersections of all halfspaces.\n    dual_points : ndarray of double, shape (nineq, ndim)\n        Dual points of the input halfspaces.\n    dual_facets : list of lists of ints\n        Indices of points forming the (non necessarily simplicial) facets of\n        the dual convex hull.\n    dual_vertices : ndarray of ints, shape (nvertices,)\n        Indices of halfspaces forming the vertices of the dual convex hull.\n        For 2-D convex hulls, the vertices are in counterclockwise order.\n        For other dimensions, they are in input order.\n    dual_equations : ndarray of double, shape (nfacet, ndim+1)\n        [normal, offset] forming the hyperplane equation of the dual facet\n        (see `Qhull documentation <http://www.qhull.org/>`__  for more).\n    dual_area : float\n        Area of the dual convex hull\n    dual_volume : float\n        Volume of the dual convex hull\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The intersections are computed using the\n    `Qhull library <http://www.qhull.org/>`__.\n    This reproduces the "qhalf" functionality of Qhull.\n\n    Examples\n    --------\n\n    Halfspace intersection of planes forming some polygon\n\n    >>> from scipy.spatial import HalfspaceIntersection\n    >>> import numpy as np\n    >>> halfspaces = np.array([[-1, 0., 0.],\n    ...                        [0., -1., 0.],\n    ...                        [2., 1., -4.],\n    ...                        [-0.5, 1., -2.]])\n    >>> feasible_point = np.array([0.5, 0.5])\n    >>> hs = HalfspaceIntersection(halfspaces, feasible_point)\n\n    Plot halfspaces as filled regions and intersection points:\n\n    >>> import matplotlib.pyplot as plt\n    >>> fig = plt.figure()\n    >>> ax = fig.add_subplot(\'111\', aspect=\'equal\')\n    >>> xlim, ylim = (-1, 3), (-1, 3)\n    >>> ax.set_xlim(xlim)\n    >>> ax.set_ylim(ylim)\n    >>> x = np.linspace(-1, 3, 100)\n    >>> symbols = [\'-\', \'+\', \'x\', \'*\']\n    >>> signs = [0, 0, -1, -1]\n    >>> fmt = {"color": None, "edgecolor": "b", "alpha": 0.5}\n    >>> for h, sym, sign in zip(halfspaces, symbols, signs):\n    ...     hlist = h.tolist()\n    ...     fmt["hatch"] = sym\n    ...     if h[1]== 0:\n    ...         ax.axvline(-h[2]/h[0], label=\'{}x+{}y+{}=0\'.format(*hlist))\n    ...         xi = np.linspace(xlim[sign], -h[2]/h[0], 100)\n    ...         ax.fill_between(xi, ylim[0], ylim[1], **fmt)\n    ...     else:\n    ...         ax.plot(x, (-h[2]-h[0]*x)/h[1], label=\'{}x+{}y+{}=0\'.format(*hlist))\n    ...         ax.fill_between(x, (-h[2]-h[0]*x)/h[1], ylim[sign], **fmt)\n    >>> x, y = zip(*hs.intersections)\n    >>> ax.plot(x, y, \'o\', markersize=8)\n\n    By default, qhull does not provide with a way to compute an interior point.\n    This can easily be computed using linear programming. Considering halfspaces\n    of the form :math:`Ax + b \\leq 0`, solving the linear program:\n\n    .. math::\n\n        max \\: y\n\n        s.t. Ax + y ||A_i|| \\leq -b\n\n    With :math:`A_i` being the rows of A, i.e. the normals to each plane.\n\n    Will yield a point x that is furthest inside the convex polyhedron. To\n    be precise, it is the center of the largest hypersphere of radius y\n    inscribed in the polyhedron. This point is called the Chebyshev center\n    of the polyhedron (see [1]_ 4.3.1, pp148-149). The\n    equations outputted by Qhull are always normalized.\n\n    >>> from scipy.optimize import linprog\n    >>> from matplotlib.patches import Circle\n    >>> norm_vector = np.reshape(np.linalg.norm(halfspaces[:, :-1], axis=1),\n    ...     (halfspaces.shape[0], 1))\n    >>> c = np.zeros((halfspaces.shape[1],))\n    >>> c[-1] = -1\n    >>> A = np.hstack((halfspaces[:, :-1], norm_vector))\n    >>> b = - halfspaces[:, -1:]\n    >>> res = linprog(c, A_ub=A, b_ub=b)\n    >>> x = res.x[:-1]\n    >>> y = res.x[-1]\n    >>> circle = Circle(x, radius=y, alpha=0.3)\n    >>> ax.add_patch(circle)\n    >>> plt.legend(bbox_to_anchor=(1.6, 1.0))\n    >>> plt.show()\n\n    References\n    ----------\n    .. [Qhull] http://www.qhull.org/\n    .. [1] S. Boyd, L. Vandenberghe, Convex Optimization, available\n           at http://stanford.edu/~boyd/cvxbook/\n\n    '
    __class__ = HalfspaceIntersection
    def __del__(self):
        return None
    
    __dict__ = {}
    def __init__(self, halfspaces, interior_point, incremental, qhull_options):
        '\n    HalfspaceIntersection(halfspaces, interior_point, incremental=False, qhull_options=None)\n\n    Halfspace intersections in N dimensions.\n\n    .. versionadded:: 0.19.0\n\n    Parameters\n    ----------\n    halfspaces : ndarray of floats, shape (nineq, ndim+1)\n        Stacked Inequalities of the form Ax + b <= 0 in format [A; b]\n    interior_point : ndarray of floats, shape (ndim,)\n        Point clearly inside the region defined by halfspaces. Also called a feasible\n        point, it can be obtained by linear programming.\n    incremental : bool, optional\n        Allow adding new halfspaces incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qx" for ndim > 4 and "" otherwise)\n        Option "H" is always enabled.\n\n    Attributes\n    ----------\n    halfspaces : ndarray of double, shape (nineq, ndim+1)\n        Input halfspaces.\n    interior_point :ndarray of floats, shape (ndim,)\n        Input interior point.\n    intersections : ndarray of double, shape (ninter, ndim)\n        Intersections of all halfspaces.\n    dual_points : ndarray of double, shape (nineq, ndim)\n        Dual points of the input halfspaces.\n    dual_facets : list of lists of ints\n        Indices of points forming the (non necessarily simplicial) facets of\n        the dual convex hull.\n    dual_vertices : ndarray of ints, shape (nvertices,)\n        Indices of halfspaces forming the vertices of the dual convex hull.\n        For 2-D convex hulls, the vertices are in counterclockwise order.\n        For other dimensions, they are in input order.\n    dual_equations : ndarray of double, shape (nfacet, ndim+1)\n        [normal, offset] forming the hyperplane equation of the dual facet\n        (see `Qhull documentation <http://www.qhull.org/>`__  for more).\n    dual_area : float\n        Area of the dual convex hull\n    dual_volume : float\n        Volume of the dual convex hull\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The intersections are computed using the\n    `Qhull library <http://www.qhull.org/>`__.\n    This reproduces the "qhalf" functionality of Qhull.\n\n    Examples\n    --------\n\n    Halfspace intersection of planes forming some polygon\n\n    >>> from scipy.spatial import HalfspaceIntersection\n    >>> import numpy as np\n    >>> halfspaces = np.array([[-1, 0., 0.],\n    ...                        [0., -1., 0.],\n    ...                        [2., 1., -4.],\n    ...                        [-0.5, 1., -2.]])\n    >>> feasible_point = np.array([0.5, 0.5])\n    >>> hs = HalfspaceIntersection(halfspaces, feasible_point)\n\n    Plot halfspaces as filled regions and intersection points:\n\n    >>> import matplotlib.pyplot as plt\n    >>> fig = plt.figure()\n    >>> ax = fig.add_subplot(\'111\', aspect=\'equal\')\n    >>> xlim, ylim = (-1, 3), (-1, 3)\n    >>> ax.set_xlim(xlim)\n    >>> ax.set_ylim(ylim)\n    >>> x = np.linspace(-1, 3, 100)\n    >>> symbols = [\'-\', \'+\', \'x\', \'*\']\n    >>> signs = [0, 0, -1, -1]\n    >>> fmt = {"color": None, "edgecolor": "b", "alpha": 0.5}\n    >>> for h, sym, sign in zip(halfspaces, symbols, signs):\n    ...     hlist = h.tolist()\n    ...     fmt["hatch"] = sym\n    ...     if h[1]== 0:\n    ...         ax.axvline(-h[2]/h[0], label=\'{}x+{}y+{}=0\'.format(*hlist))\n    ...         xi = np.linspace(xlim[sign], -h[2]/h[0], 100)\n    ...         ax.fill_between(xi, ylim[0], ylim[1], **fmt)\n    ...     else:\n    ...         ax.plot(x, (-h[2]-h[0]*x)/h[1], label=\'{}x+{}y+{}=0\'.format(*hlist))\n    ...         ax.fill_between(x, (-h[2]-h[0]*x)/h[1], ylim[sign], **fmt)\n    >>> x, y = zip(*hs.intersections)\n    >>> ax.plot(x, y, \'o\', markersize=8)\n\n    By default, qhull does not provide with a way to compute an interior point.\n    This can easily be computed using linear programming. Considering halfspaces\n    of the form :math:`Ax + b \\leq 0`, solving the linear program:\n\n    .. math::\n\n        max \\: y\n\n        s.t. Ax + y ||A_i|| \\leq -b\n\n    With :math:`A_i` being the rows of A, i.e. the normals to each plane.\n\n    Will yield a point x that is furthest inside the convex polyhedron. To\n    be precise, it is the center of the largest hypersphere of radius y\n    inscribed in the polyhedron. This point is called the Chebyshev center\n    of the polyhedron (see [1]_ 4.3.1, pp148-149). The\n    equations outputted by Qhull are always normalized.\n\n    >>> from scipy.optimize import linprog\n    >>> from matplotlib.patches import Circle\n    >>> norm_vector = np.reshape(np.linalg.norm(halfspaces[:, :-1], axis=1),\n    ...     (halfspaces.shape[0], 1))\n    >>> c = np.zeros((halfspaces.shape[1],))\n    >>> c[-1] = -1\n    >>> A = np.hstack((halfspaces[:, :-1], norm_vector))\n    >>> b = - halfspaces[:, -1:]\n    >>> res = linprog(c, A_ub=A, b_ub=b)\n    >>> x = res.x[:-1]\n    >>> y = res.x[-1]\n    >>> circle = Circle(x, radius=y, alpha=0.3)\n    >>> ax.add_patch(circle)\n    >>> plt.legend(bbox_to_anchor=(1.6, 1.0))\n    >>> plt.show()\n\n    References\n    ----------\n    .. [Qhull] http://www.qhull.org/\n    .. [1] S. Boyd, L. Vandenberghe, Convex Optimization, available\n           at http://stanford.edu/~boyd/cvxbook/\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_points(self, points, restart, interior_point):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def _update(self, qhull):
        pass
    
    def add_halfspaces(self, halfspaces, restart):
        '\n        add_halfspaces(halfspaces, restart=False)\n\n        Process a set of additional new halfspaces.\n\n        Parameters\n        ----------\n        halfspaces : ndarray\n            New halfspaces to add. The dimensionality should match that of the\n            initial halfspaces.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding halfspaces incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add halfspaces incrementally. Incremental addition\n        of halfspaces is also not possible after `close` has been called.\n\n        '
        pass
    
    def close(self):
        '\n        close()\n\n        Finish incremental processing.\n\n        Call this to free resources taken up by Qhull, when using the\n        incremental mode. After calling this, adding more points is no\n        longer possible.\n        '
        pass
    
    dual_vertices = _mod_builtins.property()
    halfspaces = _mod_builtins.property()

class QhullError(_mod_builtins.RuntimeError):
    __class__ = QhullError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.spatial.qhull'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Voronoi(_QhullUser):
    '\n    Voronoi(points, furthest_site=False, incremental=False, qhull_options=None)\n\n    Voronoi diagrams in N dimensions.\n\n    .. versionadded:: 0.12.0\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to construct a convex hull from\n    furthest_site : bool, optional\n        Whether to compute a furthest-site Voronoi diagram. Default: False\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qbb Qc Qz Qx" for ndim > 4 and\n        "Qbb Qc Qz" otherwise. Incremental mode omits "Qz".)\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    vertices : ndarray of double, shape (nvertices, ndim)\n        Coordinates of the Voronoi vertices.\n    ridge_points : ndarray of ints, shape ``(nridges, 2)``\n        Indices of the points between which each Voronoi ridge lies.\n    ridge_vertices : list of list of ints, shape ``(nridges, *)``\n        Indices of the Voronoi vertices forming each Voronoi ridge.\n    regions : list of list of ints, shape ``(nregions, *)``\n        Indices of the Voronoi vertices forming each Voronoi region.\n        -1 indicates vertex outside the Voronoi diagram.\n    point_region : list of ints, shape (npoints)\n        Index of the Voronoi region for each input point.\n        If qhull option "Qc" was not specified, the list will contain -1\n        for points that are not associated with a Voronoi region.\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The Voronoi diagram is computed using the \n    `Qhull library <http://www.qhull.org/>`__.\n\n    Examples\n    --------\n    Voronoi diagram for a set of point:\n\n    >>> points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],\n    ...                    [2, 0], [2, 1], [2, 2]])\n    >>> from scipy.spatial import Voronoi, voronoi_plot_2d\n    >>> vor = Voronoi(points)\n\n    Plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> voronoi_plot_2d(vor)\n    >>> plt.show()\n\n    The Voronoi vertices:\n\n    >>> vor.vertices\n    array([[ 0.5,  0.5],\n           [ 1.5,  0.5],\n           [ 0.5,  1.5],\n           [ 1.5,  1.5]])\n\n    There is a single finite Voronoi region, and four finite Voronoi\n    ridges:\n\n    >>> vor.regions\n    [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 2, 0, 1], [2, -1, 0], [3, -1, 1]]\n    >>> vor.ridge_vertices\n    [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]\n\n    The ridges are perpendicular between lines drawn between the following\n    input points:\n\n    >>> vor.ridge_points\n    array([[0, 1],\n           [0, 3],\n           [6, 3],\n           [6, 7],\n           [3, 4],\n           [5, 8],\n           [5, 2],\n           [5, 4],\n           [8, 7],\n           [2, 1],\n           [4, 1],\n           [4, 7]], dtype=int32)\n\n    '
    __class__ = Voronoi
    def __del__(self):
        return None
    
    __dict__ = {}
    def __init__(self, points, furthest_site, incremental, qhull_options):
        '\n    Voronoi(points, furthest_site=False, incremental=False, qhull_options=None)\n\n    Voronoi diagrams in N dimensions.\n\n    .. versionadded:: 0.12.0\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndim)\n        Coordinates of points to construct a convex hull from\n    furthest_site : bool, optional\n        Whether to compute a furthest-site Voronoi diagram. Default: False\n    incremental : bool, optional\n        Allow adding new points incrementally. This takes up some additional\n        resources.\n    qhull_options : str, optional\n        Additional options to pass to Qhull. See Qhull manual\n        for details. (Default: "Qbb Qc Qz Qx" for ndim > 4 and\n        "Qbb Qc Qz" otherwise. Incremental mode omits "Qz".)\n\n    Attributes\n    ----------\n    points : ndarray of double, shape (npoints, ndim)\n        Coordinates of input points.\n    vertices : ndarray of double, shape (nvertices, ndim)\n        Coordinates of the Voronoi vertices.\n    ridge_points : ndarray of ints, shape ``(nridges, 2)``\n        Indices of the points between which each Voronoi ridge lies.\n    ridge_vertices : list of list of ints, shape ``(nridges, *)``\n        Indices of the Voronoi vertices forming each Voronoi ridge.\n    regions : list of list of ints, shape ``(nregions, *)``\n        Indices of the Voronoi vertices forming each Voronoi region.\n        -1 indicates vertex outside the Voronoi diagram.\n    point_region : list of ints, shape (npoints)\n        Index of the Voronoi region for each input point.\n        If qhull option "Qc" was not specified, the list will contain -1\n        for points that are not associated with a Voronoi region.\n\n    Raises\n    ------\n    QhullError\n        Raised when Qhull encounters an error condition, such as\n        geometrical degeneracy when options to resolve are not enabled.\n    ValueError\n        Raised if an incompatible array is given as input.\n\n    Notes\n    -----\n    The Voronoi diagram is computed using the \n    `Qhull library <http://www.qhull.org/>`__.\n\n    Examples\n    --------\n    Voronoi diagram for a set of point:\n\n    >>> points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],\n    ...                    [2, 0], [2, 1], [2, 2]])\n    >>> from scipy.spatial import Voronoi, voronoi_plot_2d\n    >>> vor = Voronoi(points)\n\n    Plot it:\n\n    >>> import matplotlib.pyplot as plt\n    >>> voronoi_plot_2d(vor)\n    >>> plt.show()\n\n    The Voronoi vertices:\n\n    >>> vor.vertices\n    array([[ 0.5,  0.5],\n           [ 1.5,  0.5],\n           [ 0.5,  1.5],\n           [ 1.5,  1.5]])\n\n    There is a single finite Voronoi region, and four finite Voronoi\n    ridges:\n\n    >>> vor.regions\n    [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 2, 0, 1], [2, -1, 0], [3, -1, 1]]\n    >>> vor.ridge_vertices\n    [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]\n\n    The ridges are perpendicular between lines drawn between the following\n    input points:\n\n    >>> vor.ridge_points\n    array([[0, 1],\n           [0, 3],\n           [6, 3],\n           [6, 7],\n           [3, 4],\n           [5, 8],\n           [5, 2],\n           [5, 4],\n           [8, 7],\n           [2, 1],\n           [4, 1],\n           [4, 7]], dtype=int32)\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_points(self, points, restart, interior_point):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def _update(self, qhull):
        pass
    
    def add_points(self, points, restart):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    def close(self):
        '\n        close()\n\n        Finish incremental processing.\n\n        Call this to free resources taken up by Qhull, when using the\n        incremental mode. After calling this, adding more points is no\n        longer possible.\n        '
        pass
    
    points = _mod_builtins.property()
    ridge_dict = _mod_builtins.property()

class _Qhull(_mod_builtins.object):
    __class__ = _Qhull
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add_points(self):
        pass
    
    def check_active(self):
        pass
    
    def close(self):
        '\n        Uninitialize this instance\n        '
        pass
    
    @property
    def furthest_site(self):
        pass
    
    def get_extremes_2d(self):
        '\n        Compute the extremal points in a 2-D convex hull, i.e. the\n        vertices of the convex hull, ordered counterclockwise.\n\n        See qhull/io.c:qh_printextremes_2d\n\n        '
        pass
    
    def get_hull_facets(self):
        'Returns the facets contained in the current Qhull.\n        This function does not assume that the hull is simplicial,\n        meaning that facets will have different number of vertices.\n        It is thus less efficient but more general than get_simplex_facet_array.\n\n        Returns\n        -------\n        facets: list of lists of ints\n            The indices of the vertices forming each facet.\n        '
        pass
    
    def get_hull_points(self):
        'Returns all points currently contained in Qhull.\n        It is equivalent to retrieving the input in most cases, except in\n        halfspace mode, where the points are in fact the points of the dual\n        hull.\n\n        Returns\n        -------\n        points: array of double, shape (nrpoints, ndim)\n            The array of points contained in Qhull.\n\n        '
        pass
    
    def get_paraboloid_shift_scale(self):
        pass
    
    def get_points(self):
        pass
    
    def get_simplex_facet_array(self):
        '\n        Return array of simplical facets currently in Qhull.\n\n        Returns\n        -------\n        facets : array of int, shape (nfacets, ndim+1)\n            Indices of coordinates of vertices forming the simplical facets\n        neighbors : array of int, shape (nfacets, ndim)\n            Indices of neighboring facets.  The kth neighbor is opposite\n            the kth vertex, and the first neighbor is the horizon facet\n            for the first vertex.\n\n            Facets extending to infinity are denoted with index -1.\n        equations : array of double, shape (nfacets, ndim+2)\n\n        '
        pass
    
    def get_voronoi_diagram(self):
        '\n        Return the voronoi diagram currently in Qhull.\n\n        Returns\n        -------\n        voronoi_vertices : array of double, shape (nvoronoi_vertices, ndim)\n            Coordinates of the Voronoi vertices\n\n        ridge_points : array of double, shape (nridges, 2)\n            Voronoi ridges, as indices to the points array.\n\n        ridge_vertices : list of lists, shape (nridges, *)\n            Voronoi vertices for each Voronoi ridge, as indices to\n            the Voronoi vertices array.\n            Infinity is indicated by index ``-1``.\n\n        regions : list of lists, shape (nregion, *)\n            Voronoi vertices of all regions.\n\n        point_region : array of int, shape (npoint,)\n            Index of the Voronoi region for each input point.\n\n        '
        pass
    
    @property
    def mode_option(self):
        pass
    
    @property
    def ndim(self):
        pass
    
    @property
    def options(self):
        pass
    
    def triangulate(self):
        pass
    
    def volume_area(self):
        pass
    

class _QhullMessageStream(_mod_builtins.object):
    '\n    Qhull emits error messages to FILE* streams, which we should capture.\n    Do this by directing them to a temporary file.\n    '
    __class__ = _QhullMessageStream
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        '\n    Qhull emits error messages to FILE* streams, which we should capture.\n    Do this by directing them to a temporary file.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        pass
    
    def close(self):
        pass
    
    def get(self):
        pass
    

class _QhullUser(_mod_builtins.object):
    '\n    Takes care of basic dealings with the Qhull objects\n    '
    __class__ = _QhullUser
    def __del__(self):
        return None
    
    __dict__ = {}
    def __init__(self, qhull, incremental):
        '\n    Takes care of basic dealings with the Qhull objects\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.spatial.qhull'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _add_points(self, points, restart, interior_point):
        '\n        add_points(points, restart=False)\n\n        Process a set of additional new points.\n\n        Parameters\n        ----------\n        points : ndarray\n            New points to add. The dimensionality should match that of the\n            initial points.\n        restart : bool, optional\n            Whether to restart processing from scratch, rather than\n            adding points incrementally.\n\n        Raises\n        ------\n        QhullError\n            Raised when Qhull encounters an error condition, such as\n            geometrical degeneracy when options to resolve are not enabled.\n\n        See Also\n        --------\n        close\n\n        Notes\n        -----\n        You need to specify ``incremental=True`` when constructing the\n        object to be able to add points incrementally. Incremental addition\n        of points is also not possible after `close` has been called.\n\n        '
        pass
    
    _qhull = None
    def _update(self, qhull):
        pass
    
    def close(self):
        '\n        close()\n\n        Finish incremental processing.\n\n        Call this to free resources taken up by Qhull, when using the\n        incremental mode. After calling this, adding more points is no\n        longer possible.\n        '
        pass
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nWrappers for Qhull triangulation, plus some additional N-D geometry utilities\n\n.. versionadded:: 0.9\n\n'
__file__ = '/usr/lib/python3/dist-packages/scipy/spatial/qhull.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.spatial.qhull'
__package__ = 'scipy.spatial'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def _get_barycentric_transforms():
    '\n    Compute barycentric affine coordinate transformations for given\n    simplices.\n\n    Returns\n    -------\n    Tinvs : array, shape (nsimplex, ndim+1, ndim)\n        Barycentric transforms for each simplex.\n\n        Tinvs[i,:ndim,:ndim] contains inverse of the matrix ``T``,\n        and Tinvs[i,ndim,:] contains the vector ``r_n`` (see below).\n\n    Notes\n    -----\n    Barycentric transform from ``x`` to ``c`` is defined by::\n\n        T c = x - r_n\n\n    where the ``r_1, ..., r_n`` are the vertices of the simplex.\n    The matrix ``T`` is defined by the condition::\n\n        T e_j = r_j - r_n\n\n    where ``e_j`` is the unit axis vector, e.g, ``e_2 = [0,1,0,0,...]``\n    This implies that ``T_ij = (r_j - r_n)_i``.\n\n    For the barycentric transforms, we need to compute the inverse\n    matrix ``T^-1`` and store the vectors ``r_n`` for each vertex.\n    These are stacked into the `Tinvs` returned.\n\n    '
    pass

def asbytes(s):
    pass

def tsearch():
    '\n    tsearch(tri, xi)\n\n    Find simplices containing the given points. This function does the\n    same thing as `Delaunay.find_simplex`.\n\n    .. versionadded:: 0.9\n\n    See Also\n    --------\n    Delaunay.find_simplex\n\n    '
    pass

