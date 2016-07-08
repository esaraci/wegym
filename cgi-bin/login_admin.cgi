#! /usr/bin/perl -w

use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

$cgi = new CGI;
$errore = $cgi->url_param('errore');

print "Content-type: text/html\n\n";
print <<FIRST;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
<title>Login - WeGym</title>
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
			<p>Ti trovi in: Login</p>	
		</div>

		<div id="corpo">
FIRST

if ($errore eq 1) {
	print "<p id=\"errore\">Combinazione nome utente e <span xml:lang=\"en\">password</span> non corretta.</p>";
}

print <<SECOND;
			<div id="login">
				<form action="login.cgi" method="post">
					<fieldset>
					<legend>Amministrazione</legend>
						<label for="utente" xml:lang="en">Username:</label>
						<input class="textBox" type="text" id="utente" name="username"/>
						<label for="password" xml:lang="en">Password:</label>
						<input class="textBox" type="password" id="password" name="password"/>			
						<input type="submit" id="submit_button" value="Entra"/>
					</fieldset>
				</form>
				<p><a href="index.cgi">Torna al sito</a></p>
			</div>
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