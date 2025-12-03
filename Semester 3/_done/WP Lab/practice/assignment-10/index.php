<?php
// Prefill form with saved cookie preferences when available
$cookie_color = $_COOKIE['color'] ?? 'black';
$cookie_font = $_COOKIE['font'] ?? 'Arial';
$cookie_size = $_COOKIE['size'] ?? '14px';
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Text Formatter</title>
  <style>textarea { width: 400px; }</style>
</head>
<body>
  <h2>Enter Text and Choose Preferences</h2>

  <form action="display.php" method="post">
    <textarea name="text" rows="5" cols="40" placeholder="Enter your text here..."></textarea><br><br>

    Text Color: 
    <select name="color">
      <option value="black" <?php if ($cookie_color === 'black') echo 'selected'; ?>>Black</option>
      <option value="red" <?php if ($cookie_color === 'red') echo 'selected'; ?>>Red</option>
      <option value="blue" <?php if ($cookie_color === 'blue') echo 'selected'; ?>>Blue</option>
      <option value="green" <?php if ($cookie_color === 'green') echo 'selected'; ?>>Green</option>
    </select><br><br>

    Font Family:
    <select name="font">
      <option value="Arial" <?php if ($cookie_font === 'Arial') echo 'selected'; ?>>Arial</option>
      <option value="Verdana" <?php if ($cookie_font === 'Verdana') echo 'selected'; ?>>Verdana</option>
      <option value="Courier New" <?php if ($cookie_font === 'Courier New') echo 'selected'; ?>>Courier New</option>
    </select><br><br>

    Font Size:
    <select name="size">
      <option value="14px" <?php if ($cookie_size === '14px') echo 'selected'; ?>>14px</option>
      <option value="18px" <?php if ($cookie_size === '18px') echo 'selected'; ?>>18px</option>
      <option value="22px" <?php if ($cookie_size === '22px') echo 'selected'; ?>>22px</option>
    </select><br><br>

    Save preferences in cookie? 
    <input type="radio" name="save" value="yes"> Yes
    <input type="radio" name="save" value="no" checked> No<br><br>

    <input type="submit" value="Submit">
  </form>
</body>
</html>
