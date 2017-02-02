#!/usr/bin/perl
print "Content-Type: text/html\n\n";
#use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use JSON;
use JSON qw( decode_json );
use lib qw( ..);
use LWP::Simple;
use Data::Dumper;
use Perl6::Slurp;


my $json = '{
        "title": "testme blogpost",
        "body": "This is the body of the blogpost"
}';
 
my $decoded = decode_json($json);
 
#print "title:" . $decoded->{'title'}. "\:". " body:" . $decoded->{'body'}.     "\n";

my $filename = 'blogin.json';
my $json = slurp $filename;

$text = decode_json($json);
print "title = " . $text->{'post'}{'title'} . "\n";
print "body = " . $text->{'post'}{'body'} . "\n";

