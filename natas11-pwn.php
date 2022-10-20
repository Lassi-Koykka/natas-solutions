<?php
    $key = "KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKL";
    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    $newdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
    $plain_text = json_encode($defaultdata);
    $plain_new_text = json_encode($newdata);
    $encrypted_text = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D");

    function xor_encrypt($in, $key) {
        $text = $in;
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
            $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }


    function loadData($def, $cookie, $key) {
        $mydata = $def;
        if(array_key_exists("data", $cookie)) {
            // base64 -> xor_encrypt -> json_decode
            $tempdata = json_decode(xor_encrypt(base64_decode($cookie["data"]), $key), true);
            echo "Data found, ";

            if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
                echo "tempdata has necessary keys, ";
                if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
                    echo "color passes regex. \nSETTING NEW VALUES\n";
                    $mydata['showpassword'] = $tempdata['showpassword'];
                    $mydata['bgcolor'] = $tempdata['bgcolor'];
                }
            }
        }
        return $mydata;
    }

    echo xor_encrypt($encrypted_text, $key);
    echo "\n";
    $encoded_new_data = base64_encode(xor_encrypt($plain_new_text, $key));
    echo $encoded_new_data;
    echo "\n";
    print_r(loadData($defaultdata, array("data"=>$encoded_new_data), $key));
?>
