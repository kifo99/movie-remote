#include <Arduino.h>
#include <IRremote.h>

const int RECV_PIN = 11;

void setup() {
  Serial.begin(9600);

  IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK);
  Serial.println("IR receiver ready. Press the button on remote");

}

void loop() {
     if (IrReceiver.decode()) {
    unsigned long code = IrReceiver.decodedIRData.decodedRawData;
    
    if (code != 0x0) {
      Serial.print("IR Code: 0x");
      Serial.println(code, HEX);
    }
    
    IrReceiver.resume();
  }
}