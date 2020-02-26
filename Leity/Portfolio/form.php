<?php
	if ($_SERVER['REQUEST_METHOD'] == 'POST'){
          $file = "data.json";
          if(file_exists($file))  
          {  
               $current_data = file_get_contents('data.json');  
               $array_data = json_decode($current_data, true);  
               $extra = array(  
                    'name'               =>     $_POST['name'],  
                    'email'          =>     $_POST["emailAddress"],  
                    'message'     =>     $_POST["message"]  
                    );  
               $array_data[] = $extra;  
               $final_data = json_encode($array_data);
               file_put_contents($file, $final_data);
        }
     }
?>