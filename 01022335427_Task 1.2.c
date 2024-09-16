#include <stdio.h>
#include <stdlib.h>

int main()
{
int i;
    printf("Please input the number you want to countdown from.");
    scanf("%d", &i);
    for (i; i>=1; i--){
        printf("%d \n", i);
        sleep(1);
    }
    printf("Blast off to the moon!");

}
