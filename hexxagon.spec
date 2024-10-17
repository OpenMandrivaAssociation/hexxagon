Name:		hexxagon
Summary:	Othello clone (GTK version)
Version:	1.0.2
Release:	2
Group:		Games/Boards
License:	GPLv2+
Url:		https://nesqi.se/hexxagon/
Source0:	http://nesqi.se/download/%{name}-%{version}.tar.bz2
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
Patch0:		hexxagon-1.0-fix-build.patch
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	pkgconfig(gtkmm-2.4)

%description
Hexxagon is a clone of Hexxagon, an adaptation of
the Othello board game written for DOS.
This is the GTK1 version of Hexxagon.

%prep
%setup -q
%patch0 -p1 -b .fix-build

%build
%configure2_5x
%make

%install
%makeinstall bindir=%{buildroot}%{_gamesbindir}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;BoardGame;
Name=Hexxagon
Comment=Othello clone
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_liconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_miconsdir}/%{name}.png

%files
%doc README
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}*.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/%{name}



%changelog
* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 1.0-3mdv2010.0
+ Revision: 376086
- fix build
- remove non working desktop file for text mode hexxagon
- fix licence

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - do not harcode icon extension
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
    - import hexxagon

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Apr 23 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.0-2mdk
- Add BuildRequires

* Thu Apr 06 2006 Lenny Cartier <lenny@mandriva.com> 1.0-1mdk
- 1.0

* Sun Apr 03 2005 Michael Scherer <misc@mandrake.org> 0.3.3-2mdk
- Rebuild for readline

* Tue Nov 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.3-1mdk
- 0.3.3

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 0.3.2-2mdk 
- rebuild for new gcc

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.2-1mdk
- 0.3.2
- drop P0 (fixed upstream)
- bzip2 source
- drop COPYING file as it's GPL

* Sun Nov  16 2003 Olivier Blin <oliv.blin@laposte.net> 0.3.1-1mdk
- initial release
- multline strings patch for gcc 3.3 (patch0)
