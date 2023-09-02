#include <stdio.h>
#include <stdlib.h>

// Assigning Global Variables so that they don't get reset whenever I call the function every time

char *arr[100];
    int ID = 0;
    char desc[100];
    int run = 1;
    int temp;
     int i;



 // First Function

  void AddTask(char *description[]){
//printf("%d", ID);

    //Here I set the First element in the pointer array to the description entered as an argument
   // arr[ID] = description[]; //<-- Turns out this was a mistake !

    // I got the idea of these two lines from Chat GPT
    arr[ID] = malloc(strlen(description) + 1);
    strcpy(arr[ID], description);
 //End of Chat GPT inspiration

    //increasing the ID or index so that the next time I run the function it adds to the
    // 2nd index of the array instead of overriding the first one
    ID =ID +1;

    printf("Task Added Successfully!\n");


    }

int main()
{

////    char arr[50][100];





    void MainMenu(){

if (run==0){
    return;

}
//printf("%d", ID);

 printf("Minions Task Manager\n");
 printf("1. Add Task \n");
 printf("2. View Tasks\n");
 printf("3. Remove Task \n");
 printf("4. Exit\n");
 printf("\nSelect an option:");
 scanf("%d",&i);
// if user inputs numbers between 1-4 else it tells it to re-enter the input
 if(i>0 && i<5){
//        arr[0]= "First";
//        arr[1] ="Second";
//        arr[2] ="Third";
// switch(i){
//case (1):
if (i==1){
    printf("Enter task description:");

// gets user input
//    scanf("%s", &desc); (I googled this and it's supposed to work idk why it doesn't)


    //Gets user input
    fflush(stdin);
    fgets(desc, 100, stdin);  // I copied these 2 lines from a random website...I still don't-
                              //understand those input streams fully but it works for sentence inputs.


//    ID = sizeof(arr);

    //calling the function....
    AddTask(desc);

//    printf("%d", ID);
//    printf("%s", arr[ID]);

    //Redirecting to Main Menu
    MainMenu();
}
//case (2):
else if (i==2){

//looping on the array that we just created with the-
// Add Task function

    for(int k=0; k<ID; k++){
//if (arr[k]!= NULL){
//        printf("this is iteration %d",k);
        printf("Task %d Desc:", k+1);
        printf("%s\n", arr[k]);

    }
    MainMenu();
//    }
}
//case (3):
else if(i==3){

    printf("Please enter the no. of the task you wish to remove.\n");
    scanf("%d",&temp);
    // temp-- so that the task number matches the index. eg. Task 1 has index 0

    temp--;
    for(int k=0; k<50; k++){

//            printf("iteration %d\n",k);

        // So, The element we chose to remove, we will replace it with the element after it
        // and then the element after it will get replaced by the element after that
        // so it basically shifts the whole array back 1 index removing the unwanted element

        //when I assign arr[2] = arr[3] now arr[2] and arr[3] have the same value
        // and the previous value of arr[2] doesn't exist
        arr[temp]=arr[temp+1];
        temp++;
    }
    //I reduce the ID by one so that when I re-add the task
    // It gets put in the right order
    ID--;
    printf("Removed successfully\n");

    MainMenu();
}
//case (4):
else if(i==4){


    printf("Goodbye!");

    run=0;
    MainMenu();
   }
else {
    printf("Please enter a number from 1-4\n");
    MainMenu();
}
}    }
       MainMenu();
}

