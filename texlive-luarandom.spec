%global tl_name luarandom
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Create lists of random numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luarandom
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luarandom.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luarandom.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can create lists of random numbers for any given interval
[a;b]. It is possible to get lists with or without multiple numbers. The
random generator will be initialized by the system time. The package can
only be used with LuaLaTeX!

