#!/usr/bin/perl
print header('application/json');
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use DBI;
use JSON;



my $driver   = "SQLite";
my $database = "blog.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
                      or die $DBI::errstr;

my $stmt = qq(SELECT post_id, title, body  from posts;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0){
   print $DBI::errstr;
}

my $ref;
while($ref = $sth->fetchrow_hashref) {
	my $json = encode_json \%$ref;	
	print "$json\n";
}

$dbh->disconnect();
