<?php
    $passwd = "11iloveyou";
    echo (int)$passwd;
    if(strstr($passwd,"iloveyou")) echo "includes I love you\n";
    if($passwd > 10) echo "long enough\n";
    if(strstr($passwd,"iloveyou") && ($passwd > 10 )){
        echo "The credentials for the next level are:";
        echo "Username: natas24 Password: <censored>";
    }
    else{
        echo "Wrong!";
    }
    // morla / 10111
?>  
