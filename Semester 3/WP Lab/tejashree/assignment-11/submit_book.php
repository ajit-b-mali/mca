<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $book_name = isset($_POST['book_name']) ? htmlspecialchars($_POST['book_name']) : '';
    $author_name = isset($_POST['author_name']) ? htmlspecialchars($_POST['author_name']) : '';
    $publisher_name = isset($_POST['publisher_name']) ? htmlspecialchars($_POST['publisher_name']) : '';
    $category = isset($_POST['category']) ? htmlspecialchars($_POST['category']) : '';
    $synopsis = isset($_POST['synopsis']) ? htmlspecialchars($_POST['synopsis']) : '';
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
    <title>Book Details Submitted</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Book Details Submitted</h2>
    <ul>
        <li><strong>Book Name:</strong> <?php echo $book_name; ?></li>
        <li><strong>Author Name:</strong> <?php echo $author_name; ?></li>
        <li><strong>Publisher Name:</strong> <?php echo $publisher_name; ?></li>
        <li><strong>Category:</strong> <?php echo $category; ?></li>
        <li><strong>Synopsis:</strong> <?php echo nl2br($synopsis); ?></li>
    </ul>
    <a href="index.php">Back to form</a>
</body>
</html>
