#!/usr/bin/perl

use CGI qw(:cgi-lib :escapeHTML :unescapeHTML);
use CGI::Carp qw(fatalsToBrowser);
use File::Basename qw(dirname);
use lib dirname(__FILE__) . '/libs';
use Data::Dumper;
use Lib::FileSystem;

$|=1;
ReadParse();

print "Content-type: text/html; charset=utf8\n\n"; 

my $obj = Lib::FileSystem->new();
my $filePath = 'index.html';
my %nav = ('1'=>'Main',
	    '2'=>'Services',
	    '3'=>'About',
	    '4'=>'Galery',
	    '5'=>'Contacts'
	   );
my $html = $obj->getFileContent($filePath);
$html =~s/{{(\d+)}}/$nav{$1}/gie;

#print Dumper($html);
print $html;
#print "<pre>" . Dumper(\%ENV) . "</pre>";
