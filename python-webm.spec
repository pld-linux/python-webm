#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Python interface to the Google WebM video/image codec
Summary(pl.UTF-8):	Interfejs Pythona do kodeka wideo/obrazu Google WebM
Name:		python-webm
Version:	0.2.5
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://xpra.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	d2096d3a34be79f53c19302355902e3d
URL:		https://code.google.com/p/python-webm/
%if %{with tests}
BuildRequires:	libwebp
BuildRequires:	python >= 1:2.6.5
BuildRequires:	python-PIL
BuildRequires:	python-modules >= 1:2.6.5
BuildRequires:	python-nose
%endif
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python-modules >= 1:2.6.5
Requires:	libwebp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The python-webm package is an interface to the Google WebM new
video/image codec.

%description -l pl.UTF-8
Pakiet python-webm to interfejs do nowego kodeka wideo/obrazu
Google WebM.

%prep
%setup -q

%build
%if %{with tests}
nosetests -s -x
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/webm

cp -p webm/*.py $RPM_BUILD_ROOT%{py_sitescriptdir}/webm

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/webm
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/webm
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%dir %{py_sitescriptdir}/webm
%{py_sitescriptdir}/webm/*.py[co]
