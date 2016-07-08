#! /usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;
use URI::Escape;
use CGI::Session;

$cgi = new CGI;
$sid = $cgi->param("sid");
$session = CGI::Session->load($sid) or die "$!";

if ($session->param("logged") ne "admin") {
  $url = "index.cgi";
  print "Location: $url\n\n";
}

my $file = '../data/galleria.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

print "Content-type: text/html\n\n";

print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Amministra Galleria - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="viewport" content="width=device-width" />
<link href="../css/styles.css" rel="stylesheet" type="text/css" media="screen" />
<link href="../css/print.css" rel="stylesheet" type="text/css" media="print" />
<script type="text/javascript" src="../js/nav.js"></script>
</head>
<body>
  <div id="container">
    <div id="header" >
      <h1><span class="letteraRisalto">W</span>e<span class="letteraRisalto">G</span>ym - <span class="letteraRisalto">A</span>dmin</h1>
            <p id="motto">La palestra dei tuoi sogni</p>
        </div>
    <div id="path">
      <p>Ti trovi in: Galleria</p>  
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
        <li class="active"><p>Galleria</p></li>
        <li id="ultimo"><a class="navBtn" href="prodotti_admin.cgi?sid=$sid">Prodotti</a></li>
        <li id="amministrazioneBtn"><a class="navBtn" href="logout.cgi">Esci</a></li>
      </ul> 
    </div>
    <div id="corpo">
FIRST
   

   my $count = $doc->findnodes("/galleria/foto")->size();

if ($count eq 0) {
    print "<p>Nessuna immagine trovata nel database.</p>";
} else {

    print "<p class=\"messaggio\">", $session->param("messaggio"), "</p>";
    print "<table summary=\"Tabella contenente le immagini presenti nella galleria del sito e con la possibilità di eliminarle singolarmente con il tasto Elimina alla destra di ognuna di esse\">";
    print "<caption>Galleria</caption><tbody>";
    print "<tr><th scope=\"col\">Titolo</th><th scope=\"col\">Elimina</th></tr>";

    

    foreach my $foto ($doc->findnodes('/galleria/foto')) {
      foreach my $property ($foto) {
           my $titolo = $foto->findnodes('./titolo');
           my $titolo_enc = uri_escape($titolo);
           my $img_galleria = $foto->findnodes('./img_galleria');
           my $alt  = $foto->findnodes('./alt');
    
           print "<tr><td scope=\"row\">$titolo</td>";
           print "<td><a href=\"cancella_immagine_galleria.cgi?titolo=$titolo_enc&amp;&amp;sid=$sid\" title=\"Elimina $titolo\">Elimina</a></td></tr>"
      }
    }

    print "</tbody></table>";   
    $session->param("messaggio" => "");
}

print <<SECOND; 
    <form id="form_admin" action="nuova_immagine_galleria.cgi?sid=$sid" method="post" enctype="multipart/form-data" class="universal_form">
          <fieldset>
            <legend>NUOVA IMMAGINE GALLERIA</legend>
            <label for="titolo">Titolo :</label><input type="text" name="titolo" id="titolo"/>
            <label for="img_galleria">Immagine :</label><input type="file" name="img_galleria" id="img_galleria"/>
            <label for="alt">Alt :</label><textarea name="alt" id="alt" rows="1" cols="40"></textarea>
            <input type="submit" value="Crea" />  
            </fieldset>
      </form> 
    </div>
    <div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
          <img src="http://www.w3.org/Icons/valid-xhtml10" alt="" />
            <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
       <div id="diritti"><p>&copy; 2016 Gruppo <span xml:lang="en">WeGym</span></p></div>
    </div>
  </div>
</body>
</html>

SECOND

exit;