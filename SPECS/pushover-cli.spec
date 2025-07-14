%define debug_package %{nil}

%global gh_user     jc21
%global gh_commit   5637738e1a55a9bcc2d868ce09a1a32f4cda2090
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

# see https://fedoraproject.org/wiki/PackagingDrafts/Go#Build_ID
%global _dwz_low_mem_die_limit 0

Name:           pushover-cli
Version:        1.0.1
Release:        1%{?dist}
Summary:        A simple terminal UI for git commands, written in Go with the gocui library
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/%{version}.tar.gz
BuildRequires:  git golang

%description
Are YOU tired of typing every git command directly into the terminal, but
you're too stubborn to use Sourcetree because you'll never forgive Atlassian
for making Jira? This is the app for you!

%prep
%setup -q -n %{name}-%{version}

%build
export LDFLAGS="${LDFLAGS} -X main.GitCommit=%{gh_short} -X main.AppVersion=%{version}"
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Apr 8 2019 Jamie Curnow <jc@jc21.com> 1.0.1-1
- Initial Spec
