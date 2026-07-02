#include <stdio.h>

int main()

{

    int age, rollNo, encodedAge, decodedAge;

    printf("Enter your age: ");

    scanf("%d", &age);

    printf("Enter your roll number: ");

    scanf("%d", &rollNo);

    encodedAge = age ^ rollNo;

    printf("Encoded Age = %d\n", encodedAge);

    decodedAge = encodedAge ^ rollNo;

    printf("Decoded Age = %d\n", decodedAge);

    return 0;

}
