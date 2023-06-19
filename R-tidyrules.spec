#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyrules
Version  : 0.1.5
Release  : 10
URL      : https://cran.r-project.org/src/contrib/tidyrules_0.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyrules_0.1.5.tar.gz
Summary  : Obtain Rules from Rule Based Models as Tidy Dataframe
Group    : Development/Tools
License  : GPL-3.0
Requires: R-assertthat
Requires: R-magrittr
Requires: R-partykit
Requires: R-purrr
Requires: R-stringr
Requires: R-tibble
BuildRequires : R-AmesHousing
BuildRequires : R-C50
BuildRequires : R-Cubist
BuildRequires : R-assertthat
BuildRequires : R-dplyr
BuildRequires : R-magrittr
BuildRequires : R-mlbench
BuildRequires : R-modeldata
BuildRequires : R-partykit
BuildRequires : R-purrr
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
# tidyrules
<!-- badges: start -->
[![Build
Status](https://travis-ci.org/talegari/tidyrules.svg?branch=master)](https://travis-ci.org/talegari/tidyrules)
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/tidyrules)](https://cran.r-project.org/package=tidyrules)
<!-- badges: end -->

%prep
%setup -q -c -n tidyrules
cd %{_builddir}/tidyrules

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641138513

%install
export SOURCE_DATE_EPOCH=1641138513
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyrules
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyrules
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyrules
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tidyrules || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyrules/DESCRIPTION
/usr/lib64/R/library/tidyrules/INDEX
/usr/lib64/R/library/tidyrules/Meta/Rd.rds
/usr/lib64/R/library/tidyrules/Meta/features.rds
/usr/lib64/R/library/tidyrules/Meta/hsearch.rds
/usr/lib64/R/library/tidyrules/Meta/links.rds
/usr/lib64/R/library/tidyrules/Meta/nsInfo.rds
/usr/lib64/R/library/tidyrules/Meta/package.rds
/usr/lib64/R/library/tidyrules/Meta/vignette.rds
/usr/lib64/R/library/tidyrules/NAMESPACE
/usr/lib64/R/library/tidyrules/NEWS.md
/usr/lib64/R/library/tidyrules/R/tidyrules
/usr/lib64/R/library/tidyrules/R/tidyrules.rdb
/usr/lib64/R/library/tidyrules/R/tidyrules.rdx
/usr/lib64/R/library/tidyrules/doc/index.html
/usr/lib64/R/library/tidyrules/doc/tidyrules_vignette.R
/usr/lib64/R/library/tidyrules/doc/tidyrules_vignette.Rmd
/usr/lib64/R/library/tidyrules/doc/tidyrules_vignette.html
/usr/lib64/R/library/tidyrules/help/AnIndex
/usr/lib64/R/library/tidyrules/help/aliases.rds
/usr/lib64/R/library/tidyrules/help/paths.rds
/usr/lib64/R/library/tidyrules/help/tidyrules.rdb
/usr/lib64/R/library/tidyrules/help/tidyrules.rdx
/usr/lib64/R/library/tidyrules/html/00Index.html
/usr/lib64/R/library/tidyrules/html/R.css
/usr/lib64/R/library/tidyrules/tests/testthat.R
/usr/lib64/R/library/tidyrules/tests/testthat/test-c5.R
/usr/lib64/R/library/tidyrules/tests/testthat/test-cubist.R
/usr/lib64/R/library/tidyrules/tests/testthat/test-rpart.R
