#include <PRIZM.h>
PRIZM prizm; 

float cmd;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  prizm.PrizmBegin();
  prizm.setMotorInvert(1,1); 
}

void loop() {

}

void serialEvent(){
  if(Serial.read() == '$')
  {
    String data = Serial.readStringUntil('\n');

    int first = data.indexOf(",");
    int length = data.length();

    String vel = data.substring(0, first); 
    String ang = data.substring(first+1,length);

    float vel_1 = vel.toFloat();
    float vel_2 = ang.toFloat();

    if(vel_1 ==1000){
        prizm.setMotorSpeeds(-10,10);
        delay(10);
    }

    if(vel_1 ==2000){
        prizm.setMotorSpeeds(125,125);
    }

    prizm.setMotorSpeeds(vel_1,vel_2);

    
    Serial.print(prizm.readEncoderCount(1));
    Serial.print(",");
    Serial.println(prizm.readEncoderCount(2));
    
     
  }
  else
  {
    Serial.println(-1);
  }

}
