#define anInput     A0                        //analog feed from MQ135
#define co2Zero     55                        //calibrated CO2 0 level
//int t = 1;  
void setup() 
{
  pinMode(anInput,INPUT);                     //MQ135 analog feed set for input
  Serial.begin(9600);                         //serial comms for debuging
}
  
void loop() 
{
  
  int co2now[10];                               //int array for co2 readings
  int co2raw = 0;                               //int for raw value of co2
  int co2ppm = 0;                               //int for calculated ppm
  int s = 0;                                  //int for averaging
                                   


  for (int i = 0; i < 10; i++)  //sample co2 10x over 2 seconds
  {                   
    co2now[i]=analogRead(A0);
    delay(200);
  }

  for (int i = 0; i < 10; i++)  //add samples together
  {                     
    s += co2now[i];  
  }
  
  co2raw = s/10;                            //divide samples by 10
  co2ppm = co2raw - co2Zero;                 //get calculated ppm
  
  
  
 
  Serial.println(co2ppm);  // prints the value read
  
 
  
  delay(20);     
      

}
