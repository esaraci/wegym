#! /usr/bin/perl -w
use XML::LibXML; 
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;
use CGI::Session;


#load CGi
$cgi = new CGI;
#load session
$sid = $cgi->url_param('sid');
$session = CGI::Session->load($sid) or die "$!";
$url = "corsi_admin.cgi?sid=$sid";
print "Location: $url\n\n";

#default values for data
$titolo = "";
$alt = "";
$descrizione = "";
$immagine = "";

#take non file form data
$titolo = $cgi->param('titolo');
$alt = $cgi->param('alt');
$descrizione = $cgi->param('descrizione');
$immagine = $cgi->param('img_corso');

#check if all input was inserted
if ($titolo eq "" || $alt eq "" || $immagine eq "" || $descrizione eq "") {
    $session->param("messaggio" => "Tutti i campi sono obbligatori.");
    exit;
 }
  
#check if image file valid
if (!($immagine =~ /^.*\.(jpg|jpeg|gif|JPG|png|PNG)$/)) {
    $session->param("messaggio" => "Formato immagine non riconosciuto. Utilizza solo .jpg .gif .png.");
    exit;
}

#setting connection with db
my $file = "../data/corsi.xml";
my $parser = XML::LibXML->new(); #I create parser
my $doc = $parser->parse_file($file) || die("Operazione di parsificazione fallita"); #opening file for IO
my $root = $doc->getDocumentElement || die("Non accedo alla radice");

#check if titolo already exists!
$titolo_xml = $doc->findnodes("/corsi/corso[titolo = \'$titolo\']/titolo");
if ($titolo_xml eq $titolo) {
    $session->param("messaggio" => "&Egrave; gi&agrave; presente un corso con lo stesso titolo.");
    exit;
}

#pull out the extension of $immagine with regular expressions
my ($ext) = $immagine =~ /(\.[^.]+)$/;

#generate random 8 char string and append $ext to it
my @chars = ("A".."Z", "a".."z");
my $img_rinominata;
$img_rinominata .= $chars[rand @chars] for 1..8;
$img_rinominata .= $ext;

#defining context
my $context = "corsi";

#image file upload
my $upload_dir = "../public_html/images";
my $upload_filehandle = $cgi->upload("img_corso");
open ( UPLOADFILE, ">$upload_dir/$context/$img_rinominata" ) or die "$!";
binmode UPLOADFILE;
while ( <$upload_filehandle> ) {
  print UPLOADFILE;
}
close UPLOADFILE;
 
#xml format for data 
my $product = "\n\t<corso>
\t\t<titolo>$titolo</titolo>
\t\t<alt>$alt</alt>
\t\t<img_corso>$img_rinominata</img_corso>
\t\t<descrizione>$descrizione</descrizione>
\t</corso>";
 
my $father = $root->findnodes('/corsi');
my $firstnode = $father->get_node(1)->firstChild;
my $node = $parser->parse_balanced_chunk($product) || die("frammento non ben formato");
$father->get_node(1)->insertBefore($node, $firstnode);

#form data upload on xml
open OUT, ">$file" || die("cant open file");
print OUT $doc->toString || die("cant write on file");
close(OUT) || die("cant open file");

$session->param("messaggio" => "Corso aggiunto.");

exit;