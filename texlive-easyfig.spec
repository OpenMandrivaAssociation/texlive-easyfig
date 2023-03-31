Name:		texlive-easyfig
Version:	64967
Release:	2
Summary:	Simplifying the use of common figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easyfig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the command \Figure[<key=value>...]{<image
filename>} to simplify the business of including an image as
figure in the most common form (centred and with caption and
label). Caption and label are set using the caption and label
keys; the label fig:<image filename> is used if none is given.
If the here key is given, the figure is not 'floated', and the
user is responsible for placement. The package uses the
author's package adjustbox to centre an image and to simplify
further modifications.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easyfig/easyfig.sty
%doc %{_texmfdistdir}/doc/latex/easyfig/README
%doc %{_texmfdistdir}/doc/latex/easyfig/easyfig.pdf
#- source
%doc %{_texmfdistdir}/source/latex/easyfig/easyfig.dtx
%doc %{_texmfdistdir}/source/latex/easyfig/easyfig.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
