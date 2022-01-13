#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB05F05B75D36644B (jwe@gnu.org)
#
Name     : octave
Version  : 6.4.0
Release  : 37
URL      : https://mirrors.kernel.org/gnu/octave/octave-6.4.0.tar.xz
Source0  : https://mirrors.kernel.org/gnu/octave/octave-6.4.0.tar.xz
Source1  : https://mirrors.kernel.org/gnu/octave/octave-6.4.0.tar.xz.sig
Summary  : C++ interface to GNU Octave underlying library.
Group    : Development/Tools
License  : GPL-3.0
Requires: glibc-lib-avx2
BuildRequires : SuiteSparse-dev
BuildRequires : bison
BuildRequires : buildreq-kde
BuildRequires : curl-dev
BuildRequires : fftw-dev
BuildRequires : flex
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : gfortran
BuildRequires : ghostscript
BuildRequires : glibc-locale
BuildRequires : glu-dev
BuildRequires : gnuplot
BuildRequires : gperf
BuildRequires : grep
BuildRequires : hdf5-dev
BuildRequires : less
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : librsvg
BuildRequires : libsndfile-dev
BuildRequires : llvm-dev
BuildRequires : ncurses-dev
BuildRequires : openblas-dev
BuildRequires : openjdk-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : qhull-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
BuildRequires : readline-dev
BuildRequires : sundials-dev
BuildRequires : texinfo
Patch1: 0001-Fix-build-with-Qt-5.12.patch

%description
GNU Octave -- a high-level language for numerical computations
==============================================================

%prep
%setup -q -n octave-6.4.0
cd %{_builddir}/octave-6.4.0
%patch1 -p1
pushd ..
cp -a octave-6.4.0 buildavx2
popd
pushd ..
cp -a octave-6.4.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639693057
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static --enable-openmp \
--disable-docs \
--with-blas=openblas
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-openmp \
--disable-docs \
--with-blas=openblas
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static --enable-openmp \
--disable-docs \
--with-blas=openblas
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1639693057
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/octave
cp %{_builddir}/octave-6.4.0/COPYING %{buildroot}/usr/share/package-licenses/octave/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/octave-6.4.0/doc/interpreter/octave.html/Copying.html %{buildroot}/usr/share/package-licenses/octave/2f3ec857fa0d2a3e797dadfe2bde5f4dafa79031
cp %{_builddir}/octave-6.4.0/doc/liboctave/liboctave.html/Copying.html %{buildroot}/usr/share/package-licenses/octave/9bdab8329d4a0fcd61e7b9b9f8d0413687cb0c4f
cp %{_builddir}/octave-6.4.0/test/pkg/mfile_basic_test/COPYING %{buildroot}/usr/share/package-licenses/octave/21f3db650be936f00c242e559a23b6a16eaf9318
cp %{_builddir}/octave-6.4.0/test/pkg/mfile_minimal_test/COPYING %{buildroot}/usr/share/package-licenses/octave/21f3db650be936f00c242e559a23b6a16eaf9318
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
