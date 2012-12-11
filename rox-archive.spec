%define name rox-archive
%define oname archive
%define version 2.1
%define release %mkrel 4
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

for gmo in %buildroot%appdir/*/Messages/*.gmo;do
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.1-4mdv2010.0
+ Revision: 433355
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1-3mdv2009.0
+ Revision: 242550
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-1mdv2008.0
+ Revision: 32404
- build fix


* Sun May 28 2006 Götz Waschk <waschk@mandriva.org> 2.1-1mdv2007.0
- fix file list
- New release 2.1
- use mkrel

* Fri Aug 26 2005 Götz Waschk <waschk@mandriva.org> 2.0-1mdk
- fix installation path
- fix source URL
- new version

* Mon Apr 18 2005 Götz Waschk <waschk@linux-mandrake.com> 1.9.5-1mdk
- update file list
- new version

* Fri Apr 01 2005 Götz Waschk <waschk@linux-mandrake.com> 1.9.4-2mdk
- rebuild

* Sun Mar 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.4-1mdk
- add translation files
- new version

* Wed Aug 20 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.3-1mdk
- drop prefix
- new version

* Tue Jul 08 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.2-2mdk
- fix directory ownership

* Fri Jun 20 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.2-1mdk
- put the documentation only in the appdir
- URL
- new version

