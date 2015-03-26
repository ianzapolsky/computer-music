var baudio = require('baudio');
var tau = 2 * Math.PI;

var b = baudio(function (t) {

  var pattern = sawtooth(400) * (sin(3) + sin(4) + sin(5));
  if (t < 2) {
    return pattern + (t % (1/2) < 1/24 ? Math.random() : 0);
  } else if (t < 4) {
    return pattern + (t % (1/4) < 1/24 ? Math.random() : 0);
  } else if (t < 6) {
    return pattern + (t % (1/8) < 1/24 ? Math.random() : 0);
  } else if (t < 7) {
    return pattern + (t % (1/16) < 1/24 ? Math.random() : 0);
  } else if (t < 8) {
    return 0;
  } else {
    return sin(120 + Math.sin(1000 * (t % 1))) + (t % (1/2) < 1/24 ? Math.random() : 0);
  }



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
