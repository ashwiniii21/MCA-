#include <stdio.h>

int main()

{

    float subject1, subject2, subject3, total, average;

    printf("Enter marks of Subject 1: ");

    scanf("%f", &subject1);

    printf("Enter marks of Subject 2: ");

    scanf("%f", &subject2);

    printf("Enter marks of Subject 3: ");

    scanf("%f", &subject3);

    total = subject1 + subject2 + subject3;

    average = total / 3;

    printf("Total Marks = %.2f\n", total);

    printf("Average Marks = %.2f\n", average);

    return 0;

}
