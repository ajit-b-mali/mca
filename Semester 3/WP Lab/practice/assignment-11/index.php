<!DOCTYPE html>
<html>
<head>
  <title>Book Details Form</title>
</head>
<body>
  <h2>Enter Book Details</h2>

  <form method="post" action="">
    <label>Book Name:</label><br>
    <input type="text" name="book" required><br><br>

    <label>Author Name:</label><br>
    <input type="text" name="author" required><br><br>

    <label>Publisher Name:</label><br>
    <input type="text" name="publisher" required><br><br>

    <label>Category:</label><br>
    <input type="text" name="category" required><br><br>

    <label>Synopsis:</label><br>
    <textarea name="synopsis" rows="4" cols="40" required></textarea><br><br>

    <input type="submit" name="submit" value="Submit">
    <input type="reset" value="Reset">
  </form>

  <?php
  if(isset($_POST['submit'])) {
    $book = $_POST['book'];
    $author = $_POST['author'];
    $publisher = $_POST['publisher'];
    $category = $_POST['category'];
    $synopsis = $_POST['synopsis'];

    echo "<h3>Book Details Submitted:</h3>";
    echo "Book Name: $book<br>";
    echo "Author: $author<br>";
    echo "Publisher: $publisher<br>";
    echo "Category: $category<br>";
    echo "Synopsis: $synopsis<br>";
  }
  ?>
</body>
</html>
