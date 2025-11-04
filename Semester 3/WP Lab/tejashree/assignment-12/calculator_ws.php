<?php
// Set the content type of the response to be JSON
header('Content-Type: application/json');

// Initialize the response array
$response = ['error' => false, 'result' => 0, 'message' => ''];

// Check if the required POST variables are set
if (isset($_POST['num1'], $_POST['num2'], $_POST['operation'])) {

    // Get the numbers and operation from the POST request
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $operation = $_POST['operation'];

    // --- Input Validation ---
    // Check if the inputs are numeric
    if (!is_numeric($num1) || !is_numeric($num2)) {
        $response['error'] = true;
        $response['message'] = 'Error: Both inputs must be valid numbers.';
    } else {
        // Convert inputs to floating-point numbers for calculation
        $num1 = floatval($num1);
        $num2 = floatval($num2);

        // --- Perform Calculation based on the operation ---
        switch ($operation) {
            case 'add':
                $response['result'] = $num1 + $num2;
                break;
            case 'subtract':
                $response['result'] = $num1 - $num2;
                break;
            case 'multiply':
                $response['result'] = $num1 * $num2;
                break;
            case 'divide':
                // Check for division by zero
                if ($num2 == 0) {
                    $response['error'] = true;
                    $response['message'] = 'Error: Cannot divide by zero.';
                } else {
                    $response['result'] = $num1 / $num2;
                }
                break;
            default:
                $response['error'] = true;
                $response['message'] = 'Error: Invalid operation specified.';
                break;
        }
    }
} else {
    // If required parameters are missing
    $response['error'] = true;
    $response['message'] = 'Error: Missing required parameters (num1, num2, operation).';
}

// --- Send Response ---
// Encode the response array into a JSON string and output it
echo json_encode($response);

?>
