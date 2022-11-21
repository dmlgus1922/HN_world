const express = require('express');
const app = express();
const router = express.Router();

const axios = require('axios');
const cheerio = require('cheerio');

app.set('view engine', 'ejs');

router.get('/', (req, res) => {
    res.render('test');
});

router.get('/test2', (req,res) => {
    res.render('test2');
});

router.get('/test3', (req,res) => {
    res.render('test3', {
        start: '',
        end: '',
        minute: ''
    });
});

router.get('/toNavi', (req, res) => {
    const start = req.query.start;
    const end = '광주 서구 내방로 241번길 10';
    const naviUrl = 'https://map.kakao.com/?sName=' + start + '&eName=' + end;

    // res.redirect(naviUrl);

    const getHtml = async () => {
        try {
            return await axios.get(naviUrl);
        } catch (err) {
            console.error(err);
        }
    }

    getHtml()
    .then((html) => {
        // console.log("start 1");
        // console.log(html.data);
        // console.log("end 1");
        const $ = cheerio.load(html.data);
        const data = $("#info\\.flagsearch > div.CarRouteResultView > ul > li > div.summary > div > div.contents > p > span.time > span.num");
        console.log("start 2");
        console.log(data);
        console.log("end 2");
        const carTime = data.text();
        console.log("start 3");
        console.log(carTime);
        console.log("end 3");
        // console.log(carTime);
        // console.log("start 2");
        // console.log(data);
        // console.log("end 2");
        // console.log(carTime);
        // res.render('test3', {
        //     start: start,
        //     end: end,
        //     minute: carTime
        // });

        // const busTime = $('.TransitRouteItem > .time')

        // console.log(carTime);
    });

    
});

app.use(router);
app.listen(3000);