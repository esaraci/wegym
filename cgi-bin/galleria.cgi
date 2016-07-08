#! /usr/bin/perl -w
print "Content-type: text/html\n\n";

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use HTML::Entities;
 
$file = '../data/galleria.xml';
$parser = XML::LibXML->new();
$doc = $parser->parse_file($file);
 
print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Galleria - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta name="keywords" content="WeGym, palestra, gym, padova, galleria, spogliatoi, sauna, sala, corsi, sala, pesi, sala, massaggi, docce"/>
<meta name="description" content="WeGym - Galleria"/>
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
      <p>Ti trovi in: <a class="link_alter" href="index.cgi" xml:lang="en">Home</a> &gt; Galleria</p>
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
        <li class="active"><p>Galleria</p></li>
        <li><a class="navBtn" href="corsi.cgi">Corsi</a></li>
        <li><a class="navBtn" href="prodotti.cgi">Prodotti</a></li>
        <li id="ultimo"><a class="navBtn" href="info.cgi">Info</a></li>
      </ul> 
    </div>

    <div id="corpo">
          <div id="galleria_cont">
FIRST

foreach my $foto ($doc->findnodes('/galleria/foto')) {
	    print "<div class=\"foto_galleria\">";
      foreach my $property ($foto) {
           my $titolo = $foto->findnodes('./titolo');
           my $img_galleria = $foto->findnodes('./img_galleria');
           my $alt  = $foto->findnodes('./alt');
    
           print "<h2>", encode_entities($titolo), "</h2>\n";
           print "<img src=\"../images/galleria/", encode_entities($img_galleria), "\" alt=\"$alt\" />";
      }
	   print "</div>";
     print "\n";
}
	        		
print <<SECOND;
            <a class="aiuti" href="#nav">Vai alla navigazione</a>
	        	</div>
	        	
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