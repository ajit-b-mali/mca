<?php
// Simple PHP Web Service for Calculator

if (isset($_GET['num1']) && isset($_GET['num2']) && isset($_GET['op'])) {
    $num1 = (float)$_GET['num1'];
    $num2 = (float)$_GET['num2'];
    $op = $_GET['op'];
    $result = "";

    switch ($op) {
        case 'add': $result = $num1 + $num2; break;
        case 'sub': $result = $num1 - $num2; break;
        case 'mul': $result = $num1 * $num2; break;
        case 'div': 
            $result = ($num2 != 0) ? $num1 / $num2 : "Error: Divide by zero";
            break;
        default: $result = "Invalid operation";
    }

    echo json_encode(["result" => $result]);
}
?>
