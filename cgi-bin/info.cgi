#! /usr/bin/perl -w
print "Content-type: text/html\n\n";
print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Info - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta name="keywords" content="WeGym, palestra, gym, padova, info, contatto, dove siamo, contattaci, orario"/>
<meta name="description" content="WeGym - Info"/>
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
			<p>Ti trovi in: <a class="link_alter" href="index.cgi" xml:lang="en">Home</a> &gt; Info</p>
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
				<li><a class="navBtn" href="corsi.cgi">Corsi</a></li>
				<li><a class="navBtn" href="prodotti.cgi">Prodotti</a></li>
				<li class="active" id="ultimo"><p>Info</p></li>
			</ul>	
		</div>

		<div id="corpo">
			<h2 class="informazioni">Dove Siamo</h2>
			<p class="informazioni_p"><span xml:lang="en">WeGym</span> si trova in Via Luigi Luzzatti, 4 a Padova. </p>
			<img id="mappa" src="../images/map.jpg" alt="mappa della nostra palestra" />	
			<h2 class="informazioni">Orario</h2>
			<p class="informazioni_p">Sala Pesi: <abbr title="lunedì">lun</abbr>-<abbr title="venerdì">ven</abbr> 9:30 - 21:30 / <abbr title="sabato">sab</abbr>-<abbr title="domenica">dom</abbr> 9:30 - 13:00</p>
			<p class="informazioni_p">Zumba: <abbr title="lunedì">lun</abbr> 18:30 - 20:30 / <abbr title="mercoledì">mer</abbr> 18:30 - 20:30 / <abbr title="venerdì">ven</abbr> 18:30 - 20:30</p>
			<p class="informazioni_p">Salsa: <abbr title="martedì">mar</abbr> 21:30 - 23:30 / <abbr title="giovedì">gio</abbr> 21:30 - 23:30</p>
			<p class="informazioni_p"><abbr title="Mixed Martial Arts" xml:lang="en">MMA</abbr>: <abbr title="lunedì">lun</abbr> - <abbr title="giovedì">gio</abbr> 15:00 - 21:00</p>
			<p class="informazioni_p"><span xml:lang="fr">Boxe</span>: <abbr title="martedì">mar</abbr> - <abbr title="venerdì">ven</abbr> 16:00 - 23:00</p>
			<h2 class="informazioni">Contattaci</h2>
			<p class="informazioni_p">Se hai bisogno di ulteriori informazioni sentiti libero di contattarci al seguente indirizzo <span xml:lang="en"> e-mail</span>: supporto[at]wegym[dot]it oppure chiamaci al 0499040214.</p>
			<a class="aiuti" href="#nav">Vai alla navigazione</a>
			
		</div>
		<div id="footer"> <!-- bisogna togliere lo style dall'immagine -->
    			<img src="http://www.w3.org/Icons/valid-xhtml10" alt="" />
        		<img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="" />
        		<a id="link_admin" class="link_alter" href="login_admin.cgi">Amministrazione</a>
				<div id="diritti"><p>&copy; 2016 Gruppo <span xml:lang="en">WeGym</span></p></div>
		</div>
	</div>
</body>
</html>

FIRST
exit;