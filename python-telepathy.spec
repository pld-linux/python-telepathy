Summary:	Python module to connect to Telepathy
Summary(pl.UTF-8):	Moduł Pythona do łączenia się z Telepathy
Name:		python-telepathy
Version:	0.13.10
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.gz
# Source0-md5:	a8c7d7cd3c0f18eff5848a1f060b979e
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to connect to Telepathy.

%description -l pl.UTF-8
Moduł Pythona do łączenia się z Telepathy.

%prep
%setup -q -n telepathy-python-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO-*
%dir %{py_sitescriptdir}/telepathy
%{py_sitescriptdir}/telepathy/*.py[co]
%dir %{py_sitescriptdir}/telepathy/_generated
%{py_sitescriptdir}/telepathy/_generated/*.py[co]
%dir %{py_sitescriptdir}/telepathy/client
%{py_sitescriptdir}/telepathy/client/*.py[co]
%dir %{py_sitescriptdir}/telepathy/server
%{py_sitescriptdir}/telepathy/server/*.py[co]
%{py_sitescriptdir}/telepathy_python-*.egg-info
