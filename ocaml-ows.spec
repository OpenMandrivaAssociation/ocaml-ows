%define name	ocaml-ows
%define version	0.1
%define release	%mkrel 3

%if %mdkversion > 200900
%define ocaml_libdir %{_libdir}/ocaml
%else
%define ocaml_libdir %{ocaml_sitelib}
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    OCaml Web Session
Group:      Development/Other
License:    MIT
URL:        http://pauillac.inria.fr/~guesdon/Tools/Tars/
Source0:    http://pauillac.inria.fr/~guesdon/Tools/Tars/ows_snapshot.tar.gz
Patch:      ows-snapshot-fix-build.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-cgi-devel
BuildRequires:  cameleon-libs
BuildRequires:  camlp4
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OWS is a library to easily create a multi-page cgi-bin with session management.
It can manage session id in the url arguments or in a cookie.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cgi-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ows-snapshot
%patch -p 1

%build
autoconf
./configure
make all doc INCLUDES="-I %{ocaml_libdir}/cameleon -I %{ocaml_libdir}/cgi"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{ocaml_libdir}
make install \
    DESTDIR=%{buildroot} \
    INSTALL_LIBDIR=%{buildroot}%{ocaml_libdir}/ows
cp ows.mli %{buildroot}%{ocaml_libdir}/ows/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{ocaml_libdir}/ows
%{ocaml_libdir}/ows/*.cmi
%{ocaml_libdir}/ows/*.cma

%files devel
%defattr(-,root,root)
%doc LICENSE INSTALL README
%doc doc
%dir %{ocaml_libdir}/ows/*
%{ocaml_libdir}/ows/*.cmxa
%{ocaml_libdir}/ows/*.a
%{ocaml_libdir}/ows/*.mli

