<!DOCTYPE html>
<html>
<head>
  <title>Text Formatter</title>
</head>
<body>
  <h2>Enter Text and Choose Preferences</h2>

  <form action="display.php" method="post">
    <textarea name="text" rows="5" cols="40" placeholder="Enter your text here..."></textarea><br><br>

    Text Color: 
    <select name="color">
      <option value="black">Black</option>
      <option value="red">Red</option>
      <option value="blue">Blue</option>
      <option value="green">Green</option>
    </select><br><br>

    Font Family:
    <select name="font">
      <option value="Arial">Arial</option>
      <option value="Verdana">Verdana</option>
      <option value="Courier New">Courier New</option>
    </select><br><br>

    Font Size:
    <select name="size">
      <option value="14px">14px</option>
      <option value="18px">18px</option>
      <option value="22px">22px</option>
    </select><br><br>

    Save preferences in cookie? 
    <input type="radio" name="save" value="yes"> Yes
    <input type="radio" name="save" value="no" checked> No<br><br>

    <input type="submit" value="Submit">
  </form>
</body>
</html>
