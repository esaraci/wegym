#! /usr/bin/perl -w


use XML::LibXML;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;

use CGI::Session;
$session = new CGI::Session();
$id = $session->id;

#find utenti.xml and give handle
$filexml_path = '../data/utenti.xml';
$parser = XML::LibXML->new();
$doc = $parser->parse_file($filexml_path);
 

#data from input
$cgi = new CGI;
$username = $cgi->param('username');
$password = $cgi->param('password');

#data from xml
$username_xml = $doc->findnodes("/utenti/utente[username = '$username']/username"); #filename of img 
$hashed_password_xml = $doc->findnodes("/utenti/utente[username = '$username']/hashed_password"); #filename of img 

#se esiste l'utente 
if (!($username_xml eq "")) {
    #aggiungi utente a sessione
    $pwd = crypt($password, "TW16");
    if ($pwd eq $hashed_password_xml) {
       $session->param("logged" => $username); 
       $session->expire('+1h'); #session will expire after 1 hour of use
       $url = "index_admin.cgi?sid=$id";
    }
    else { #pwd sbagliata
      $url = "login_admin.cgi?errore=1";
    }
}
#altrimenti se nome utente sbagliato o non inserito (e pass sbagliata o no inserita)
else {
  $url = "login_admin.cgi?errore=1";
}

print "Location: $url\n\n";



exit;

