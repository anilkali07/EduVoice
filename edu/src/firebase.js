// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
export const firebaseConfig = {
    apiKey: "AIzaSyDpZi5cIGVj-WdLKn9di0itO7Rbp6y6Ido",
    authDomain: "edu-voice-e3c7c.firebaseapp.com",
    projectId: "edu-voice-e3c7c",
    storageBucket: "edu-voice-e3c7c.firebasestorage.app",
    messagingSenderId: "339930556390",
    appId: "1:339930556390:web:50e58e2a45ee9399b41827"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const auth = getAuth(app);
export const db = getFirestore(app);

export default app;
