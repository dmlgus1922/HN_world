const fs = require('fs');
const { Configuration, OpenAIApi } = require("openai");

// api key 불러오고 적용
const apiKey = fs.readFileSync('../api_key.txt', 'utf-8');
const configuration = new Configuration({
    apiKey: apiKey
});
const openai = new OpenAIApi(configuration);

