
END
#
# morla /10111
# '$_=qw/ljttft3dvu{/,s/./print chr ord($&)-1/eg'
#
# credits for the previous level go to whoever 
# created insomnihack2016/fridginator, where i stole the idea from. 
# that was a fun challenge, Thanks! 
#

print <<end; 

END

if(param('file')){
    $f=param('file');
    if($f=~/natas/){
        print "meeeeeep!<br>";
    }
    else{
        open(FD, "$f.txt");
        print "<pre>";
        while (<fd>){
            print CGI::escapeHTML($_);
        }
        print "</fd></pre>";
    }
}

print <<end; <div="" id="viewsource">c4n Y0 h4z s4uc3?</end;></end;>
