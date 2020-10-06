# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Graph State Stabilizer Simulator -- S. Anders"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _graphsim
else:
    import _graphsim

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _graphsim.delete_SwigPyIterator

    def value(self) -> "PyObject *":
        return _graphsim.SwigPyIterator_value(self)

    def incr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _graphsim.SwigPyIterator_incr(self, n)

    def decr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _graphsim.SwigPyIterator_decr(self, n)

    def distance(self, x: "SwigPyIterator") -> "ptrdiff_t":
        return _graphsim.SwigPyIterator_distance(self, x)

    def equal(self, x: "SwigPyIterator") -> "bool":
        return _graphsim.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _graphsim.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _graphsim.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _graphsim.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _graphsim.SwigPyIterator_previous(self)

    def advance(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _graphsim.SwigPyIterator_advance(self, n)

    def __eq__(self, x: "SwigPyIterator") -> "bool":
        return _graphsim.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: "SwigPyIterator") -> "bool":
        return _graphsim.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _graphsim.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _graphsim.SwigPyIterator___isub__(self, n)

    def __add__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _graphsim.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _graphsim.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _graphsim:
_graphsim.SwigPyIterator_swigregister(SwigPyIterator)

class VectorOfStructVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _graphsim.VectorOfStructVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _graphsim.VectorOfStructVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _graphsim.VectorOfStructVector___bool__(self)

    def __len__(self) -> "std::vector< std::vector< long > >::size_type":
        return _graphsim.VectorOfStructVector___len__(self)

    def __getslice__(self, i: "std::vector< std::vector< long > >::difference_type", j: "std::vector< std::vector< long > >::difference_type") -> "std::vector< std::vector< long,std::allocator< long > >,std::allocator< std::vector< long,std::allocator< long > > > > *":
        return _graphsim.VectorOfStructVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _graphsim.VectorOfStructVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< std::vector< long > >::difference_type", j: "std::vector< std::vector< long > >::difference_type") -> "void":
        return _graphsim.VectorOfStructVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _graphsim.VectorOfStructVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::vector< long > >::value_type const &":
        return _graphsim.VectorOfStructVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _graphsim.VectorOfStructVector___setitem__(self, *args)

    def pop(self) -> "std::vector< std::vector< long > >::value_type":
        return _graphsim.VectorOfStructVector_pop(self)

    def append(self, x: "std::vector< std::vector< long > >::value_type const &") -> "void":
        return _graphsim.VectorOfStructVector_append(self, x)

    def empty(self) -> "bool":
        return _graphsim.VectorOfStructVector_empty(self)

    def size(self) -> "std::vector< std::vector< long > >::size_type":
        return _graphsim.VectorOfStructVector_size(self)

    def swap(self, v: "VectorOfStructVector") -> "void":
        return _graphsim.VectorOfStructVector_swap(self, v)

    def begin(self) -> "std::vector< std::vector< long > >::iterator":
        return _graphsim.VectorOfStructVector_begin(self)

    def end(self) -> "std::vector< std::vector< long > >::iterator":
        return _graphsim.VectorOfStructVector_end(self)

    def rbegin(self) -> "std::vector< std::vector< long > >::reverse_iterator":
        return _graphsim.VectorOfStructVector_rbegin(self)

    def rend(self) -> "std::vector< std::vector< long > >::reverse_iterator":
        return _graphsim.VectorOfStructVector_rend(self)

    def clear(self) -> "void":
        return _graphsim.VectorOfStructVector_clear(self)

    def get_allocator(self) -> "std::vector< std::vector< long > >::allocator_type":
        return _graphsim.VectorOfStructVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _graphsim.VectorOfStructVector_pop_back(self)

    def erase(self, *args) -> "std::vector< std::vector< long > >::iterator":
        return _graphsim.VectorOfStructVector_erase(self, *args)

    def __init__(self, *args):
        _graphsim.VectorOfStructVector_swiginit(self, _graphsim.new_VectorOfStructVector(*args))

    def push_back(self, x: "std::vector< std::vector< long > >::value_type const &") -> "void":
        return _graphsim.VectorOfStructVector_push_back(self, x)

    def front(self) -> "std::vector< std::vector< long > >::value_type const &":
        return _graphsim.VectorOfStructVector_front(self)

    def back(self) -> "std::vector< std::vector< long > >::value_type const &":
        return _graphsim.VectorOfStructVector_back(self)

    def assign(self, n: "std::vector< std::vector< long > >::size_type", x: "std::vector< std::vector< long > >::value_type const &") -> "void":
        return _graphsim.VectorOfStructVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _graphsim.VectorOfStructVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _graphsim.VectorOfStructVector_insert(self, *args)

    def reserve(self, n: "std::vector< std::vector< long > >::size_type") -> "void":
        return _graphsim.VectorOfStructVector_reserve(self, n)

    def capacity(self) -> "std::vector< std::vector< long > >::size_type":
        return _graphsim.VectorOfStructVector_capacity(self)
    __swig_destroy__ = _graphsim.delete_VectorOfStructVector

