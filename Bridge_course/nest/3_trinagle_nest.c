#include <stdio.h>
int main() {
    int n, i, j, val;
    printf("Enter n: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        val = 1;
        for (j = 1; j <= i; j++) {
            printf("%d ", val);
            val = 1 - val; // toggles between 1 and 0
        }
        printf("\n");
    }
    return 0;
}