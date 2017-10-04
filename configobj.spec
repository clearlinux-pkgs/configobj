#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : configobj
Version  : 5.0.6
Release  : 22
URL      : http://pypi.debian.net/configobj/configobj-5.0.6.tar.gz
Source0  : http://pypi.debian.net/configobj/configobj-5.0.6.tar.gz
Summary  : Config file reading, writing and validation.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: configobj-legacypython
Requires: configobj-python3
Requires: configobj-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
file round tripper*. Its main feature is that it is very easy to use, with a
        straightforward programmer's interface and a simple syntax for config files.

%package legacypython
Summary: legacypython components for the configobj package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the configobj package.


%package python
Summary: python components for the configobj package.
Group: Default
Requires: configobj-legacypython
Requires: configobj-python3

%description python
python components for the configobj package.


%package python3
Summary: python3 components for the configobj package.
Group: Default
Requires: python3-core

%description python3
python3 components for the configobj package.


%prep
%setup -q -n configobj-5.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507151856
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507151856
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
