%define		_name		SoFar

Summary:	Infocom text game - So Far
Summary(pl):	Tekstówka Infocomu - So Far
Name:		infocom-sofar
Version:	961218
Release:	1
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z8
# Source0-md5:	9ed2128ac97285ddf44650178629f477
URL:		http://www.ifarchive.org/
Requires:	frotz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
itting in a cramped theatre, irritated that your partner apparently
hasn't turned up, you are strangely intrigued by a current of air. It
will lead you to a place very different from your own familiar
surroundings...

XYZZY Awards 1996: Best Game, Best Writing, Best Puzzles, Best
Individual Puzzle

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/games/zcode

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z8
