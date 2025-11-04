<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $text = isset($_POST['text']) ? $_POST['text'] : '';
    $color = isset($_POST['color']) ? $_POST['color'] : 'black';
    $font = isset($_POST['font']) ? $_POST['font'] : 'Arial';
    $size = isset($_POST['size']) ? intval($_POST['size']) : 16;
    $save = isset($_POST['save']) ? $_POST['save'] : 'no';

    if ($save === 'yes') {
        setcookie('text', $text, time() + 60*60*24*30); // 30 days
        setcookie('color', $color, time() + 60*60*24*30);
        setcookie('font', $font, time() + 60*60*24*30);
        setcookie('size', $size, time() + 60*60*24*30);
    } else {
        setcookie('text', '', time() - 3600);
        setcookie('color', '', time() - 3600);
        setcookie('font', '', time() - 3600);
        setcookie('size', '', time() - 3600);
    }
} else {
    // Redirect to form if accessed directly
    header('Location: index.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Formatted Text</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Your Formatted Text</h2>
    <div class="formatted-box" style="color: <?php echo htmlspecialchars($color); ?>; font-family: <?php echo htmlspecialchars($font); ?>; font-size: <?php echo intval($size); ?>px;">
        <?php echo nl2br(htmlspecialchars($text)); ?>
    </div>
    <br>
    <a href="index.php">Back to form</a>
</body>
</html>
