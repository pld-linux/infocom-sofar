%define		_name		SoFar
Summary:	Infocom text game - So Far
Summary(pl.UTF-8):	Tekstówka Infocomu - So Far
Name:		infocom-sofar
Version:	961218
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z8
# Source0-md5:	9ed2128ac97285ddf44650178629f477
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Sitting in a cramped theatre, irritated that your partner apparently
hasn't turned up, you are strangely intrigued by a current of air. It
will lead you to a place very different from your own familiar
surroundings...

XYZZY Awards 1996: Best Game, Best Writing, Best Puzzles, Best
Individual Puzzle.

%description -l pl.UTF-8
Gdy siedzisz w zatłoczonym teatrze i złościsz się na swojego partnera,
który najwyraźniej się nie pojawił dziwnie zaintrygował cię prąd
powietrza. Doprowadzi cię on do miejsca mocno różniącego się od
twojego zwykłego otoczenia...

Nagrody XYZZY 1996: za najlepszą grę, za najlepszy tekst, za najlepsze
łamigłówki, za najlepszą indywidualną łamigłówkę.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z8
