%global tl_name easyfig
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Simplifying the use of common figures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easyfig
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfig.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the command \Figure[<key=value>...]{<image
filename>} to simplify the business of including an image as figure in
the most common form (centred and with caption and label). Caption and
label are set using the caption and label keys; the label fig:<image
filename> is used if none is given. If the here key is given, the figure
is not 'floated', and the user is responsible for placement. The package
uses the author's package adjustbox to centre an image and to simplify
further modifications. As adjustbox now provides keys to turn images or
other material into floats or non-floats, including captions, easyfig
has become quite redundant.

