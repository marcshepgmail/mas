#!/usr/bin/perl -w


use strict;
use warnings;
use ExtUtils::Installed;
use File::Copy qw(copy);

my $good;
my $cgidload = "/etc/apache2/mods-enabled/cgid.load";
my $cgidconf = "/etc/apache2/mods-enabled/cgid.conf";
my $user;

#
# First, check if all the required modules have
# been installed inthe system this script will run on.
#
BEGIN {
    my @import_modules = (
	'DBI',
	'JSON',
	'CGI',
	'CGI::Carp ',
	'LWP::Simple',
	'Data::Dumper',
	'Perl6::Slurp',
        );

    my ($inst) = ExtUtils::Installed->new();
    my (@installed_modules) = $inst->modules();

    for ( @import_modules ) {
	my $result = `perl -e 'use $_; print "ok\n"'`;
		if ($result ne ''){
 		  print "Module $_ is installed \n";
		  $good=1;
		} else {
		  print "Module $_ is not installed please install it using /usr/bin/perl -MCPAN -e 'install $_' \n";
		  $good=0;
		}
    }

	if ($good eq 1 ){
	my $cgidload = "/etc/apache2/mods-enabled/cgid.load";
	my $cgidconf = "/etc/apache2/mods-enabled/cgid.conf";
	my $cgifile = "/opt/mas/cgi-default.conf";
	my $apachecgi = "/etc/apache/sites-enabled/cgi-default.conf";
	my $index = "/etc/apache/sites-enabled/index.html";
	my $dir = "/opt/mas/";
	print "All modules are installed \n";
	if ( -l $cgidload) {
        	print "cgi.load is enabled \n";	
	}else{
	my $link = `ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/`;
	}
	if ( -l $cgidconf) {
	        print "cgid.conf is enabled \n";
	}else{
	my $link = `ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/`;
	}
	copy $cgifile, $apachecgi;
	unlink $index;
	system("service apache2 reload");
	my ($login,$pass,$uid,$gid) = getpwnam("www-data")
	        or die "$user not in passwd file";

	chown $uid, $gid, $dir;
	}
}
