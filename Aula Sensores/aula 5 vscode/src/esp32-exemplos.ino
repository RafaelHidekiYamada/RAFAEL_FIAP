#define led1 23
#define led2 22
#define led3 21
#define led4 19

#define bot1 18
#define bot2 5
#define bot3 17
#define bot4 16

#define buzzer 4

void setup() {
    Serial.begin(115200);
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);

    pinMode(bot1, INPUT_PULLUP);
    pinMode(bot2, INPUT_PULLUP);
    pinMode(bot3, INPUT_PULLUP);
    pinMode(bot4, INPUT_PULLUP);

    ledcSetup(0, 1000, 8);
    ledcAttachPin(buzzer, 0);
}

void loop() {
    int melody[] = {
    440, 440, 440, 349, 523, 440, 349, 523, 440,
    659, 659, 659, 698, 523, 784, 740, 698, 659
  };
  int tempo[] = 
  {
    500, 500, 500, 350, 150, 500, 350, 150, 1000,
    500, 500, 500, 350, 150, 500, 350, 150, 1000
  };
  for (int i = 0; i < sizeof(melody) / sizeof(melody[0]); i++) 
  {
    ledcWrite(0, melody[i]);
    delay(tempo[i] * 1.30); // Pequeno delay para espaçar as notas
    ledcWrite(0, 0); // Desliga o buzzer ao final de cada nota
    delay(50); // Pequeno delay para evitar cliques entre as notas
  }

}
