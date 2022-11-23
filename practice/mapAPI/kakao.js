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
    const naviUrl = 'http://map.kakao.com/?sName=' + start + '&eName=' + end;
    // const naviUrl = 'http://map.kakao.com/?sName=서울 강남구1&eName=광주서구내방로241번길10';
    console.log(naviUrl)
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
        const $ = cheerio.load(html.data);
        
        // const data = JSON.stringify(html[0]);
        // const carTime = data.text();
        console.log(html)
        
        // res.render('test4', {
        //     test: html
        // })
        
        console.log(carTime);
        res.render('test3', {
            start: start,
            end: end,
            minute: carTime
        });

        // const busTime = $('.TransitRouteItem > .time')

        // console.log(carTime);
    });

    
});
router.get('/test4', (req, res) => {
    res.render('test4', {
        test:'<h1>hi</h1>'
    })
})

router.get('/test5', (req, res) => {
    res.render('test5')
})

app.use(router);
app.listen(3001);