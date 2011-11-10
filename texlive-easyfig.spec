# revision 24501
# category Package
# catalog-ctan /macros/latex/contrib/easyfig
# catalog-date 2011-11-03 08:30:49 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-easyfig
Version:	1.0
Release:	1
Summary:	Simplifying the use of common figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easyfig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the command \Figure[<key=value>...]{<image
filename>} to simplify the business of including an image as
figure in the most common form (centred and with caption and
label). Caption and label are set using the caption and label
keys. The label defaults to fig:<image filename> if not used.
The package uses the author's package adjustbox to centre an
image and to allow for easy further modifications.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easyfig/easyfig.sty
%doc %{_texmfdistdir}/doc/latex/easyfig/README
%doc %{_texmfdistdir}/doc/latex/easyfig/easyfig.pdf
#- source
%doc %{_texmfdistdir}/source/latex/easyfig/easyfig.dtx
%doc %{_texmfdistdir}/source/latex/easyfig/easyfig.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
