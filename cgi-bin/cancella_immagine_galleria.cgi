#! /usr/bin/perl -w
use XML::LibXML; 
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use HTML::Entities;
use CGI::Session;


$cgi = new CGI;
$sid = $cgi->param("sid");
$session = CGI::Session->load($sid) or die "$!";

if ($session->param("logged") ne "admin") {
  $url = "index.cgi";
  print "Location: $url\n\n";
  exit;
}

$url = "galleria_admin.cgi?sid=$sid";
print "Location: $url\n\n";

$titolo = $cgi->param('titolo');

$filexml_path = "../data/galleria.xml";
$parser = XML::LibXML->new();
$doc = $parser->parse_file($filexml_path);
$radice= $doc->getDocumentElement;


$immagine = $doc->findnodes("/galleria/foto[titolo = '$titolo']")->get_node(1);
$galleria = $immagine->parentNode; #the parent node of a immagine is galleria
$img = $doc->findnodes("/galleria/foto[titolo = '$titolo']/img_galleria"); #filename of img 
$galleria->removeChild($immagine);  #delete the child element of interest


#delete image
$img_path = "../public_html/images/galleria/$img";
unlink $img_path;

if(-e $img_path) 
{
    print "File still exists!";
}
else 
{
    print "File gone.";
}

#save changes (delete) on xml
open OUT, ">$filexml_path" || die("cant open file");
print OUT $doc->toString || die("cant write on file");
close(OUT) || die("cant open file");

$session->param("messaggio" => "Immagine galleria cancellata!");


exit;