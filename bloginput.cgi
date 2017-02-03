#!/usr/bin/perl
print "Content-Type: text/html\n\n";
#use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use DBI;
use JSON;
use JSON qw( decode_json );
use lib qw( ..);
use LWP::Simple;
use Data::Dumper;
use Perl6::Slurp;

my $postid;

my $filename = 'blogin.json';
my $json = slurp $filename;
$text = decode_json($json);
$body = $text->{'post'}{'body'};
$title = $text->{'post'}{'title'};


my $driver   = "SQLite"; 
my $database = "blog.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) 
                      or die $DBI::errstr;

my $stmt = qq(SELECT post_id  from posts;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0){
   print $DBI::errstr;
}
while(my @row = $sth->fetchrow_array()) {
      $postid = $row[0];
	#print "postid is :" . $postid;
	if ($postid ne "")
	{
	++$postid;	
	#print "Incremented postid is :" . $postid;
	}else{
	$postid=1000001;
	} 
      
}
print "Operation Completed, blog post " . $postid  . " recorded". "<br>";

my $sth = $dbh->prepare('INSERT INTO posts VALUES (?, ?, ?)');
$sth->execute($postid, $title, $body);

$dbh->disconnect();

