const express = require('express');
const app = express();
const router = express.Router();


app.get('/', (req, res) => {
    
})

app.get('http://codingtest.brique.kr:8080/random', (req, res) => {
    console.log(req)
})


// app.use(express.json());
// app.use(express.urlencoded());

// app.use(router);

app.listen(3000);