var baudio = require('baudio');
var tau = 2 * Math.PI;

var melody1 = [0, -1/2, 0, 1/2]
  .map(function (x) { return Math.pow(2, x) });

var melody3 = [0, 4/12, 7/12, 1, 7/12, 4/12]
  .map(function (x) { return Math.pow(2, x) });

var cur1 = 0;
var cur2 = 0;

var b = baudio(function (t) {

  if (Math.floor(t * 1000) % 100 == 0) {
    cur1 = Math.floor(Math.random() * melody3.length);
  }
  if (Math.floor(t * 1000) % 100 == 0) {
    cur2 = Math.floor(Math.random() * melody3.length);
  }

  return sin(400 * (t % 100) * melody3[cur1]);

  function sin (freq) {
    return Math.sin(tau * t * freq);
  }
  
  function square (freq) {
    return Math.sin(tau * t * freq) < 0 ? -1 : 1;
  }

  function sawtooth (freq) {
    return t % (1 / freq) * freq * 2 - 1;
  }

});

b.play();