# Register VectorOfStructVector in _graphsim:
_graphsim.VectorOfStructVector_swigregister(VectorOfStructVector)

class boolpc(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _graphsim.boolpc_swiginit(self, _graphsim.new_boolpc())
    __swig_destroy__ = _graphsim.delete_boolpc

    def assign(self, value: "bool") -> "void":
        return _graphsim.boolpc_assign(self, value)

    def value(self) -> "bool":
        return _graphsim.boolpc_value(self)

    def cast(self) -> "bool *":
        return _graphsim.boolpc_cast(self)

    @staticmethod
    def frompointer(t: "bool *") -> "boolpc *":
        return _graphsim.boolpc_frompointer(t)

# Register boolpc in _graphsim:
_graphsim.boolpc_swigregister(boolpc)

def boolpc_frompointer(t: "bool *") -> "boolpc *":
    return _graphsim.boolpc_frompointer(t)

class RightPhase(object):
    r"""Proxy of C++ RightPhase class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ph = property(_graphsim.RightPhase_ph_get, _graphsim.RightPhase_ph_set, doc=r"""ph : unsigned short""")

    def __init__(self, *args):
        r"""
        __init__(RightPhase self) -> RightPhase
        __init__(RightPhase self, unsigned short ph_) -> RightPhase
        """
        _graphsim.RightPhase_swiginit(self, _graphsim.new_RightPhase(*args))

    def get_name(self) -> "string":
        r"""get_name(RightPhase self) -> string"""
        return _graphsim.RightPhase_get_name(self)
    __swig_destroy__ = _graphsim.delete_RightPhase

# Register RightPhase in _graphsim:
_graphsim.RightPhase_swigregister(RightPhase)

class LocCliffOp(object):
    r"""Proxy of C++ LocCliffOp class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    op = property(_graphsim.LocCliffOp_op_get, _graphsim.LocCliffOp_op_set, doc=r"""op : unsigned short""")

    def __init__(self, *args):
        r"""
        __init__(LocCliffOp self, unsigned short op_) -> LocCliffOp
        __init__(LocCliffOp self, unsigned short signsymb, unsigned short permsymb) -> LocCliffOp
        """
        _graphsim.LocCliffOp_swiginit(self, _graphsim.new_LocCliffOp(*args))

    def get_name(self) -> "string":
        r"""get_name(LocCliffOp self) -> string"""
        return _graphsim.LocCliffOp_get_name(self)

    def conjugate(self, trans: "LocCliffOp") -> "RightPhase":
        r"""conjugate(LocCliffOp self, LocCliffOp trans) -> RightPhase"""
        return _graphsim.LocCliffOp_conjugate(self, trans)

    def herm_adjoint(self) -> "LocCliffOp":
        r"""herm_adjoint(LocCliffOp self) -> LocCliffOp"""
        return _graphsim.LocCliffOp_herm_adjoint(self)

    @staticmethod
    def mult_phase(op1: "LocCliffOp", op2: "LocCliffOp") -> "RightPhase":
        r"""mult_phase(LocCliffOp op1, LocCliffOp op2) -> RightPhase"""
        return _graphsim.LocCliffOp_mult_phase(op1, op2)

    def isXY(self) -> "bool":
        r"""isXY(LocCliffOp self) -> bool"""
        return _graphsim.LocCliffOp_isXY(self)

    def is_diagonal(self) -> "bool":
        r"""is_diagonal(LocCliffOp self) -> bool"""
        return _graphsim.LocCliffOp_is_diagonal(self)

    def get_matrix(self) -> "RightMatrix":
        r"""get_matrix(LocCliffOp self) -> RightMatrix"""
        return _graphsim.LocCliffOp_get_matrix(self)
    __swig_destroy__ = _graphsim.delete_LocCliffOp

# Register LocCliffOp in _graphsim:
_graphsim.LocCliffOp_swigregister(LocCliffOp)

def LocCliffOp_mult_phase(op1: "LocCliffOp", op2: "LocCliffOp") -> "RightPhase":
    r"""LocCliffOp_mult_phase(LocCliffOp op1, LocCliffOp op2) -> RightPhase"""
    return _graphsim.LocCliffOp_mult_phase(op1, op2)

class Stabilizer(object):
    r"""Proxy of C++ Stabilizer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    numQubits = property(_graphsim.Stabilizer_numQubits_get, _graphsim.Stabilizer_numQubits_set, doc=r"""numQubits : VertexIndex""")
    paulis = property(_graphsim.Stabilizer_paulis_get, _graphsim.Stabilizer_paulis_set, doc=r"""paulis : std::vector<(std::vector<(LocCliffOp)>)>""")
    rowsigns = property(_graphsim.Stabilizer_rowsigns_get, _graphsim.Stabilizer_rowsigns_set, doc=r"""rowsigns : std::vector<(RightPhase)>""")
    vtxidx = property(_graphsim.Stabilizer_vtxidx_get, _graphsim.Stabilizer_vtxidx_set, doc=r"""vtxidx : std::vector<(VertexIndex)>""")

    def __init__(self, *args):
        r"""
        __init__(Stabilizer self, VertexIndex const numQubits_) -> Stabilizer
        __init__(Stabilizer self, GraphRegister gr, hash_set< VertexIndex > const & qubits) -> Stabilizer
        __init__(Stabilizer self, QState * qs) -> Stabilizer
        """
        _graphsim.Stabilizer_swiginit(self, _graphsim.new_Stabilizer(*args))

    def add_row(self, target: "unsigned int", addend: "unsigned int") -> "void":
        r"""add_row(Stabilizer self, unsigned int target, unsigned int addend)"""
        return _graphsim.Stabilizer_add_row(self, target, addend)

    def conjugate(self, row: "unsigned int", col: "unsigned int", trans: "LocCliffOp") -> "void":
        r"""conjugate(Stabilizer self, unsigned int row, unsigned int col, LocCliffOp trans)"""
        return _graphsim.Stabilizer_conjugate(self, row, col, trans)

    def conjugate_column(self, col: "unsigned int", trans: "LocCliffOp") -> "void":
        r"""conjugate_column(Stabilizer self, unsigned int col, LocCliffOp trans)"""
        return _graphsim.Stabilizer_conjugate_column(self, col, trans)

    def print_tbl(self, *args) -> "void":
        r"""print_tbl(Stabilizer self, ostream & os=cout)"""
        return _graphsim.Stabilizer_print_tbl(self, *args)

    def compare(self, diag: "Stabilizer") -> "bool":
        r"""compare(Stabilizer self, Stabilizer diag) -> bool"""
        return _graphsim.Stabilizer_compare(self, diag)
    __swig_destroy__ = _graphsim.delete_Stabilizer

# Register Stabilizer in _graphsim:
_graphsim.Stabilizer_swigregister(Stabilizer)
consts = _graphsim.consts
num_LocCliffOps = consts.num_LocCliffOps
lco_Id = consts.lco_Id
lco_X = consts.lco_X
lco_Y = consts.lco_Y
lco_Z = consts.lco_Z
lco_H = consts.lco_H
lco_spiZ = consts.lco_spiZ
lco_smiZ = consts.lco_smiZ
lco_spiY = consts.lco_spiY
lco_smiY = consts.lco_smiY
lco_spiX = consts.lco_spiX
lco_smiX = consts.lco_smiX
lco_S = consts.lco_S
lco_Sh = consts.lco_Sh
rp_p1 = consts.rp_p1
rp_pI = consts.rp_pI
rp_m1 = consts.rp_m1
rp_mI = consts.rp_mI

class QubitVertex(object):
    r"""Proxy of C++ QubitVertex class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    byprod = property(_graphsim.QubitVertex_byprod_get, _graphsim.QubitVertex_byprod_set, doc=r"""byprod : LocCliffOp""")
    neighbors = property(_graphsim.QubitVertex_neighbors_get, _graphsim.QubitVertex_neighbors_set, doc=r"""neighbors : hash_set<(VertexIndex)>""")

    def __init__(self):
        r"""__init__(QubitVertex self) -> QubitVertex"""
        _graphsim.QubitVertex_swiginit(self, _graphsim.new_QubitVertex())
    __swig_destroy__ = _graphsim.delete_QubitVertex

# Register QubitVertex in _graphsim:
_graphsim.QubitVertex_swigregister(QubitVertex)

class GraphRegister(object):
    r"""Proxy of C++ GraphRegister class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    vertices = property(_graphsim.GraphRegister_vertices_get, _graphsim.GraphRegister_vertices_set, doc=r"""vertices : std::vector<(QubitVertex)>""")

    def __init__(self, *args):
        r"""
        __init__(GraphRegister self, VertexIndex numQubits, int randomize=-1) -> GraphRegister
        __init__(GraphRegister self, GraphRegister gr) -> GraphRegister
        """
        _graphsim.GraphRegister_swiginit(self, _graphsim.new_GraphRegister(*args))
    __swig_destroy__ = _graphsim.delete_GraphRegister

    def local_op(self, v: "VertexIndex", o: "LocCliffOp") -> "void":
        r"""local_op(GraphRegister self, VertexIndex v, LocCliffOp o)"""
        return _graphsim.GraphRegister_local_op(self, v, o)

    def hadamard(self, v: "VertexIndex") -> "void":
        r"""hadamard(GraphRegister self, VertexIndex v)"""
        return _graphsim.GraphRegister_hadamard(self, v)

    def phaserot(self, v: "VertexIndex") -> "void":
        r"""phaserot(GraphRegister self, VertexIndex v)"""
        return _graphsim.GraphRegister_phaserot(self, v)

    def bitflip(self, v: "VertexIndex") -> "void":
        r"""bitflip(GraphRegister self, VertexIndex v)"""
        return _graphsim.GraphRegister_bitflip(self, v)

    def phaseflip(self, v: "VertexIndex") -> "void":
        r"""phaseflip(GraphRegister self, VertexIndex v)"""
        return _graphsim.GraphRegister_phaseflip(self, v)

    def cphase(self, v1: "VertexIndex", v2: "VertexIndex") -> "void":
        r"""cphase(GraphRegister self, VertexIndex v1, VertexIndex v2)"""
        return _graphsim.GraphRegister_cphase(self, v1, v2)

    def cnot(self, vc: "VertexIndex", vt: "VertexIndex") -> "void":
        r"""cnot(GraphRegister self, VertexIndex vc, VertexIndex vt)"""
        return _graphsim.GraphRegister_cnot(self, vc, vt)

    def measure(self, *args) -> "int":
        r"""measure(GraphRegister self, VertexIndex v, LocCliffOp basis=lco_Z, bool * determined=None, int force=-1) -> int"""
        return _graphsim.GraphRegister_measure(self, *args)

    def get_full_stabilizer(self) -> "Stabilizer &":
        r"""get_full_stabilizer(GraphRegister self) -> Stabilizer"""
        return _graphsim.GraphRegister_get_full_stabilizer(self)

    def invert_neighborhood(self, v: "VertexIndex") -> "void":
        r"""invert_neighborhood(GraphRegister self, VertexIndex v)"""
        return _graphsim.GraphRegister_invert_neighborhood(self, v)

    def print_adj_list(self, *args) -> "void":
        r"""print_adj_list(GraphRegister self, ostream & os=cout)"""
        return _graphsim.GraphRegister_print_adj_list(self, *args)

    def print_adj_list_line(self, os: "ostream &", i: "VertexIndex") -> "void":
        r"""print_adj_list_line(GraphRegister self, ostream & os, VertexIndex i)"""
        return _graphsim.GraphRegister_print_adj_list_line(self, os, i)

    def print_stabilizer(self, *args) -> "void":
        r"""print_stabilizer(GraphRegister self, ostream & os=cout)"""
        return _graphsim.GraphRegister_print_stabilizer(self, *args)

    def subAdjacencyMatrix(self, vs1: "hash_set< VertexIndex > const", vs2: "hash_set< VertexIndex > const") -> "NTL::mat_GF2":
        r"""subAdjacencyMatrix(GraphRegister self, hash_set< VertexIndex > const vs1, hash_set< VertexIndex > const vs2) -> NTL::mat_GF2"""
        return _graphsim.GraphRegister_subAdjacencyMatrix(self, vs1, vs2)

    def complementSet(self, vs1: "hash_set< VertexIndex > const") -> "hash_set< VertexIndex >":
        r"""complementSet(GraphRegister self, hash_set< VertexIndex > const vs1) -> hash_set< VertexIndex >"""
        return _graphsim.GraphRegister_complementSet(self, vs1)

    def entEntropy(self, obj: "PyObject *") -> "long":
        r"""entEntropy(GraphRegister self, PyObject * obj) -> long"""
        return _graphsim.GraphRegister_entEntropy(self, obj)

    def degreeSum(self) -> "long":
        r"""degreeSum(GraphRegister self) -> long"""
        return _graphsim.GraphRegister_degreeSum(self)

    def getClusters(self) -> "std::vector< long >":
        r"""getClusters(GraphRegister self) -> std::vector< long >"""
        return _graphsim.GraphRegister_getClusters(self)

    def getClusterList(self) -> "std::vector< std::vector< long > >":
        r"""getClusterList(GraphRegister self) -> VectorOfStructVector"""
        return _graphsim.GraphRegister_getClusterList(self)

    def largestCluster(self) -> "long":
        r"""largestCluster(GraphRegister self) -> long"""
        return _graphsim.GraphRegister_largestCluster(self)

    def randomTwoQubitClifford(self, v1: "VertexIndex", v2: "VertexIndex") -> "void":
        r"""randomTwoQubitClifford(GraphRegister self, VertexIndex v1, VertexIndex v2)"""
        return _graphsim.GraphRegister_randomTwoQubitClifford(self, v1, v2)

# Register GraphRegister in _graphsim:
_graphsim.GraphRegister_swigregister(GraphRegister)



