var baudio = require('baudio'); 
var musicUtil = require('./music-util');

var arpeggio = [0, 4/12, 7/12, 1, 7/12, 4/12]
  .map(function (x) { return Math.pow(2, x) });

var chord = [0, 3/12, 7/12, 1, 10/12]
  .map(function (x) { return Math.pow(2, x) });

var dreezy1 = [1/12, 5/12, 10/12]
  .map(function (x) { return Math.pow(2, x) });

var dreezyX = [1/12, 5/12, 1]
  .map(function (x) { return Math.pow(2, x) });

var dreezy2 = [0, 5/12, 10/12]
  .map(function (x) { return Math.pow(2, x) });

var dreezy3 = [0, 5/12, 8/12]
  .map(function (x) { return Math.pow(2, x) });

var bass = [-14/12, -14/12, -11/12, -12/12]
  .map(function (x) { return Math.pow(2, x) });


var b = baudio(function (t) {

  musicUtil.setTime(t);
  
  var music = 0;

  var melody = musicUtil.majorArpeggio.concat(musicUtil.minorArpeggio);

  var loop = dreezy1.concat(dreezy1).concat(dreezy1).concat(dreezy1).concat(dreezy1).concat(dreezy1).concat(dreezy1).concat(dreezyX).concat(dreezy2).concat(dreezy2).concat(dreezy2).concat(dreezy3).concat(dreezy3).concat(dreezy3).concat(dreezy3).concat(dreezy3);

  //music += musicUtil.playBeat(8);
  //music += musicUtil.playMelody('square', 300, 12, loop);
  //music += musicUtil.playMelody('sawtooth', 400, 1, bass);

  music += musicUtil.ascendingChord(440, 3, chord);

  return music;

});

setInterval(function () {
  b.play();
}, 1000);




