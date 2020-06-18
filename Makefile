# Makefile for graphsim

# This make file defines the following targets:
#   gs: The graphsim C++ library (as simple object file to link against)
#      and a small test program called gstest
#   pywrapper: Python bindings to graphsim (needs SWIG)
#   doc: documentation for use with C++ (needs Doxygen)
#   docpy: documentation for use with Python (needs Pydoc)
#   all: all of the above
#   chpcomp: compile Aaronson's CHP program to compare with this. Only for debugging
#      Needs subdirectory 'CHP'.
#   clean: Delete all generated files

# Set these variables to 'yes' or 'no' to switch on or off debug information,
# profile inpormation, and optimization
DEBUG=yes
PROFILE=no
OPTIMIZE=yes

# SWIG is a tool to generate bindings to the C++ library for script languages
# (here: Python). Enter here the path to the SWIG binary. If you do not have
# SWIG and do not need Python bindings, leave it empty and build only the target
# 'gs', not 'all'
SWIG=/usr/local/bin/swig

# Mathlink is a part of Mathematica. It is used here to compare the computation of
# graphsim with Scott Aaronson's CHP program. If you do not want to do debugging
# or checking, you do not need this. Put it to 'no'.
WITH_MATHLINK=no
#MATHLINK=/opt/local/cluster/Mathematica/5.0/AddOns/MathLink/DeveloperKit/Linux/CompilerAdditions/

# The following compiler flags are for GNU C/C++. if you have another compiler
# you might have to change them
CXX=g++
CC=gcc

#source /opt/intel/compilers_and_libraries_2019/linux/mkl/bin/mklvars.sh ia32

CFLAGS=-Wall -fPIC
CFLAGS += -fvisibility=hidden
CFLAGS += -std=c++11 -pthread -march=native
POSTFLAGS=-LLIBDIR -lntl -lgmp -lgf2x -lm
#CFLAGS += -m64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm
NOLINK=-c
ifeq (${DEBUG}, yes)
   CFLAGS += -g
endif
ifeq (${PROFILE}, yes)
   CFLAGS += -pg
endif
ifeq (${OPTIMIZE}, yes)
   CFLAGS += -O3
endif

# Doxygen binary. (Leave empty if you do not have Doxygen.)
DOXYGEN=/usr/bin/doxygen

# End of user configurable settings.

# This is for MathLink:
MLLIB=
MLINC=
ifeq (${WITH_MATHLINK}, yes)
   CFLAGS += -DWITH_MATHLINK
   MLLIB = ${MATHLINK}/libML.a
   MLINC = -I${MATHLINK}
endif
 
all: gs pywrapper doc docpy

gs: graphsim.o gstest

pywrapper: graphsim.py _graphsim.so
  
doc: doc/timestamp.dummy
	
docpy: doc/graphsim_py.html

chpcomp: chp.py _chp.so

DELFILES=*.o _*.so gstest *_wrap.* graphsim.py \
	graphsim.html chp.py chp.html *.pyc core.*
clean:
	rm -f ${DELFILES} CHP/${DELFILES}
	#cd doc && rm -rf *
	
# Now the details:

gstest: graphsim.o loccliff.o stabilizer.o gstest.cpp
	${CXX} ${CFLAGS} -o gstest gstest.cpp graphsim.o loccliff.o stabilizer.o ${MLLIB} ${POSTFLAGS} -I/home/oliver/anaconda3/envs/idp/include/python3.7m -L/home/oliver/anaconda3/envs/idp/lib -lpython3.7m
	
graphsim.o: graphsim.cpp graphsim.h cphase.tbl loccliff.h stabilizer.h
	${CXX} ${CFLAGS} ${NOLINK} graphsim.cpp -I/home/oliver/anaconda3/envs/idp/include/python3.7m
  
loccliff.o: loccliff.cpp loccliff.h
	${CXX} ${CFLAGS} ${NOLINK} loccliff.cpp -I/home/oliver/anaconda3/envs/idp/include/python3.7m

stabilizer.o: stabilizer.cpp stabilizer.h graphsim.h loccliff.h
	${CXX} ${CFLAGS} ${NOLINK} stabilizer.cpp ${MLINC} -I/home/oliver/anaconda3/envs/idp/include/python3.7m

graphsim_wrap.cxx: graphsim.h loccliff.h
	${SWIG} -python -py3 ${NOLINK}++ -globals consts graphsim.h
   
_graphsim.so: graphsim.o graphsim_wrap.o loccliff.o stabilizer.o
	${CXX} ${CFLAGS} -shared graphsim.o graphsim_wrap.o loccliff.o \
	stabilizer.o ${MLLIB} ${POSTFLAGS} -I/home/oliver/anaconda3/envs/idp/include/python3.7m -o _graphsim.so

graphsim_wrap.o: graphsim_wrap.cxx
	${CXX} ${CFLAGS} ${NOLINK} graphsim_wrap.cxx -I/home/oliver/anaconda3/envs/idp/include/python3.7m

loccliff.h: multtbl.tbl

graphsim.py: _graphsim.so

doc/graphsim_py.html: graphsim.py
	pydoc -w ./graphsim.py
	mv graphsim.html doc/graphsim_py.html

doc/chp.html: chp.py
	pydoc -w CHP/chp.py
	mv chp.html doc/chp_py.html

doc/timestamp.dummy: graphsim.h loccliff.h stabilizer.h
	touch doc/timestamp.dummy
	${DOXYGEN}

chp.py: _chp.so

#chp_wrap.o: CHP/chp_wrap.c
#	${CC} ${CFLAGS} ${NOLINK} CHP/chp_wrap.c -I/usr/include/python2.7/

chp_wrap.o: CHP/chp_wrap.c
	${CC} ${CFLAGS} ${NOLINK} CHP/chp_wrap.c -I/home/oliver/anaconda3/envs/idp/include/python3.7m

chp_wrap.c: CHP/chp.i CHP/chp.h
	${SWIG} -python -py3 CHP/chp.i
   
chp.o: CHP/chp.c
	${CC} ${CFLAGS} ${NOLINK} CHP/chp.c
   
chp.py _chp.so: chp.o chp_wrap.o
	${CC} ${CFLAGS} -shared chp.o chp_wrap.o -o _chp.so
