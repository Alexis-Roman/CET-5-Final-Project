function redirectToLogin() {
    // Open login.html in a new tab
    window.open("Login_responsive.html", "_blank");
}

function redirectToSignup() {
    // Open SignUp.html in a new tab
    window.open("SignUp.html", "_blank");
}

// Additional function for Login_responsive.html
function redirectToSignupFromLoginResponsive() {
    // Open SignUp.html in a new tab
    window.open("SignUp.html", "_blank");
}

// New function to handle redirection from Login_responsive.html to SignUp.html
function redirectToLoginResponsiveFromSignup() {
    // Redirect to SignUp.html
    window.open("Login_responsive.html", "_blank");
}

function redirectToMaterial(materialPage) {
    // Redirect to the selected material page in the same tab
    
    window.location.href = materialPage;

    if (materialPage === 'Post_page.html') {
        // Redirect to Post_page.html in the same tab
        window.location.href = materialPage;
    }
}

// New function to handle redirection from login button to account.html
function redirectToAccount() {
    // Redirect to account.html
    window.location.href = "Account.html";
}