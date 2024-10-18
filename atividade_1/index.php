<?php
$host = 'localhost';
$dbname = 'nosql';

$args = "mysql:host={$host};dbname={$dbname};charset=utf8mb4";
$user = 'root';
$password = '';

$db = new \PDO($args, $user, $password);

$sql = "SELECT * from pacientes";


$stm = $db->prepare($sql);
$stm->execute();
$dados = $stm->FetchAll(PDO::FETCH_OBJ);

    foreach ($dados as $paciente) {
        echo "<pre>";
            print_r($paciente);
        echo "</pre>";
    }
?>