# TODO
# - make install re-entrant

%define		_name	Suedstern

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):   Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	3.2.2
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.barbarakaemper.de/download/bk_berlin_subway-%{version}.tar.bz2
# Source0-md5:	ee6c775ee1e1c28dc28855fc08ef36b0
URL:		http://kde-look.org/content/show.php?content=8236
Requires:	kde-icons-%{_name}
Requires:	kde-colorscheme-%{_name}
Requires:	kde-wallpaper-%{_name}
Requires:	kde-sounds-%{_name}
Requires:	kde-splash-%{_name}
Requires:	kde-decoration-icewm-%{_name}
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

%description -l pl.UTF-8
Motyw ikon Suedstern składa się z subtelnych, czerwonawych ikon, które
tworzą melancholijny nastrój. W tym pakiecie znajdziesz również:
schemat kolorów tworzący melancholijny, lekko brązowy wygląd, zdjęcia
ze stacji metra Berlin-Suedestern (południowy wschód) opracowane tak,
aby tworzy melancholijny klimat, podstawowe dźwięki KDE opracowane na
podstawie odgłosów ze stacji metra Berlin-Suedestern (południowy
wschód), obrazek startowy KDE oparty na zdjęciu wnętrza wagonu metra,
zegary dla odpowiednich tapet z tematu Suedestern. Działają w miejscu,
gdzie na tapecie znajduje się zegar metra oraz dekorację icewm z tłem
stylizowanym na drewno oraz prostymi i widocznymi przyciskami.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl.UTF-8):   Motyw ikon do kde  - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
The Suedstern icon theme consists of mild, red-colorized icons which
create a melancholic mood.

%description -n kde-icons-%{_name} -l pl.UTF-8
Motyw ikon Suedstern składa się z subtelnych, czerwonawych ikon, które
tworzą melancholijny nastrój.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):   Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
A colorscheme that creates a melancholic, mild brown look.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Schemat kolorów tworzący melancholijny, lekko brązowy wygląd.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl.UTF-8):   Tapeta do KDE - %{_name}
Group:		Themes
Requires:	/usr/share/wallpapers

%description -n kde-wallpaper-%{_name}
Melancholic photos of the Berlin-Suedestern (south-eastern) metro
station.

%description -n kde-wallpaper-%{_name} -l pl.UTF-8
Zdjęcia ze stacji metra Berlin-Suedestern (południowy wschód)
opracowane tak, aby tworzy melancholijny klimat.

%package -n kde-sounds-%{_name}
Summary:	KDE sounds - %{_name} theme
Summary(pl.UTF-8):   Dźwięki do KDE z motywu %{_name}
Group:		Themes
Requires:	/usr/share/wallpapers

%description -n kde-sounds-%{_name}
KDE sounds based on sound from the Berlin-Suedestern (south-eastern)
metro station.

%description -n kde-sounds-%{_name} -l pl.UTF-8
Podstawowe dźwięki KDE opracowane na podstawie odgłosów ze stacji
metra Berlin-Suedestern (południowy wschód).

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl.UTF-8):   Obrazek startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
A KDE splash screen featuring an inside of a metro car.

%description -n kde-splash-%{_name} -l pl.UTF-8
Obrazek startowy KDE oparty na zdjęciu wnętrza wagonu metra.

%package -n superkaramba-theme-%{_name}
Summary:	An XMMS skin %{_name} theme
Summary(pl.UTF-8):   Skórka dla XMMS-a z motywu %{_name}
Group:		Themes
Requires:	superkaramba

%description -n superkaramba-theme-%{_name}
Clocks for related background in the Suedestern KDE theme, which work
in the same place where the metro clocks are on the backgrounds.

%description -n superkaramba-theme-%{_name} -l pl.UTF-8
Zegary dla odpowiednich tapet z tematu Suedestern. Działają w miejscu,
gdzie na tapecie znajduje się zegar metra.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl.UTF-8):   Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
This package contains an icewm decoration which has a wooden
background and simple yet visible buttons.

%description -n kde-decoration-icewm-%{_name} -l pl.UTF-8
Ten pakiet zawiera dekorację icewm z tłem stylizowanym na drewno oraz
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

%files

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
