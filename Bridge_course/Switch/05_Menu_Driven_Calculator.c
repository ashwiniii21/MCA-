#include <stdio.h>

int main() {
    int choice;
    double radius, length, width, base, height, area;

    printf("----- MENU -----\n");
    printf("1. Area of Circle\n");
    printf("2. Area of Rectangle\n");
    printf("3. Area of Triangle\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter radius: ");
            scanf("%lf", &radius);
            area = 3.14 * radius * radius;
            printf("Area of Circle = %.2f\n", area);
            break;

        case 2:
            printf("Enter length: ");
            scanf("%lf", &length);
            printf("Enter width: ");
            scanf("%lf", &width);
            area = length * width;
            printf("Area of Rectangle = %.2f\n", area);
            break;

        case 3:
            printf("Enter base: ");
            scanf("%lf", &base);
            printf("Enter height: ");
            scanf("%lf", &height);
            area = 0.5 * base * height;
            printf("Area of Triangle = %.2f\n", area);
            break;

        case 4:
            printf("Exiting program. Goodbye!\n");
            break;

        default:
            printf("Invalid choice! Please select 1-4.\n");
    }

    return 0;
}
