<?php
// Connect to the database (use the same credentials as in signup.php)
$db_host = 'localhost';
$db_user = 'root';
$db_password = '@Phoenix1365';
$db_name = 'upcycledb';

$conn = new mysqli($db_host, $db_user, $db_password, $db_name);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// Process login
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Retrieve hashed password from the database
    $sql = "SELECT id, password FROM users WHERE email = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('s', $email);
    $stmt->execute();
    $stmt->bind_result($user_id, $hashed_password);
    $stmt->fetch();
    $stmt->close();

    // Verify password
    if (password_verify($password, $hashed_password)) {
        // Password is correct, set up a session and redirect to a welcome page
        session_start();
        $_SESSION['user_id'] = $user_id;
        header('Location: welcome.php'); // Redirect to a welcome page
        exit();
    } else {
        // Password is incorrect, display an error message
        echo 'Incorrect email or password.';
    }
}

$conn->close();
?>