Name:		hexxagon
Summary:	Othello clone (GTK version)
Version:	1.0
Release:	%mkrel 2
Url:		http://nesqi.homeip.net/hexxagon/
Source0:	http://nesqi.homeip.net/hexxagon/download/%{name}-%{version}.tar.bz2
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
Group:		Games/Boards
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+1.2-devel
BuildRequires:  gtkmm2.4-devel

%description
Hexxagon is a clone of Hexxagon, an adaptation of
the Othello board game written for DOS.
This is the GTK1 version of Hexxagon.

%prep
%setup -q
%configure 

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir}

#install -m755 src/%{name}-gtk/%{name} -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
#install -m755 src/%{name}-text/%{name}_text -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}-text

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=BoardGame;
Name=Hexxagon (GTK)
Comment=Othello clone
EOF

cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}-text.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=BoardGame;
Name=Hexxagon (text)
Comment=Othello clone
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}*.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/%name

