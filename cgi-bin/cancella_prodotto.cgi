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
$url = "prodotti_admin.cgi?sid=$sid";
print "Location: $url\n\n";

$titolo = $cgi->param('titolo');

$filexml_path = '../data/prodotti.xml';
$parser = XML::LibXML->new();
$doc = $parser->parse_file($filexml_path);
$radice= $doc->getDocumentElement;


$prodotto = $doc->findnodes("/prodotti/prodotto[titolo = '$titolo']")->get_node(1);
$prodotti = $prodotto->parentNode; #the parent node of a prodotto is prodotti
$img = $doc->findnodes("/prodotti/prodotto[titolo = '$titolo']/img_prodotto"); #filename of img 
$prodotti->removeChild($prodotto);  #delete the child element of interest


#delete image
$path_img = "../public_html/images/prodotti/$img";
unlink($path_img);

if(-e $path_img) 
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

$session->param("messaggio" => "Prodotto cancellato!");

exit;