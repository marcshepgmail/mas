#!/usr/bin/perl
print "Content-Type: text/html\n\n";
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use DBI;
use JSON;


my $driver   = "SQLite";
my $database = "blog.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
                      or die $DBI::errstr;
print "Opened database successfully\n";

my $stmt = qq(SELECT post_id, title, body  from posts;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0){
   print $DBI::errstr;
}

while(my @row = $sth->fetchrow_array()) {
      print "post_ID = ". $row[0] . "\n";
      print "Title = ". $row[1] ."\n";
      print "Body = ". $row[2] ."\n";
}
print "Operation done successfully\n";
$dbh->disconnect();
