%define name rox-archive
%define oname archive
%define version 2.1
%define release %mkrel 1
%define appdir %_prefix/lib/apps
Summary: Create and read archive files with the ROX desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/sourceforge/rox/%{oname}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
URL: http://rox.sf.net/archive.html
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: rox-lib
Buildarch: noarch

%description
You can use this program to compress a directory or file into a
single, smaller file (which can be stored, emailed, etc).

You can also use it to extract a compressed archive back into a
file or directory structure.


%prep
%setup -q -n %oname-%version

%build

%install
rm -rf $RPM_BUILD_ROOT %name.lang
mkdir -p %buildroot/%appdir
cp -r Archive %buildroot/%appdir
rm -f %buildroot%appdir/Archive/Messages/dist
rm -f %buildroot%appdir/Archive/Messages/*po
rm -rf %buildroot%appdir/Archive/tests
chmod 644 %buildroot%appdir/*/*.xml

for gmo in %buildroot%_libdir/apps/*/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc %appdir/Archive/Help
%dir %appdir/Archive/
%appdir/Archive/AppRun
%appdir/Archive/.DirIcon
%appdir/Archive/*.py
%appdir/Archive/AppInfo.xml
%appdir/Archive/Archive.xml
%dir %appdir/Archive/Messages

