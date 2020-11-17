const byte numChars = 5;
char receivedChars[numChars];

boolean newData = false;

void setup(){
    pinMode(3, OUTPUT);
    Serial.begin(500000);
    analogWrite(3, 255);
}

void loop() {
    recv();
    int inp = atoi(receivedChars);
    analogWrite(3, inp);
}

void recv() {
    static byte index = 0;
    char endMarker = 'd';
    char currentChar;

    if (Serial.available() > 0){
        currentChar = Serial.read();
        if (currentChar != endMarker){
            receivedChars[index] = currentChar;
            index++;
        }
    
    else {
        receivedChars[index] = '\0'; // terminate the string
        index = 0;
        }
    }
}

