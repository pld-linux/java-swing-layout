%define		srcname		swing-layout
Summary:	Natural layout for Swing panels
Name:		java-%{srcname}
Version:	1.0.4
Release:	1
License:	LGPL v2
Group:		Libraries/Java
# https://svn.java.net/svn/swing-layout~svn/trunk/
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/swing-layout/%{srcname}-%{version}-src.zip/dddf900113dfd94658d0d0504cb78a8c/%{srcname}-%{version}-src.zip
# Source0-md5:	dddf900113dfd94658d0d0504cb78a8c
# from http://java.net/jira/secure/attachment/27303/pom.xml
# use javac target/source 1.5
Patch0:		project_properties.patch
Patch1:		fix-incorrect-fsf-address.patch
URL:		https://swing-layout.dev.java.net/
BuildRequires:	ant
BuildRequires:	jdk >= 1.3
BuildRequires:	jpackage-utils >= 1.6
Requires:	jre >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensions to Swing to create professional cross platform layout.

%prep
%setup -q -n %{srcname}-%{version}
%undos releaseNotes.txt COPYING nbproject/project.properties
%patch -P0 -p0
%patch -P1 -p0

%build
%ant jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc releaseNotes.txt COPYING
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar
