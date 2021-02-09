# PBA


# Requirements:
## Python 3
## Node.js
## Windows/Unix operating system

PBA can be used for very quickly making bots or sending lots of packets through proxies.
Ofc don't do anything illegal with it, only test sites with permission or sites that you own.

# How to use
import library in python,
call init function with the parameters,
WSS url (string) looks like (ws://148.392.03.28:8372)
connect packet (string) should look like (32, 543, 42, 00)
join packet (string) should look like (38, 324, 654, 240, 092)
move packet(string) you get the idea it looks like the other 2 packets...


# How to get WSS url
example image: https://imgur.com/a/wmb0u3Z

tutorial:
go to .io game in browser
open developer tools
select network tab
click WS tab
reload page
hover over result to see ws link

# How to get packets
example image: https://imgur.com/a/kUV8l2n

tutorial:
find serverbound packet logger
open dev tools
paste in console and run
and play

packet logger code:



WebSocket.prototype._send = WebSocket.prototype.send;
WebSocket.prototype.send = function(a) {
          console.log(new Uint8Array(a));
          this._send(a);
};

