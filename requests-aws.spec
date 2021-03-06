#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-aws
Version  : 0.1.8
Release  : 12
URL      : https://pypi.python.org/packages/source/r/requests-aws/requests-aws-0.1.8.tar.gz
Source0  : https://pypi.python.org/packages/source/r/requests-aws/requests-aws-0.1.8.tar.gz
Summary  : AWS authentication for Amazon S3 for the python requests module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: requests-aws-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
#S3 using python-requests
AWS authentication for Amazon S3 for the wonderful [pyhon requests library](http://python-requests.org)

%package python
Summary: python components for the requests-aws package.
Group: Default

%description python
python components for the requests-aws package.


%prep
%setup -q -n requests-aws-0.1.8

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
