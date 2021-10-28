#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : configobj
Version  : 5.0.6
Release  : 59
URL      : http://pypi.debian.net/configobj/configobj-5.0.6.tar.gz
Source0  : http://pypi.debian.net/configobj/configobj-5.0.6.tar.gz
Summary  : Config file reading, writing and validation.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: configobj-python = %{version}-%{release}
Requires: configobj-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
file round tripper*. Its main feature is that it is very easy to use, with a
        straightforward programmer's interface and a simple syntax for config files.

%package python
Summary: python components for the configobj package.
Group: Default
Requires: configobj-python3 = %{version}-%{release}

%description python
python components for the configobj package.


%package python3
Summary: python3 components for the configobj package.
Group: Default
Requires: python3-core
Provides: pypi(configobj)
Requires: pypi(six)

%description python3
python3 components for the configobj package.


%prep
%setup -q -n configobj-5.0.6
cd %{_builddir}/configobj-5.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603388749
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
