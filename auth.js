// auth.js

// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-analytics.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAtPlc5gKUL3bE3JJyoR15eywqzYqcMyBM",
  authDomain: "upcycle-d254a.firebaseapp.com",
  projectId: "upcycle-d254a",
  storageBucket: "upcycle-d254a.appspot.com",
  messagingSenderId: "144128623287",
  appId: "1:144128623287:web:64194a3160eb550447c332",
  measurementId: "G-M29PS6ZNN6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const auth = getAuth();

function signUp(email, password) {
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // Signed up successfully
        const user = userCredential.user;
        console.log('User signed up:', user);
      })
      .catch((error) => {
        // Handle errors
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error('Sign-up error:', errorCode, errorMessage);
      });
  }

  function logIn(email, password) {
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // Login successful
        const user = userCredential.user;
        console.log('User logged in:', user);
      })
      .catch((error) => {
        // Handle errors
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error('Login error:', errorCode, errorMessage);
      });
  }