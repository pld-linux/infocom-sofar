%define		_name		SoFar
Summary:	Infocom text game - So Far
Summary(pl):	Tekstówka Infocomu - So Far
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

%description -l pl
Gdy siedzisz w zat³oczonym teatrze i z³o¶cisz siê na swojego partnera,
który najwyra¼niej siê nie pojawi³ dziwnie zaintrygowa³ ciê pr±d
powietrza. Doprowadzi ciê on do miejsca mocno ró¿ni±cego siê od
twojego zwyk³ego otoczenia...

Nagrody XYZZY 1996: za najlepsz± grê, za najlepszy tekst, za najlepsze
³amig³ówki, za najlepsz± indywidualn± ³amig³ówkê.

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
