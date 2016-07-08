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
$url = "galleria_admin.cgi?sid=$sid";
print "Location: $url\n\n";

#default values for data
$titolo = "";
$alt = "";
$immagine = "";

#take non file form data
$titolo = $cgi->param('titolo');
$alt = $cgi->param('alt');
$immagine = $cgi->param('img_galleria');

#check if all input was inserted
if ($titolo eq "" || $alt eq "" || $immagine eq "") {
    $session->param("messaggio" => "Tutti i campi sono obbligatori.");
    exit;
 }
  
#check if image file valid
if (!($immagine =~ /^.*\.(jpg|jpeg|gif|JPG|png|PNG)$/)) {
    $session->param("messaggio" => "Formato immagine non riconosciuto. Utilizza solo .jpg .gif .png.");
    exit;
}

#setting connection with db
my $file = "../data/galleria.xml";
my $parser = XML::LibXML->new(); #I create parser
my $doc = $parser->parse_file($file) || die("Operazione di parsificazione fallita"); #opening file for IO
my $root = $doc->getDocumentElement || die("Non accedo alla radice");

#check if titolo already exists!
$titolo_xml = $doc->findnodes("/galleria/foto[titolo = \'$titolo\']/titolo");
if ($titolo_xml eq $titolo) {
    $session->param("messaggio" => "&Egrave; gi&agrave; presente un' immagine con lo stesso titolo.");
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
my $context = "galleria";


#image file upload
my $upload_dir = "../public_html/images";
my $upload_filehandle = $cgi->upload("img_galleria");
open ( UPLOADFILE, ">$upload_dir/$context/$img_rinominata" ) or die "$!";
binmode UPLOADFILE;
while ( <$upload_filehandle> ) {
  print UPLOADFILE;
}
close UPLOADFILE;

 
#xml format for data 
my $product = "\n\t<foto>
\t\t<titolo>$titolo</titolo>
\t\t<img_galleria>$img_rinominata</img_galleria>
\t\t<alt>$alt</alt>
\t</foto>";
 
my $father = $root->findnodes('/galleria');
my $firstnode = $father->get_node(1)->firstChild;
my $node = $parser->parse_balanced_chunk($product) || die("frammento non ben formato");
$father->get_node(1)->insertBefore($node, $firstnode);

#form data changes printed on xml (save)
open OUT, ">$file" || die("cant open file");
print OUT $doc->toString || die("cant write on file");
close(OUT) || die("cant open file");

$session->param("messaggio" => "Immagine caricata.");

exit;