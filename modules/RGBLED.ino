#define red 13;
#define green 12;
#define blue 11;

void setup() {
    pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(blue, OUTPUT);
}

void loop() {
    digitalWrite(red, HIGH);
    delay(2);
    digitalWrite(green, HIGH);
    delay(2);
    digitalWrite(blue, HIGH);
    delay(2);
    digitalWrite(red, LOW);
    delay(2);
    digitalWrite(green, LOW);
    delay(2);
    digitalWrite(blue, LOW);
}