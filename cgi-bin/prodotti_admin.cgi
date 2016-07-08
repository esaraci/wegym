#! /usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;
use URI::Escape;
use CGI::Session;

$cgi = new CGI;
$sid = $cgi->url_param('sid');
$session = CGI::Session->load($sid) or die "$!";

if ($session->param("logged") ne "admin") {
  $url = "index.cgi";
  print "Location: $url\n\n";
}

my $file = '../data/prodotti.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

#default or not values for categoria, prezzomin, prezzomax
$pmin = (defined $cgi->param("prezzomin"))? $cgi->param("prezzomin"): 0;
$pmax = (defined $cgi->param("prezzomax"))? $cgi->param("prezzomax"): 150;

$ok = "nok";
if ($pmin =~ /^\d+$/ && $pmax =~ /^\d+$/) { 
    $ok = "ok";
} 



print "Content-type: text/html\n\n";

print <<pippo;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Amministra Prodotti - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="WeGym Group"/>
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
			<p>Ti trovi in: Prodotti</p>	
		</div>
		
		<div class="ricerca_corsi cors_mod" id="right">
			<div class="togliere" id="login">
				<form action="logout.cgi?sid=$sid" method="post">
					<fieldset>
          <legend>Stato</legend>
						<p>Loggato come Admin</p>		
						<input type="submit" id="submit_button" value="Esci"/>
					</fieldset>
				</form>
			</div>  
			<div id="ricerca" class="cors_modifica">
        <form action="prodotti_admin.cgi?sid=$sid" method="post">
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
            <label for="prezzomin">Min. (€)</label>
            <input class="textBox prezzoTextBox" type="text" id="prezzomin" name="prezzomin" value="$pmin"/>
            <label for="prezzomax">Max. (€)</label>
            <input class="textBox prezzoTextBox" type="text" id="prezzomax" name="prezzomax" value="$pmax"/>      
            <input type="submit" id="filtra_button" value="Filtra"/>
          </fieldset>
        </form>
      </div>          
		</div>
		<div id="nav">
			<ul> 
				<li id="primo"><a class="navBtn" href="corsi_admin.cgi?sid=$sid">Corsi</a></li>
				<li><a class="navBtn" href="galleria_admin.cgi?sid=$sid">Galleria</a></li>
				<li class="active" id="ultimo"><p>Prodotti</p></li>
				<li id="amministrazioneBtn"><a class="navBtn" href="#">Esci</a></li>
			</ul>	
		</div>

		<div id="corpo">
pippo

