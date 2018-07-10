# revision 26424
# category Package
# catalog-ctan /macros/latex/contrib/easyfig
# catalog-date 2012-05-15 13:39:37 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-easyfig
Version:	1.2a
Release:	2
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 812243
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 804571
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751280
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 729652
- texlive-easyfig
- texlive-easyfig

