
%define         _name	Suedstern

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	3.2.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.barbarakaemper.de/download/bk_berlin_subway-%{version}.tar.bz2
# Source0-md5:	ee6c775ee1e1c28dc28855fc08ef36b0
URL:		http://kde-look.org/content/show.php?content=8236
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Suedstern icon theme consists of mild, red-colorized icons which
create a melancholic mood. Here you will also find: a colorscheme that
creates a melancholic, mild brown look, melancholic photos of the
Berlin-Suedestern (south-eastern) metro station,a KDE splash screen
featuring an inside of a metro car, clocks for related background in
the Suedestern KDE theme, which work in the same place where the metro
clocks are on the backgrounds and an icewm decoration which has a
wooden background and simple yet visible buttons.

%description -l pl
Motyw ikon Suedstern sk³ada siê z subtelnych, czerwonawych ikon, które
tworz± melancholijny nastrój. W tym pakiecie znajdziesz równie¿:
schemat kolorów tworz±cy melancholijny, lekko br±zowy wygl±d, zdjêcia
ze stacji metra Berlin-Suedestern (po³udniowy wschód) opracowane tak,
aby tworzy melancholijny klimat, podstawowe d¼wiêki KDE opracowane na
podstawie odg³osów ze stacji metra Berlin-Suedestern (po³udniowy
wschód), obrazek startowy KDE oparty na zdjêciu wnêtrza wagonu metra,
zegary dla odpowiednich tapet z tematu Suedestern. Dzia³aj± w miejscu,
gdzie na tapecie znajduje siê zegar metra oraz dekoracjê icewm z t³em
stylizowanym na drewno oraz prostymi i widocznymi przyciskami.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl):	Motyw ikon do kde  - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
The Suedstern icon theme consists of mild, red-colorized icons which
create a melancholic mood.

%description -n kde-icons-%{_name} -l pl
Motyw ikon Suedstern sk³ada siê z subtelnych, czerwonawych ikon, które
tworz± melancholijny nastrój.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
A colorscheme that creates a melancholic, mild brown look.

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów tworz±cy melancholijny, lekko br±zowy wygl±d.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl):	Tapeta do KDE - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
Melancholic photos of the Berlin-Suedestern (south-eastern) metro
station.

%description -n kde-wallpaper-%{_name} -l pl
Zdjêcia ze stacji metra Berlin-Suedestern (po³udniowy wschód)
opracowane tak, aby tworzy melancholijny klimat.

%package -n kde-sounds-%{_name}
Summary:	KDE sounds - %{_name} theme
Summary(pl):	D¼wiêki do KDE z motywu %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-sounds-%{_name}
KDE sounds based on sound from the Berlin-Suedestern (south-eastern)
metro station.

%description -n kde-sounds-%{_name} -l pl
Podstawowe d¼wiêki KDE opracowane na podstawie odg³osów ze stacji
metra Berlin-Suedestern (po³udniowy wschód).

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl):	Obrazek startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
A KDE splash screen featuring an inside of a metro car.

%description -n kde-splash-%{_name} -l pl
Obrazek startowy KDE oparty na zdjêciu wnêtrza wagonu metra.

%package -n superkaramba-theme-%{_name}
Summary:	An xmms skin %{_name} theme
Summary(pl):	Skórka dla XMMS-a z motywu %{_name}
Group:		Themes
Requires:	superkaramba

%description -n superkaramba-theme-%{_name}
Clocks for related background in the Suedestern KDE theme, which work
in the same place where the metro clocks are on the backgrounds.

%description -n superkaramba-theme-%{_name} -l pl
Zegary dla odpowiednich tapet z tematu Suedestern. Dzia³aj± w miejscu,
gdzie na tapecie znajduje siê zegar metra.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl):	Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
This package contains an icewm decoration which has a wooden
background and simple yet visible buttons.

%description -n kde-decoration-icewm-%{_name} -l pl
Ten pakiet zawiera dekoracjê icewm z t³em stylizowanym na drewno oraz
prostymi i widocznymi przyciskami.

%prep
%setup -q -n bk_subway-3.2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/Suedestern
install -d $RPM_BUILD_ROOT%{_iconsdir}/Suedestern
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/Suedestern
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/Suedestern
install -d $RPM_BUILD_ROOT%{_datadir}/{wallpapers,sounds}

cd theme_content
mv -f bk_berlin_subway_icons-3.1/* $RPM_BUILD_ROOT%{_iconsdir}/Suedestern
mv -f colors/bk_berlin_subway.kcsrc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
mv -f bk_berlin_subway_splash/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/Suedestern
mv -f bk_berlin_subway_IceWM/* $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/Suedestern
mv -f wallpapers/* $RPM_BUILD_ROOT%{_datadir}/wallpapers
mv -f bk_berlin_subway_sounds/* $RPM_BUILD_ROOT%{_datadir}/sounds
mv -f bk_berlin_subway_superkaramba/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/Suedestern

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde-sounds-%{_name}
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files -n kde-splash-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Suedestern

%files -n kde-decoration-icewm-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n superkaramba-theme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/Suedestern