if ($ok eq "nok") {
  print "<p class=\"messaggio\">Hai inserito dei valori non validi, inserisci valori interi positivi.</p>";
}
if ($ok eq "ok") {
  print "<p class=\"messaggio\">", $session->param("messaggio"), "</p>";
  $session->param("messaggio" => "");
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

if ($totaleprod eq 0) {
    print "<p>Nessun prodotto trovato nel database.</p>";
} else {


  #print products on page
  print "<table summary=\"Tabella contenente i prodotti presenti nel sito con il loro nome, marca e prezzo e la possibilità di eliminarli singolarmente con il tasto Elimina alla destra di ognuno di essi\">";
  print "<caption>Prodotti</caption><tbody>";
  print "<tr><th scope=\"col\">Titolo</th><th scope=\"col\">Marca</th><th scope=\"col\">Prezzo</th><th scope=\"col\">Elimina</th></tr>";
  foreach my $prodotto (@prodotti) {
        foreach my $property ($prodotto) {
             my $titolo = $prodotto->findnodes('./titolo');
             my $titolo_enc = uri_escape($titolo);
             my $img_prodotto = $prodotto->findnodes('./img_prodotto');
             my $alt  = $prodotto->findnodes('./alt');
             my $marca = $prodotto->findnodes('./marca');
             my $prezzo = $prodotto->findnodes('./prezzo');
      
             print "<tr><td scope=\"row\">$titolo</td>";
             print "<td>$marca</td>";
             print "<td>$prezzo &euro;</td>";
             print "<td><a href=\"cancella_prodotto.cgi?titolo=$titolo_enc&amp;&amp;sid=$sid\"  title=\"Elimina $titolo\">Elimina</a></td></tr>";
        }  
  }
  print "</tbody>";
  print "</table>";
  
  #pagination for $prodotti
  print "<div id=\"pagine\"><p>Pagine: "; 
  for (my $i=1; $i <= $totalepag; $i++) {
    if ((!defined $cgi->param('categoria') || ($cgi->param('categoria') eq "tutti")) and !defined $cgi->param('prezzomin') and !defined $cgi->param('prezzomax')) {
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti_admin.cgi?pagina=$i&amp;&amp;sid=$sid\">$i</a> ";}
    }
    if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and !defined $cgi->param('prezzomin') and !defined $cgi->param('prezzomax')) {
      $categoria = $cgi->param("categoria");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti_admin.cgi?pagina=$i&amp;&amp;categoria=$categoria&amp;&amp;sid=$sid\">$i</a> ";}
    }
    if ((!defined $cgi->param('categoria') || $cgi->param('categoria') eq "tutti") and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
      $prezzomin = $cgi->param("prezzomin");
      $prezzomax = $cgi->param("prezzomax");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti_admin.cgi?pagina=$i&amp;&amp;prezzomin=$prezzomin&amp;&amp;prezzomax=$prezzomax&amp;&amp;sid=$sid\">$i</a> ";}
    }
    if ((defined $cgi->param('categoria') && ($cgi->param('categoria') ne "tutti")) and defined $cgi->param('prezzomin') and defined $cgi->param('prezzomax')) {
      $categoria = $cgi->param("categoria");
      $prezzomin = $cgi->param("prezzomin");
      $prezzomax = $cgi->param("prezzomax");
      if ($pagina eq $i) {print "<span id=\"pag_sel\" class=\"pag\">$i</span> ";}
      else {print "<a class=\"pag\" href=\"prodotti_admin.cgi?pagina=$i&amp;&amp;categoria=$categoria&amp;&amp;prezzomin=$prezzomin&amp;&amp;prezzomax=$prezzomax&amp;&amp;sid=$sid\">$i</a> ";}
    }
  } 
  print "</p></div>";
}
    
}    
    
print <<SECOND;
        <form id="form_admin" action="nuovo_prodotto.cgi?sid=$sid" method="post" enctype="multipart/form-data" class="universal_form">
          	<fieldset>
			    	<legend>NUOVO PRODOTTO</legend>
				    <label for="titolo">Titolo :</label><input type="text" name="titolo" id="titolo"/>
				      
				    <label for="img_prodotto">Immagine :</label><input type="file" name="img_prodotto" id="img_prodotto"/>
				    <label for="alt">Alt :</label><textarea name="alt" id="alt" rows="1" cols="40"></textarea>
				    <label for="marca">Marca :</label><input type="text" name="marca" id="marca" />
				    <label for="prezzo">Prezzo (€) :</label><input type="text" name="prezzo" id="prezzo" />
				    <label for="categoria">Categoria :</label>
				    <select name="categoria" id="categoria">
				        <option value="guanti">Guanti</option>
				        <option value="pantaloncini">Pantaloncini</option>
				        <option value="integratori">Integratori</option>
				        <option value="tshirt">T-Shirt</option>
				        <option value="snacks">Snacks</option>
            </select>  
				    <input type="submit" value="Crea" />  
				    </fieldset>
				</form>
		</div>
		<div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
    			<img src="http://www.w3.org/Icons/valid-xhtml10" alt="" />
        		<img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
				<div id="diritti"><p>&copy; 2016 Gruppo WeGym</p></div>
		</div>
	</div>
</body>
</html>

SECOND

exit;