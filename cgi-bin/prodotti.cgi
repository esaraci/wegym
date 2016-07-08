#! /usr/bin/perl -w
print "Content-type: text/html\n\n";

use XML::LibXML;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;


 
my $file = '../data/prodotti.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
$cgi = new CGI;

#default or not values for categoria, prezzomin, prezzomax
$pmin = (defined $cgi->param("prezzomin"))? $cgi->param("prezzomin"): 0;
$pmax = (defined $cgi->param("prezzomax"))? $cgi->param("prezzomax"): 150;

$ok = "nok";
if ($pmin =~ /^\d+$/ && $pmax =~ /^\d+$/) { 
    $ok = "ok";
} 

print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Prodotti - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta name="keywords" content="WeGym, palestra, gym, padova, prodotti, guanti, t-shirt, pantaloncini, integratori, cibi, snacks, marca, prezzo"/>
<meta name="description" content="WeGym - Prodotti"/>
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
      <p>Ti trovi in: <a class="link_alter" href="index.cgi" xml:lang="en">Home</a> &gt; Prodotti</p>
      <a class="aiuti" href="#ricerca">Vai alla ricerca</a>
    </div>
    
    <div class="ricerca_corsi cors_mod" id="right">
      <div class="togliere" id="login">
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
      <a class="aiuti" href="#corpo">Vai ai prodotti</a>
      <a class="aiuti" href="#nav">Vai alla navigazione</a>
      <div id="ricerca" class="cors_modifica">
        <form action="prodotti.cgi" method="post">
          <fieldset>
            <legend>Filtra</legend>
            <select name="categoria" title="categoria">
             <option value="tutti">Tutti</option>
             <option value="guanti">Guanti</option>
             <option value="tshirt">T-Shirt</option>
             <option value="pantaloncini">Pantaloncini</option>
             <option value="integratori">Integratori</option>
             <option value="snacks">Cibi</option>
            </select>
            <label for="prezzomin"><abbr title="Minimo">Min.</abbr> (€)</label>
            <input class="textBox prezzoTextBox" type="text" id="prezzomin" name="prezzomin" value="$pmin"/>
            <label for="prezzomax"><abbr title="Massimo">Max.</abbr> (€)</label>
            <input class="textBox prezzoTextBox" type="text" id="prezzomax" name="prezzomax" value="$pmax"/>      
            <input type="submit" id="filtra_button" value="Filtra"/>
          </fieldset>
        </form>
        <a class="aiuti" href="#corpo">Vai ai prodotti</a>
      </div>            
    </div>

  <div id="nav">
      <ul>
        <li id="primo"><a class="navBtn" href="index.cgi" xml:lang="en">Home</a></li>
        <li><a class="navBtn" href="galleria.cgi">Galleria</a></li>
        <li><a class="navBtn" href="corsi.cgi">Corsi</a></li>
        <li class="active"><p>Prodotti</p></li>
        <li id="ultimo"><a class="navBtn" href="info.cgi">Info</a></li>
      </ul> 
    </div>

    <div id="corpo">
      <!-- PARTE DA GENERARE CON PERL --> 
      <div id="cont_prodotti">
FIRST

