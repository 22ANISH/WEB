const express = require('express');
const app = express();


// Serve static files from the "public" directory
app.use(express.static( 'public'));

// Start the server
app.listen(4000, () => {
  console.log(`Server is running at http://localhost:4000`);
});
