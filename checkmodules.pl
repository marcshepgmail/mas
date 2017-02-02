#!/usr/bin/perl -w


use strict;
use warnings;

use ExtUtils::Installed;

#
# First, check if all the required modules have
# been installed inthe system this script will run on.
#
BEGIN {
    my @import_modules = (
	'DBI',
	'JSON',
	'CGI',
	'LWP::Simple',
	'Data::Dumper',
	'Perl6::Slurp',
        );

    my ($inst) = ExtUtils::Installed->new();
    my (@installed_modules) = $inst->modules();

    for ( @import_modules ) {

        eval{ $inst->validate($_) };
        if($@) {
            print qq{\n
	Module $_ does not seem to be installed in this system.
	Please install the module and try again!\n
	};
            exit 1;

        } 

    } 

} 
