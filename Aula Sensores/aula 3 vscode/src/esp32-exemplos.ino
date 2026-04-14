#define botao 19
#define botao2 12
void setup() {
    Serial.begin(115200);
    pinMode(botao, INPUT_PULLUP);
    pinMode(botao2, INPUT_PULLUP);
}

void loop() {
    if (digitalRead(botao) == LOW){
        Serial.print("Alegria, Alregia, ohhhhhhhhhhh");
    }
    if (digitalRead(botao2) == LOW){
        Serial.println();
    }
    delay(150);
}