/* Define all common variables
*/
// === IBM Design Language colors, See https://www.ibm.com/design/language/resources/swatchbook ====
var cyan = "151,187,205";
var green = "75,132,0";
var yellow = "253,214,0";
var gray = "174,174,174";
var blue = "21,41,53";

// === Minion's places ===
var minion = "Finnie's Nerdy Palace";
var minionGirl = "IBM Böblingen Lab";
var minionOneEye = "Kai's Kingdom";
var minionDuck = "Pradeep's Castle";

//=== GPS position ==== 
var minionPos = {"lat":48.688725, "lng": 8.995648};
var minionGirlPos = {"lat":48.6660732, "lng": 9.0388024};
var minionOneEyePos = {"lat":48.7684932, "lng": 9.153817};
var minionDuckPos = {"lat":48.66542,"lng": 8.9891824};
var minionPurplePos = {"lat":48.755777, "lng": 8.882709};

//=== Dialogs ===
var minionDialog = "Save me!!";
var minionGirlDialog = "I'm a nerd...";
var minionOneEyeDialog = "I have a monocle.";
var minionDuckDialog = "I have a duck inner tube.";

//=== SMS service ===
var minionNumber = '--the number you want to text--';
var minionGirlNumber = '--the number you want to text--';
var minionOneEyeNumber = '--the number you want to text--';
var minionDuckNumber = '--the number you want to text--';

var SMSData = {
  fromNumber: '--your twilio number--',
  message: '',
  targetNumber: [minionNumber, minionGirlNumber, minionOneEyeNumber, minionDuckNumber]
};

//== for quake service ==
var minionQuakeIndex = 0;
var minionGirlQuakeIndex = 1;
var minionOneEyeQuakeIndex = 2;
var minionDuckQuakeIndex = 3;

var numQuakeDetectors = 3;
var quakeMagnitude = [0,0,0];


var numQuakeDetectors = 4;
var numTemperatureDetectors = 4;
var numHumitureDetector = 4;
var numRaindropDetector = 4;

var quakeMagnitude = [0,0,0,0];
var temperatureReadings = [0,0,0,0];
var humidReadings = [0,0,0,0];
