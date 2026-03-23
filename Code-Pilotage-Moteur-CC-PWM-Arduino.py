#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x20, 16, 2); // Adresse I2C : 0x20 ou 0x27

int brochePot = A0;      // Entrée analogique
int brocheMoteur = 9;    // Sortie PWM (notée ~ sur Arduino)

int valeurCAN = 0;       // De 0 à 1023
int valeurPWM = 0;       // De 0 à 255
float tension = 0.0;
int pourcentage = 0;

void setup() {
  Serial.begin(9600);
  pinMode(brocheMoteur, OUTPUT);
  lcd.init();
  lcd.backlight();
  lcd.print("Systeme PWM OK");
  delay(1000);
  lcd.clear();
}

void loop() {
  valeurCAN = analogRead(brochePot);            // Lecture tension potentiomètre
  valeurPWM = map(valeurCAN, 0, 1023, 0, 255);  // Conversion pour analogWrite
  tension = valeurCAN * 5.0 / 1023.0;           // Calcul de la tension réelle
  pourcentage = map(valeurCAN, 0, 1023, 0, 100); // Pourcentage de vitesse

  analogWrite(brocheMoteur, valeurPWM);         // Génération du signal PWM

  // Affichage LCD
  lcd.setCursor(0, 0); lcd.print("CAN: "); lcd.print(valeurCAN);
  lcd.setCursor(0, 1); lcd.print("Vitesse: "); lcd.print(pourcentage); lcd.print("%");

  delay(200);
}