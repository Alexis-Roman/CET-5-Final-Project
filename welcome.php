<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['user_id'])) {
    header('Location: login.html'); // Redirect to the login page if not logged in
    exit();
}

// Display a welcome message or other content
echo 'Welcome to Upcycle!';

// You can also include a logout button or other user-specific content here
?>