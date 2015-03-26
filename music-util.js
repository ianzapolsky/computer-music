var baudio = require('baudio');
var TAU = 2 * Math.PI;

var musicUtil = {

  /**
   * t is time, tonic is the root freqency relative to which other pitches are 
   * built.
   */
  t: null,

  tonic: null,

  /**
   * MAIN CALLBACK
   */
  play: function(song) {
    var _this = this;
    var b = baudio(function (t) {
      _this.setTime(t);
      return song();
    });
    b.play();
  },

  /**
   * BUILT-IN NOTE RELATIONSHIPS
   */
  majorTriad: [0, 4/12, 7/12].map(function (x) { return Math.pow(2, x) }),

  majorArpeggio: [0, 4/12, 7/12, 1, 7/12, 4/12].map(function (x) { return Math.pow(2, x) }),

  minorTriad: [0, 3/12, 7/12].map(function (x) { return Math.pow(2, x) }),

  minorArpeggio: [0, 3/12, 7/12, 1, 7/12, 3/12].map(function (x) { return Math.pow(2, x) }),

  /**
   * METHODS OF PLAYING ARRAYS OF NOTES
   */
  playMelody: function(notes, wave, freq, notesPerSec) {
    switch(wave) {
      case 'sin': return this.sin(freq * notes[Math.floor(this.t * notesPerSec % notes.length)]);
      case 'square': return this.square(freq * notes[Math.floor(this.t * notesPerSec % notes.length)]);
      case 'sawtooth': return this.sawtooth(freq * notes[Math.floor(this.t * notesPerSec % notes.length)]);
    }
  },

  playChord: function(notes, wave, freq) {
    var _this = this;
    var music = 0;
    notes.forEach(function (note) {
      switch (wave) {
        case 'sin': music += _this.sin(freq * note);
        case 'square': music += _this.square(freq * note);
        case 'sawtooth': music += _this.sawtooth(freq * note);
      }
    });
    return music;
  },

  ascendingChord: function(notes, freq, ascendingFactor) {
    var _this = this;
    var notes = 0;
    notes.forEach(function (note) {
      notes += _this.sin(freq * note * (_this.t / ascendingFactor));
    });
    return notes;
  },

  playPattern: function(melodies) {
    var index = Math.floor(this.t % melodies.length);
    return this.playMelody(melodies[index], 'sawtooth', 400, 8);
  },

  /**
   * PRECUSSION
   */
  playBeat: function(beatsPerSecond) {
    return this.t % (1 / beatsPerSecond) < 1/24 ? Math.random() : 0
  },

  /**
   * SETTERS FOR TIME AND TONIC VARIABLES
   */
  setTime: function (t) {
    this.t = t;
  },

  setTonic: function (freq) {
    this.tonic = freq;
  },
  
  /**
   * DIFFERENT KINDS OF SOUND WAVES
   */
  sin: function (freq) {
    return Math.sin(TAU * this.t * freq);
  },

  square: function (freq) {
    return Math.sin(TAU * this.t * freq) < 0 ? -1 : 1;
  },
  
  sawtooth: function (freq) {
    return this.t % (1 / freq) * freq * 2 - 1;
  }

};

module.exports = musicUtil;
