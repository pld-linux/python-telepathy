Summary:	Python module to connect to Telepathy
Summary(pl.UTF-8):	Moduł Pythona do łączenia się z Telepathy
Name:		python-telepathy
Version:	0.15.15
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://telepathy.freedesktop.org/releases/telepathy-python/telepathy-python-%{version}.tar.gz
# Source0-md5:	714fac03ff1386092f209f7ec398d261
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to connect to Telepathy.

%description -l pl.UTF-8
Moduł Pythona do łączenia się z Telepathy.

%package examples
Summary:	Examples for telepathy module
Summary(pl.UTF-8):	Przykłady do modułu telepathy
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples for telepathy module.

%description examples -l pl.UTF-8
Przykłady do modułu telepathy.

%prep
%setup -q -n telepathy-python-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitescriptdir}/telepathy
%{py_sitescriptdir}/telepathy/*.py[co]
%dir %{py_sitescriptdir}/telepathy/_generated
%{py_sitescriptdir}/telepathy/_generated/*.py[co]
%dir %{py_sitescriptdir}/telepathy/client
%{py_sitescriptdir}/telepathy/client/*.py[co]
%dir %{py_sitescriptdir}/telepathy/server
%{py_sitescriptdir}/telepathy/server/*.py[co]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
