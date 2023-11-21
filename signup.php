<?php
// Connect to the database
$db_host = 'localhost'; // Replace with your database host
$db_user = 'root'; // Replace with your database username
$db_password = '@Phoenix1365'; // Replace with your database password
$db_name = 'upcycledb'; // Replace with your database name

$conn = new mysqli($db_host, $db_user, $db_password, $db_name);

if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $full_name = $_POST['full_name'];
    $username = $_POST['username'];
    $birthday = $_POST['birthday'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hash the password

    // Insert data into the 'users' table
    $sql = "INSERT INTO users (full_name, username, birthday, email, password) VALUES (?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('sssss', $full_name, $username, $birthday, $email, $password);
    
    if ($stmt->execute()) {
        echo 'User registered successfully.';
    } else {
        echo 'Error: ' . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>