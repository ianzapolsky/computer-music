var mu = require('./music-util');

var melody1 = [1, 11/12];
var melody2 = [1, 10/12];
var melody3 = [1, 9/12];
var melodies = [melody1, melody2, melody3, melody2];

var song = function() {
  var music = 0;
  music += mu.playBeat(4);
  music += mu.playMelody(mu.majorArpeggio, 'sin', 400, 2);
  music += mu.playPattern(melodies);
  return music;
}

mu.play(song);
