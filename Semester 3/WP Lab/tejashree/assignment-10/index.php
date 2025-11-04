<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Formatter</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Text Formatter</h2>
    <form action="format.php" method="post">
        <label for="text">Enter your text:</label><br>
        <textarea name="text" id="text" rows="5" cols="40"><?php if(isset($_COOKIE['text'])) echo htmlspecialchars($_COOKIE['text']); ?></textarea><br><br>

        <label for="color">Choose text color:</label>
        <select name="color" id="color">
            <option value="black" <?php if(isset($_COOKIE['color']) && $_COOKIE['color']=='black') echo 'selected'; ?>>Black</option>
            <option value="red" <?php if(isset($_COOKIE['color']) && $_COOKIE['color']=='red') echo 'selected'; ?>>Red</option>
            <option value="blue" <?php if(isset($_COOKIE['color']) && $_COOKIE['color']=='blue') echo 'selected'; ?>>Blue</option>
            <option value="green" <?php if(isset($_COOKIE['color']) && $_COOKIE['color']=='green') echo 'selected'; ?>>Green</option>
        </select><br><br>

        <label for="font">Choose font:</label>
        <select name="font" id="font">
            <option value="Arial" <?php if(isset($_COOKIE['font']) && $_COOKIE['font']=='Arial') echo 'selected'; ?>>Arial</option>
            <option value="Times New Roman" <?php if(isset($_COOKIE['font']) && $_COOKIE['font']=='Times New Roman') echo 'selected'; ?>>Times New Roman</option>
            <option value="Courier New" <?php if(isset($_COOKIE['font']) && $_COOKIE['font']=='Courier New') echo 'selected'; ?>>Courier New</option>
            <option value="Verdana" <?php if(isset($_COOKIE['font']) && $_COOKIE['font']=='Verdana') echo 'selected'; ?>>Verdana</option>
        </select><br><br>

        <label for="size">Font size (px):</label>
        <input type="number" name="size" id="size" min="10" max="72" value="<?php echo isset($_COOKIE['size']) ? intval($_COOKIE['size']) : 16; ?>"><br><br>

        <label>Save preferences for next time?</label>
        <input type="radio" name="save" value="yes" checked> Yes
        <input type="radio" name="save" value="no"> No<br><br>

        <input type="submit" value="Format Text">
    </form>
</body>
</html>
