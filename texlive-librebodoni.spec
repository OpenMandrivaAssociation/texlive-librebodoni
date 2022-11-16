Name:		texlive-librebodoni
Version:	64431
Release:	1
Summary:	Libre Bodoni fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/librebodoni
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebodoni.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librebodoni.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Libre Bodoni fonts are designed by Pablo Impallari and
Rodrigo Fuenzalida, based on the 19th century Morris Fuller
Benton's.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/librebodoni
%{_texmfdistdir}/fonts/vf/impallari/librebodoni
%{_texmfdistdir}/fonts/type1/impallari/librebodoni
%{_texmfdistdir}/fonts/tfm/impallari/librebodoni
%{_texmfdistdir}/fonts/opentype/impallari/librebodoni
%{_texmfdistdir}/fonts/map/dvips/librebodoni
%{_texmfdistdir}/fonts/enc/dvips/librebodoni
%doc %{_texmfdistdir}/doc/fonts/librebodoni

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