if ($ok eq "nok") {
  print "<p class=\"messaggio\">Prezzomin o Prezzomax non validi, inserisci valori interi</p>";
}
if ($ok eq "ok") {
  #current page number
  $pagina = 1;
  if (defined $cgi->param('pagina')) {$pagina = $cgi->param('pagina');}
  
  
  $totaleprod = $doc->findnodes("/prodotti/prodotto")->size(); #find all the products
  $totalepag = int (($totaleprod)/6); #find all the pages with a page made by 6 products
  $resto = ($totaleprod)%6;  #elements of the last page
  if ($resto > 0) {$totalepag = $totalepag + 1;}  #real total pages
  $from = $pagina*6 - 5; #from
  $to = $pagina*6; #to
  @prodotti = $doc->findnodes("/prodotti/prodotto[position() >= $from and position() <= $to]");
  
  if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and !defined $cgi->param('prezzomin') and !defined $cgi->param('prezzomax')) {
    $categoria = $cgi->param("categoria");
    $totaleprod = $doc->findnodes("/prodotti/prodotto[categoria = \'$categoria\']")->size();
    $totalepag = int (($totaleprod)/6);
    $resto = ($totaleprod)%6;
    if ($resto > 0) {$totalepag = $totalepag + 1;}
    $from = $pagina*6 - 5;
    $to = $pagina*6;
    @prodotti = $doc->findnodes("/prodotti/prodotto[categoria = \'$categoria\'\][position() >= $from and position() <= $to]");
  }
  if ((!defined $cgi->param('categoria') || ($cgi->param('categoria') eq "tutti")) and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
    $prezzomin = $cgi->param("prezzomin");
    $prezzomax = $cgi->param("prezzomax");
    $totaleprod = $doc->findnodes("/prodotti/prodotto[prezzo >= $prezzomin and prezzo <= $prezzomax ]")->size();
    $totalepag = int (($totaleprod)/6);
    $resto = ($totaleprod)%6;
    if ($resto > 0) { $totalepag =  $totalepag + 1;}
    $from = $pagina*6 - 5;
    $to = $pagina*6;
    @prodotti = $doc->findnodes("/prodotti/prodotto[prezzo >= $prezzomin and prezzo <= $prezzomax][position() >= $from and position() <= $to]"); 
  
  }
  
  if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
    $categoria = $cgi->param("categoria");
    $prezzomin = $cgi->param("prezzomin");
    $prezzomax = $cgi->param("prezzomax");
    $totaleprod = $doc->findnodes("/prodotti/prodotto[categoria = \'$categoria\' and prezzo >= $prezzomin and prezzo <= $prezzomax]")->size();
    $totalepag = int (($totaleprod)/6);
    $resto = ($totaleprod)%6;
    if ($resto > 0) {$totalepag =  $totalepag + 1;}
    $from = $pagina*6 - 5;
    $to = $pagina*6;
    @prodotti = $doc->findnodes("/prodotti/prodotto[categoria = \'$categoria\' and prezzo >= $prezzomin and prezzo <= $prezzomax][position() >= $from and position() <= $to]"); 
  }
  
  #print products on page
  foreach my $prodotto (@prodotti) {
        print "<div class=\"prodotto\">";
        foreach my $property ($prodotto) {
             my $titolo = $prodotto->findnodes('./titolo');
             my $img_prodotto = $prodotto->findnodes('./img_prodotto');
             my $alt  = $prodotto->findnodes('./alt');
             my $marca = $prodotto->findnodes('./marca');
             my $prezzo = $prodotto->findnodes('./prezzo');
      
             print "<p class =\"nome_p\">", encode_entities($titolo), "</p>\n";
             print "<img class=\"immagine_p\" src=\"../images/prodotti/", encode_entities($img_prodotto), "\" alt=\"$alt\" />";
             print "<p class=\"marca\">Marca: ", encode_entities($marca), "</p>\n";
             print "<p class=\"prezzo\"> Prezzo: ", encode_entities($prezzo), " euro</p>\n";
  
        }
       print "</div>";
       print "\n";
  }
  
  #pagination for $prodotti
  print "<div id=\"pagine\"><p>Pagine: "; 
  for (my $i=1; $i <= $totalepag; $i++) {
    if ((!defined $cgi->param('categoria') || ($cgi->param('categoria') eq "tutti")) and !defined $cgi->param('prezzomin') and !defined $cgi->param('prezzomax')) {
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti.cgi?pagina=$i\">$i</a> ";}
    }
    if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and !defined $cgi->param('prezzomin') and !defined $cgi->param('prezzomax')) {
      $categoria = $cgi->param("categoria");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti.cgi?pagina=$i&&categoria=$categoria\">$i</a> ";}
    }
    if ((!defined $cgi->param('categoria') || $cgi->param('categoria') eq "tutti") and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
      $prezzomin = $cgi->param("prezzomin");
      $prezzomax = $cgi->param("prezzomax");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti.cgi?pagina=$i&&prezzomin=$prezzomin&&prezzomax=$prezzomax\">$i</a> ";}
    }
    if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
      $categoria = $cgi->param("categoria");
      $prezzomin = $cgi->param("prezzomin");
      $prezzomax = $cgi->param("prezzomax");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti.cgi?pagina=$i&&categoria=$categoria&&prezzomin=$prezzomin&&prezzomax=$prezzomax\">$i</a> ";}
    }
  } 
  print "</p></div>";
}

print <<SECOND;				
	        

	      </div>
          <a class="aiuti" href="#nav">Vai alla navigazione</a>
      <a class="aiuti" href="#ricerca">Torna alla ricerca</a>
		</div>
		<div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
          <img src="http://www.w3.org/Icons/valid-xhtml10" alt=""/>
            <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
            <a id="link_admin" class="link_alter" href="login_admin.cgi">Amministrazione</a>
        <div id="diritti"><p>&copy; 2016 Gruppo <span xml:lang="en">WeGym</span></p></div>
    </div>
  </div>
</body>
</html>

SECOND

exit;