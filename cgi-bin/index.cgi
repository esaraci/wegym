#! /usr/bin/perl
print "Content-type: text/html\n\n";
print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Home - WeGym</title>
<meta name="author" content="WeGym TW Group 15/16" />
<meta name="copyright" content="Gruppo WeGym"/>
<meta name="keywords" content="WeGym, palestra, gym, padova, homepage, cos'è wegym"/>
<meta name="description" content="WeGym - Homepage"/>
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
      <p>Ti trovi in: <span xml:lang="en">Home</span></p> 
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
        <li class="active" id="primo" xml:lang="en"><p>Home</p></li>
        <li><a class="navBtn" href="galleria.cgi">Galleria</a></li>
        <li><a class="navBtn" href="corsi.cgi">Corsi</a></li>
        <li><a class="navBtn" href="prodotti.cgi">Prodotti</a></li>
        <li id="ultimo"><a class="navBtn" href="info.cgi">Info</a></li>
      </ul> 
    </div>

    <div id="corpo">
      <h2>Cos'è <span xml:lang="en">WeGym</span></h2>
      <p><span xml:lang="en">WeGym</span> è la palestra dei tuoi sogni a Padova! Nasce nel 2016 da un gruppo di giovani ambiziosi con l'intento di soddisfare i bisogni di tutte le tipologie di clienti, oltre alla sala pesi offriamo anche una vasta scelta di corsi. Qui troverete <span xml:lang="en">personal trainer</span> altamente qualificati che vi aiuteranno a determinare l'allenamento ideale per le vostre esigenze, inoltre usufruirete delle migliori attrezzature presenti sul mercato per un'esperienza <span xml:lang="en">Top</span>. Venite a trovarci in Via Luigi Luzzatti, 4!</p>
      <img id="img_home" class="centra" src="../images/1.jpg" alt="foto degli interni della palestra" /> 
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
