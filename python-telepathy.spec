Summary:	Python module to connect to Telepathy
Name:		telepathy-python
Version:	0.13.10
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-python/%{name}-%{version}.tar.gz
# Source0-md5:	a8c7d7cd3c0f18eff5848a1f060b979e
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to connect to Telepathy.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/ -name \*.py | xargs rm -f


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitescriptdir}/telepathy
%{py_sitescriptdir}/telepathy/*.py[co]
%dir %{py_sitescriptdir}/telepathy/_generated/
%{py_sitescriptdir}/telepathy/_generated/*.py[co]
%dir %{py_sitescriptdir}/telepathy/client/
%{py_sitescriptdir}/telepathy/client/*.py[co]
%dir %{py_sitescriptdir}/telepathy/server/
%{py_sitescriptdir}/telepathy/server/*.py[co]
