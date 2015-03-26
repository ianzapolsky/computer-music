var baudio = require('baudio');
var tau = 2 * Math.PI;

/*
 * 3/12 or 1/4 is a minor third
 * 4/12 or 1/3 is a major third
 * 6/12 or 1/2 is a tritone
 */

// tritone
var melody1 = [0, -1/2, 0, 1/2]
  .map(function (x) { return Math.pow(2, x) });

// tritone
var melody2 = [1/2, 0, -1/2, 0]
  .map(function (x) { return Math.pow(2, x) });

// major triad, ascending and desceding
var melody3 = [0, 4/12, 7/12, 1, 7/12, 4/12]
  .map(function (x) { return Math.pow(2, x) });

var chord = [0, 3/12, 7/12, 10/12]
  .map(function (x) { return Math.pow(2, x) });

var b = baudio(function (t) {
  
  // 2 beats per second
  var m1 = melody1[Math.floor(t * 2 % melody1.length)];
  var m2 = melody2[Math.floor(t * 2 % melody2.length)];

  // indicates 4 beats per second
  var m3 = melody3[Math.floor(t * 4 % melody3.length)];
  var m4 = melody3[Math.floor(t * 4.1 % melody3.length)];
  var m5 = melody3[Math.floor(t * 4.3 % melody3.length)];

  var arpegg = chord[Math.floor(t * 4 % chord.length)];

  // cool sound
  //return sin(400 * m3) + sin(400 * Math.pow(2, 1/2) * m4);

  return playTogether(440, sawtooth, chord)

  function playTogether(baseFreq, waveType, arr) {
    var notes = 0;
    arr.forEach(function (note) {
      notes += waveType(baseFreq * note);
    });
    return notes;
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
