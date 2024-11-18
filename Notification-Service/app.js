const express = require('express');
const axios = require('axios'); // Für HTTP-Anfragen
const app = express();

app.use(express.json()); // Middleware, um JSON-Anfragen zu verarbeiten

// Definiert einen API-Endpunkt /notify für POST-Anfragen
app.post('/notify', async (req, res) => {
    const userId = req.body.user_id;

    try {
        // API-Anfrage an den User Service, um Benutzerdaten zu erhalten
        const response = await axios.get(`http://user-service:5003/user/${userId}`);

        if (response.status === 200) {
            const userData = response.data;
            console.log(`Sending email to ${userData.email}: Order confirmation.`);
            res.status(200).json({ message: "Notification sent" });
        } else {
            res.status(404).json({ error: "User not found" });
        }
    } catch (error) {
        // Fehlerbehandlung bei der Anfrage an den User Service
        console.error("Error fetching user data:", error.message);
        res.status(404).json({ error: "User not found" });
    }
});

// Startet den Server auf Port 5004
app.listen(5004, () => {
    console.log("Notification Service running on port 5004");
});