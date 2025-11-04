<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Book Details Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Enter Book Details</h2>
    <form action="submit_book.php" method="post">
        <label for="book_name">Book Name:</label><br>
        <input type="text" id="book_name" name="book_name" required><br><br>

        <label for="author_name">Author Name:</label><br>
        <input type="text" id="author_name" name="author_name" required><br><br>

        <label for="publisher_name">Publisher Name:</label><br>
        <input type="text" id="publisher_name" name="publisher_name" required><br><br>

        <label for="category">Category:</label><br>
        <input type="text" id="category" name="category" required><br><br>

        <label for="synopsis">Synopsis:</label><br>
        <textarea id="synopsis" name="synopsis" rows="4" cols="40" required></textarea><br><br>

        <input type="submit" value="Submit">
        <input type="reset" value="Reset">
    </form>
</body>
</html>
