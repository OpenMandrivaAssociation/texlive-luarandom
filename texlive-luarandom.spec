Name:		texlive-luarandom
Version:	68847
Release:	1
Summary:	Create lists of random numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luarandom
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luarandom.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luarandom.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can create lists of random numbers for any given
interval [a;b]. It is possible to get lists with or without
multiple numbers. The random generator will be initialized by
the system time. The package can only be used with LuaLaTeX!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luarandom
%doc %{_texmfdistdir}/doc/lualatex/luarandom

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
