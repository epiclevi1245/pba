
var ws = require('ws');
var url = require('url');
var fs = require('fs');

console.log("NODE.JS started, reading data files...")

var proxyAgent = require('https-proxy-agent');
var proxies = fs.readFileSync('proxies.txt', 'utf-8').split('\r\n');
var ip = fs.readFileSync('ip.txt', 'utf-8');
var jp = fs.readFileSync('jp.txt', 'utf-8').split('\n');
var mp = fs.readFileSync('mp.txt', 'utf-8').split('\n');
var cp = fs.readFileSync('cp.txt', 'utf-8').split('\n');


var proxyPos = 0;
var botCount = 0;



console.log("NODE.JS read data files, starting script...")



var ws = require('ws');
const { error } = require('console');
var botCount = 0;

//this is the main function
function index() {
    var originProxy = {
        origin: 'http://google.com',
    };
    //makes the ws
    var bot = new ws(ip, originProxy)
    bot.onopen = function () {
        //connects the bot
        bot.send(new Uint8Array(cp))
        bot.send(new Uint8Array(jp))
        bot.send(new Uint8Array(mp))
        botCount++
    }
    bot.on('error', () => { })
} setInterval(index, 0);
process.on('uncaughtException', () => {})







