#! /usr/bin/perl -w
print "Content-type: text/html\n\n";

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use HTML::Entities;
 
my $file = '../data/corsi.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file); 

print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Corsi - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta name="keywords" content="WeGym, palestra, gym, padova, corsi, zumba, salsa, mma, boxe"/>
<meta name="description" content="WeGym - Corsi"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="viewport" content="width=device-width" />
<link href="../css/styles.css" rel="stylesheet" type="text/css" media="screen" />
<link href="../css/print.css" rel="stylesheet" type="text/css" media="print" />
<script type="text/javascript" src="../js/nav.js"></script>
</head>
<body>
  <div id="container">
    <div id="header" >
      <h1><span class="letteraRisalto">W</span>e<span class="letteraRisalto">G</span>ym</h1>
            <p id="motto">La palestra dei tuoi sogni</p>
        </div>
    <div id="path">
      <p>Ti trovi in: <a class="link_alter" href="index.cgi" xml:lang="en">Home</a> &gt; Corsi</p>
      <a class="aiuti" href="#corpo">Salta la navigazione</a>
    </div>
    
    <div id="right">
      <div id="login">
        <form action="login.cgi" method="post">
          <fieldset>
            <legend xml:lang="en">Admin</legend>
            <label for="utente" xml:lang="en">Username:</label>
            <input class="textBox" type="text" id="utente" name="username"/>
            <label for="password" xml:lang="en">Password:</label>
            <input class="textBox" type="password" id="password" name="password"/>      
            <input type="submit" id="submit_button" value="Entra"/>
          </fieldset>
        </form>
      </div>

      <!-- togliere questo div per rimuovere le news -->
            
    </div>

    <div id="nav">
      <ul>
        <li id="primo"><a class="navBtn" href="index.cgi" xml:lang="en">Home</a></li>
        <li><a class="navBtn" href="galleria.cgi">Galleria</a></li>
        <li class="active"><p>Corsi</p></li>
        <li><a class="navBtn" href="prodotti.cgi">Prodotti</a></li>
        <li id="ultimo"><a class="navBtn" href="info.cgi">Info</a></li>
      </ul> 
    </div>

    <div id="corpo">
      <div id="cont_corsi">
FIRST

foreach my $corso ($doc->findnodes('/corsi/corso')) {
      print "<div class=\"corso\">";
      foreach my $property ($corso) {
           my $titolo = $corso->findnodes('./titolo');
           my $img_corso = $corso->findnodes('./img_corso');
           my $alt  = $corso->findnodes('./alt');
           my $descrizione = $corso->findnodes('./descrizione');
           
          print "<h2>", encode_entities($titolo), "</h2>\n";           
          print "<div class=\"imgcorso\"><img src=\"../images/corsi/",encode_entities($img_corso),"\" alt=\"$alt\" /></div>";
          print "<p class=\"descr_corso\">", encode_entities($descrizione), "</p>";
      }
     print "</div>";
     print "\n";
}

print <<SECOND;
	        </div>
          <a class="aiuti" href="#nav">Vai alla navigazione</a>
		</div>
    <div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
          <img src="http://www.w3.org/Icons/valid-xhtml10" alt="" height="31" width="88" />
            <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
            <a id="link_admin" class="link_alter" href="login_admin.cgi">Amministrazione</a>
        <div id="diritti"><p>&copy; 2016 Gruppo <span xml:lang="en">WeGym</span></p></div>
    </div>
  </div>
</body>
</html>

SECOND

exit;