# revision 13293
# category Package
# catalog-ctan /fonts/dancers/dancers.mf
# catalog-date 2008-11-24 17:20:15 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-dancers
Version:	20081124
Release:	2
Summary:	Font for Conan Doyle's "The Dancing Men"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dancers/dancers.mf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dancers.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081124-2
+ Revision: 750762
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081124-1
+ Revision: 718199
- texlive-dancers
- texlive-dancers
- texlive-dancers
- texlive-dancers

