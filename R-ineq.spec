%global packname  ineq
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2_10
Release:          2
Summary:          Measuring Inequality, Concentration, and Poverty
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-10.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats R-graphics R-grDevices 
Requires:         R-stats R-graphics R-grDevices 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-graphics R-grDevices
BuildRequires:    R-stats R-graphics R-grDevices 

%description
Inequality, concentration, and poverty measures. Lorenz curves (empirical
and theoretical).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2_10-1
+ Revision: 777008
- Import R-ineq
- Import R-ineq

