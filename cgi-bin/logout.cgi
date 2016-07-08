#! /usr/bin/perl -w

use CGI;
use CGI::Session;
#load existing session
$cgi = new CGI;
$sid = $cgi->param("sid");
$session = CGI::Session->load($sid) or die "$!";
#delete it
undef($session);
#redirect
$url = "index.cgi";
print "Location: $url\n\n";

exit;