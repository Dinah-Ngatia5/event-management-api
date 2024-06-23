console.log("Starting server...")

const express = require('express');
const cors = require('cors');
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Allow requests from http://127.0.0.1:5173
app.use(cors({
    origin: 'http://127.0.0.1:5173',
    credentials: true // if you are using cookies or session
}));

// Example root route
app.get('/', (req, res) => {
    res.send('Welcome to the API!');
});

// Example route for profile
app.get('/profile', (req, res) => {
    // Your logic to get user profile
    res.json({ user: { username: 'exampleUser' } });
});

// Example route for logout
app.get('/logout', (req, res) => {
    // Your logic to handle logout
    res.json({ message: 'Logged out successfully' });
});

// Start the server
const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
