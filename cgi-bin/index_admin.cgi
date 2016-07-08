#! /usr/bin/perl -w

use XML::LibXML;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;
use CGI::Session;

$cgi = new CGI;
$sid = $cgi->param("sid");
$session = CGI::Session->load($sid) or die "$!";

if ($session->param("logged") ne "admin") {
  $url = "index.cgi";
  print "Location: $url\n\n";
}

print "Content-type: text/html\n\n";
print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
  <title>Home - WeGym</title>
  <meta name="author" content="WeGym TW Group 15/16" />
  <meta name="copyright" content="Gruppo WeGym"/>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width" />
  <link href="../css/styles.css" rel="stylesheet" type="text/css" media="screen" />
  <link href="../css/print.css" rel="stylesheet" type="text/css" media="print" />
  <script type="text/javascript" src="../js/nav.js"></script></head>
<body>
  <div id="container">
    <div id="header" >
            <h1><span class="letteraRisalto">W</span>e<span class="letteraRisalto">G</span>ym - <span class="letteraRisalto">A</span>dmin</h1>
            <p id="motto">La palestra dei tuoi sogni</p>
        </div>
    <div id="path">
      <p>Ti trovi in: <span xml:lang="en">Home</span> Amministratore </p> 
    </div>
    
    <div id="right">
      <div id="login">
        <form action="logout.cgi?sid=$sid" method="post">
          <fieldset>
          <legend>Stato</legend>
            <p>Loggato come Admin</p>   
            <input type="submit" id="submit_button" value="Esci"/>
          </fieldset>
        </form>
      </div>

      <!-- togliere questo div per rimuovere le news -->
            
    </div>

    <div id="nav">
      <ul> 
        <li id="primo"><a class="navBtn" href="corsi_admin.cgi?sid=$sid">Corsi</a></li>
        <li><a class="navBtn" href="galleria_admin.cgi?sid=$sid">Galleria</a></li>
        <li id="ultimo"><a class="navBtn" href="prodotti_admin.cgi?sid=$sid">Prodotti</a></li>
        <li id="amministrazioneBtn"><a class="navBtn" href="logout.cgi">Esci</a></li>
      </ul> 
    </div>

    <div id="corpo">
      <h2>PANNELLO DI AMMINISTRAZIONE</h2>
      <p>Benvenuto nel pannello di amministrazione, dal qui puoi gestire i corsi, le immagini della galleria e i prodotti esposti nel sito. </p>
    </div>
    <div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
          <img src="http://www.w3.org/Icons/valid-xhtml10" alt="" />
            <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
        <div id="diritti"><p>&copy; 2016 Gruppo <span xml:lang="en">WeGym</span></p></div>
    </div>
  </div>
</body>
</html>

FIRST


exit;

