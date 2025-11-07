<!DOCTYPE html>
<html>
<head>
  <title>Formatted Text</title>
</head>
<body>
  <?php
  $text = $_POST['text'];
  $color = $_POST['color'];
  $font = $_POST['font'];
  $size = $_POST['size'];
  $save = $_POST['save'];

  if($save == "yes") {
    setcookie("color", $color, time()+3600);
    setcookie("font", $font, time()+3600);
    setcookie("size", $size, time()+3600);
    echo "<p>Preferences saved for next visit.</p>";
  }
  ?>

  <h2>Formatted Output:</h2>
  <div style="color: <?php echo $color; ?>;
              font-family: <?php echo $font; ?>;
              font-size: <?php echo $size; ?>;">
    <?php echo nl2br(htmlspecialchars($text)); ?>
  </div>

  <br><a href="index.php">Go Back</a>
</body>
</html>
