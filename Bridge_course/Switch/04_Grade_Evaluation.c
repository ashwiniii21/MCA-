#include <stdio.h>

int main() {
    int marks, band;

    printf("Enter marks (0-100): ");
    scanf("%d", &marks);

    if (marks < 0 || marks > 100) {
        printf("Invalid marks! Must be between 0 and 100.\n");
        return 0;
    }

    band = marks / 10;   // e.g. 95 -> 9, 72 -> 7, 30 -> 3

    switch (band) {
        case 10:
        case 9:
            printf("Grade: A\n");
            break;
        case 8:
            printf("Grade: B\n");
            break;
        case 7:
            printf("Grade: C\n");
            break;
        case 6:
            printf("Grade: D\n");
            break;
        default:
            // Any band from 0 to 5 means marks are below 60
            printf("Grade: F\n");
    }

    return 0;
}
