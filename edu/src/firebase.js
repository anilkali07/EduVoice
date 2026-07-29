// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
export const firebaseConfig = {
    apiKey: "AIzaSyB7gjZwqSUamP2ZQcUt0GA63w7OSU_1PnU",
    authDomain: "eduvoice-a653a.firebaseapp.com",
    projectId: "eduvoice-a653a",
    storageBucket: "eduvoice-a653a.firebasestorage.app",
    messagingSenderId: "1091779646636",
    appId: "1:1091779646636:web:5586024b63f1694e697b09",
    measurementId: "G-ZD3VF748TK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const auth = getAuth(app);
export const db = getFirestore(app);

export default app;
