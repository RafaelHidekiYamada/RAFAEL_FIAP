#define led 23
#define botao 34
#define botao2 33

void setup() {
  // vermleho positivo, preto negativo, verde sinal
  Serial.begin(115200);
  Serial.println("Hello, ESP32!");
  pinMode(led, OUTPUT);
  pinMode(botao, INPUT);
  pinMode(botao2, INPUT_PULLUP);
}

void loop() {
  if(digitalRead(botao) == LOW) {
    digitalWrite(led, HIGH);
  }
  if(digitalRead(botao2) == LOW){
    digitalWrite(led, LOW);
  }
  delay(10);
}
