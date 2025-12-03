<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Formatted Text</title>
</head>
<body>
  <?php
  // Use POST values when form submitted; otherwise fall back to saved cookies or defaults.
  if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $text = $_POST['text'] ?? '';
    $color = $_POST['color'] ?? ($_COOKIE['color'] ?? 'black');
    $font = $_POST['font'] ?? ($_COOKIE['font'] ?? 'Arial');
    $size = $_POST['size'] ?? ($_COOKIE['size'] ?? '14px');
    $save = $_POST['save'] ?? 'no';

    if ($save === 'yes') {
      // Set cookies for future requests. Note: cookies set by setcookie() won't appear
      // in $_COOKIE until the browser makes the next request.
      setcookie('color', $color, time() + 3600, '/');
      setcookie('font', $font, time() + 3600, '/');
      setcookie('size', $size, time() + 3600, '/');
      echo '<p>Preferences saved for next visit.</p>';
      echo '<p><em>Note:</em> saved preferences will be applied automatically on your next visit or when the form is reloaded.</p>';
    }
  } else {
    // No form submission — use cookies or sensible defaults
    $text = '';
    $color = $_COOKIE['color'] ?? 'black';
    $font = $_COOKIE['font'] ?? 'Arial';
    $size = $_COOKIE['size'] ?? '14px';
  }
  ?>

  <h2>Formatted Output:</h2>
  <div style="color: <?php echo htmlspecialchars($color); ?>;
              font-family: <?php echo htmlspecialchars($font); ?>;
              font-size: <?php echo htmlspecialchars($size); ?>;">
    <?php echo nl2br(htmlspecialchars($text)); ?>
  </div>

  <br><a href="index.php">Go Back</a>
</body>
</html>
