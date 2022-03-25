************
Installation
************

MuST uses make to compile the package and create executables. You have an option of doing a full install, or only installing certain packages like MST, LSMS etc. For simplicity, a full install is recommended.

++++++++++++++++++
Full Installation (Recommended)
++++++++++++++++++

Instead of passing all the required parameters to make, MuST uses a simple "architecture file", which contains all the information (like compilers, library paths) that make requires. Several architecture files are available in the architecture folder. Here is an example file for osx system using gnu compilers and openmpi::
  #=====================================================================
  # Acceleration = 1: enable GPU acceleration
  # Acceleration = 0: otherwise
  #=====================================================================
  Acceleration = 0
  
  #=====================================================================
  # Library paths and elements, e.g.,
  #    LIBXC_PATH  = /opt/packages/LibXC/libxc-4.3.4/INTEL
  #    ACCEL_PATH  = /usr/local/cuda
  #    FFTW_PATH   = /usr/local/FFTW/fftw-3.3.8/INTEL
  #    P3DFFT_PATH = /opt/packages/P3DFFT/p3dfft-2.7.9/INTEL
  #    LUA_PATH    = /opt/packages/Lua/lua-5.3.5
  #  
  # If LUA_PATH, LIBXC_PATH, FFTW_PATH, and/or P3DFFT_PATH are empty, the
  # corresponding packages will be installed under $(EXTERN_LIB_PATH)
  #=====================================================================
  HDF5_PATH   = /usr/local
  ACCEL       =
  ACCEL_PATH  =
  LIBXC_PATH  =
  FFTW_PATH   = /Users/vishnuraghuraman/Documents/fftw-3.3.8
  P3DFFT_PATH = /Users/vishnuraghuraman/Documents/P3DFFT
  
  LUA_PATH    =
  LIBS       += -framework Accelerate -L/usr/local/lib/gcc/9 -lgfortran
  
  #=====================================================================
  # Compiler tools
  #=====================================================================
  CC          = mpicc
  CXX         = mpicxx
  F77         = mpif77
  FC          = mpif90
  MPICC       = mpicc
  ACCEL_CXX   =
  ARCHV       = ar -r
  
  #=====================================================================
  # Preprocessor/Compiler/Linker flags, e.g.,
  #    FFLAGS = -I. -O3 -CB -CU -traceback -ftrapuv -fpe0 -ftz -fp-stack-check
  # Note: "FPPFLAGS = -DMPI" enables MPI parallel processing.
  #=====================================================================
  FPPDEFS     = -cpp
  CPPDEFS     =
  FPPFLAGS    = -DMPI -DMaxOutProcs=1
  
  CFLAGS      = -O3
  CXXFLAGS    = -O3 -std=c++14
  FFLAGS      = -O3 -fcheck=all
  F77FLAGS    = -O3
  OPT_OPENMP  = -openmp
  
  LD_FLAGS    =
  LD          = $(FC) $(LD_FLAGS)
  
  #=====================================================================
  # LIBXC_CONFIG_FLAGS, P3DFFT_CONFIG_FLAGS and FFTW_CONFIG_FLAGS are 
  # ./configure flags for hdf5, libxc, p3dfft, and fftw package, respectively.
  # Note: for hdf5, "--enable-parallel" might be needed in the future.
  #=====================================================================
  HDF5_CONFIG_FLAGS   = --enable-fortran --enable-static-exec CC=$(CC) CXX=$(CXX) FC=$(FC)
  LIBXC_CONFIG_FLAGS  = CC=$(CC) CFLAGS="$(CFLAGS)" FC=$(FC) FFLAGS="$(FFLAGS)"
  P3DFFT_CONFIG_FLAGS = --enable-openmpi FC=$(FC) CC=$(CC) LIBS="$(LIBS)" CCLD=$(FC)
  FFTW_CONFIG_FLAGS   = --enable-mpi --enable-fortran CC=$(CC) CFLAGS="$(CFLAGS)" MPICC=$(MPICC) F77=$(F77) FFLAGS="$(FFLAGS)"

As you can see, the file contains information that would normally be passed to make. Here are the steps to follow

1. Identify the architecture file most suited to your system. Carefully look through this file and see if any specific changes are needed in order to make it run for your system

  * NOTE: If you are running this on Summit, Cori, Bridges (Bridges-2), Crusher, Ascent, Frontera or ThetaGPU, you can directly use the corresponding    
  architecture file provided.
 
2. In the top directory (MuST/), run the following command to build executables::

  make architecture-file-name (e.g., make linux-intel-nogpu)

3. To copy all executables into a single bin folder, run::

  make install
  
Note --
make clean: delete the object, library, executable files under lsms and MST from installation
make distclean: delete the object, library, executable, and architecture.h files under lsms and MST from installation; also
                delete the executables under bin/.

++++++++++++++++++++
Partial Installation
++++++++++++++++++++

The code MST (under MST/) and LSMS/WL-LSMS (under lsms/) can be built separately by running make under MST
and lsms. The executables can be found under MST/bin and lsms/bin, respectively. It requires to create
archietecture.h under MST and lsms using symbolic link. Steps are as follows

* To build MST

  1. cd MST
  2. set SystemName in Makefile (at line 6) to a proper name, or execute the following command::
      ln -s arch/architecture_file architecture.h
  3. make

* To build LSMS/WL-LSMS

  1. cd lsms
  2. ln -s arch/architecture_file architecture.h
  3. make

++++++++++++++++++++
Notes to the user of Fedora systems
++++++++++++++++++++

MST may require using External Data Representation (XDR) library to store potential and charge density data.
Unfortunately, the latest Fedora Linux system does not place the library in conventional locations. Therefore,
before installing MuST or MST, please make sure that /usr/include/tirpc and /usr/include/tirpc/rpc exist. If not,
you need to ask your system administrator to istall libtirpc and librirpc-devel for you, or to run the following command
if you have the sys-admin privilige:
   sudo dnf install libtirpc libtirpc-devel
