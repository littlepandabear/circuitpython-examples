/*************************************************** 
  This is an example for the Adafruit VS1053 Codec Breakout

  Designed specifically to work with the Adafruit VS1053 Codec Breakout 
  ----> https://www.adafruit.com/products/1381

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

// include SPI, MP3 and SD libraries
#include <SPI.h>
#include <Adafruit_VS1053.h>
#include <SD.h>

// These are the pins used for the music maker shield
#define SHIELD_RESET  -1      // VS1053 reset pin (unused!)
#define SHIELD_CS     7      // VS1053 chip select pin (output)
#define SHIELD_DCS    6      // VS1053 Data/command select pin (output)

// These are common pins between breakout and shield
#define CARDCS 4     // Card chip select pin
// DREQ should be an Int pin, see http://arduino.cc/en/Reference/attachInterrupt
#define DREQ 3       // VS1053 Data request, ideally an Interrupt pin

 // create shield-example object!
Adafruit_VS1053_FilePlayer musicPlayer = Adafruit_VS1053_FilePlayer(SHIELD_RESET, SHIELD_CS, SHIELD_DCS, DREQ, CARDCS);

const int buttonPin = 5; 
int buttonState;
int currTrack = 0;
int lastTrack = -1; // set as 0 if you dont want it to play on startup
boolean isPlaying = false;

char *tracks[] = {"track001.mp3", "track002.mp3"}; //tracks array

int tracksLength = sizeof(tracks)/sizeof(char *); //finds number of tracks

 
void setup() {
  Serial.begin(9600);
  Serial.println(tracksLength);

  Serial.println("Adafruit VS1053 Simple Test");

  if (! musicPlayer.begin()) { // initialise the music player
     Serial.println(F("Couldn't find VS1053, do you have the right pins defined?"));
     while (1);
  }
  Serial.println(F("VS1053 found"));
  
   if (!SD.begin(CARDCS)) {
    Serial.println(F("SD failed, or not present"));
    while (1);  // don't do anything more
  }

  
  // Set volume for left, right channels. lower numbers == louder volume!
  musicPlayer.setVolume(20,20);


  // If DREQ is on an interrupt pin (on uno, #2 or #3) we can do background
  // audio playing
  musicPlayer.useInterrupt(VS1053_FILEPLAYER_PIN_INT);  // DREQ int
  

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);


}

void loop() {
  buttonState = digitalRead(buttonPin);
  //if button pressed increment currTrack
  if (buttonState == HIGH) {
      delay(1000);//delay for long press
      currTrack++;
      //if passes length, return to 0
      if (currTrack >= tracksLength){
          currTrack = 0;
      }
  }
  
  if (currTrack != lastTrack ){
      //play track
      musicPlayer.startPlayingFile(tracks[currTrack]);
      //set last track
      lastTrack = currTrack;

      isPlaying = true;
  }
  
  
  delay(100);
  
}
