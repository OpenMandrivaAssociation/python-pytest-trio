%define module pytest-trio
%define uname pytest_trio

Name:		python-pytest-trio
Version:	0.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-trio/%{module}-%{version}.tar.gz
Summary:	Pytest plugin for trio
URL:		https://pypi.org/project/pytest-trio/
License:	MIT OR Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(trio) >= 0.22.0
BuildRequires:	python%{pyver}dist(wheel)

%description
Pytest plugin for trio

%prep
%autosetup -n %{module}-%{version} -p1
rm pytest_trio/_tests/test_hypothesis_interaction.py
mv pytest_trio/_tests/ tests

%build
%py_build

%install
%py_install
rm -r %{buildroot}%{python3_sitelib}/tests/

%files
%{python3_sitelib}/%{uname}
%{python3_sitelib}/%{uname}-%{version}.dist-info
%license LICENSE
