#include <stdio.h>
#include <stdlib.h>

    float error_1 = 0.21;
    float error_2 = 0.08;
    float first_fused_arr[10];
    float second_fused_arr[10];
    float y =0;
    float P = 1.0;


    float rad = 46 *3.14/180;
    float time;
    float mpuacc = 0.92;
    float bnoacc= 0.79;

float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
float bno55[10] = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};


// Failed to use Kalman's Filter , I've been trying to understand it for two days now...
//



//float KalmanFilter(float mpu, float bno ){
//
//
//
//float P2 = P;
//float y2 = y;
//
//    float K = P2 / (P2 + bno);
//    y = y2 + K * (mpu - y2);
//    P = (1 - K) * P2;
//
//}


int main()
{
//printf("first fused array is:");
//    for (int i=0; i<10; i++){
//    first_fused_arr[i]= KalmanFilter(mpu6050[i],error_1);
//    printf("  %.2f", first_fused_arr[i]);
//
//
  float arr[10];
 printf("Fused Array: {");
  for (int i=0; i<10; i++){

//        Theory: y= Vnode * sin(alpha)*t- 1/2 g*t^2


        time = 0.5*i;    // According to graph provided

        //Mechanics 2 equation:
        float theory = 30 * sin(rad)*time -.5 *9.81 * pow(time, 2);

    //Multiplying each element by it's accuracy then dividing by the total accuracy
    arr[i]= ((mpu6050[i] *mpuacc +bno55[i]* bnoacc)/(mpuacc+bnoacc)+theory)/2;

    printf(" %.2f,", arr[i]); // .2f makes it so it prints to two decimal places of the float
}
printf("}");
}



