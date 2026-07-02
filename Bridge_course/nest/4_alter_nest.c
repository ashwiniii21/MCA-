#include <stdio.h>

int main() {
    int n, i, j, val;
    
    printf("Enter n (number of rows): ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        val = (i % 2 == 0) ? 0 : 1;
        if (i == 2 || i == 3 || i == 6) val = 0;
        else val = 1;

        for (j = 1; j <= i; j++) {
            printf("%d ", val);
            val = 1 - val;
        }
        printf("\n");
    }
    return 0;
}