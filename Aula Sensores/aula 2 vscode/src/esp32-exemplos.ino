#define led 25
#define botao 19


void setup() {
    Serial.begin(115200);
    pinMode(led, OUTPUT);
    pinMode(botao, INPUT_PULLUP);
}

void loop() {
    if (digitalRead(botao) == LOW){
        for(int x = 1; x < 10; x++){ 
        digitalWrite(led, HIGH);
        delay(200);
        digitalWrite(led, LOW);
        delay(200);
        }
    }
}
