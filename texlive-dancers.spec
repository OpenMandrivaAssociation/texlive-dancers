# revision 13293
# category Package
# catalog-ctan /fonts/dancers/dancers.mf
# catalog-date 2008-11-24 17:20:15 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-dancers
Version:	20081124
Release:	1
Summary:	Font for Conan Doyle's "The Dancing Men"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dancers/dancers.mf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dancers.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

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
%{_texmfdistdir}/fonts/source/public/dancers/dancers.mf
%{_texmfdistdir}/fonts/tfm/public/dancers/dancers.tfm
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
