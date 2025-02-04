Name:		texlive-dancers
Version:	13293
Release:	2
Summary:	Font for Conan Doyle's "The Dancing Men"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dancers/dancers.mf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dancers.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (Sherlock Holmes) book contains a code which uses dancing
men as glyphs. The alphabet as given is not complete, lacking
f, j, k, q, u, w, x and z, so those letters in the font are not
due to Conan Doyle. The code required word endings to be marked
by the dancing man representing the last letter to be holding a
flag: these are coded as A-Z.
thaTiStOsaYsentenceSiNthEcodElooKlikEthiS. In some cases, the
man has no arms, making it impossible for him to hold a flag.
In these cases, he is wearing a flag on his hat in the
'character'. The font is distributed as MetaFont source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/dancers/dancers.mf
%{_texmfdistdir}/fonts/tfm/public/dancers/dancers.tfm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
