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
$url = "corsi_admin.cgi?sid=$sid";
print "Location: $url\n\n";

$titolo = $cgi->param('titolo');

$filexml_path = '../data/corsi.xml';
$parser = XML::LibXML->new();
$doc = $parser->parse_file($filexml_path);
$radice= $doc->getDocumentElement;


$corso = $doc->findnodes("/corsi/corso[titolo = '$titolo']")->get_node(1);
$corsi = $corso->parentNode; #the parent node of a corso is corsi
$img = $doc->findnodes("/corsi/corso[titolo = '$titolo']/img_corso"); #filename of img 
$corsi->removeChild($corso);  #delete the child element of interest


#delete image
$path_img = "../public_html/images/corsi/$img";
unlink $path_img;

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

$session->param("messaggio" => "Corso cancellato.");


exit;