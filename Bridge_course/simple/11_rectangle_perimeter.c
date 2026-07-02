#include <stdio.h>

int main()

{

    float length, breadth, perimeter;

    printf("Enter the length: ");

    scanf("%f", &length);

    printf("Enter the breadth: ");

    scanf("%f", &breadth);

    perimeter = 2 * (length + breadth);

    printf("Perimeter of the rectangle = %.2f\n", perimeter);

    return 0;

}
