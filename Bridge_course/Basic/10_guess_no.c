#include <stdio.h>
int main() {
    int secret = 24; 
    int guess, attempts = 0;

    printf("Guess the number between 20 and 30!\n");

    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;

        if (guess < secret)
            printf("Too low! Try again.\n");
        else if (guess > secret)
            printf("Too high! Try again.\n");
        else
            printf("Correct! You guessed it in %d attempts.\n", attempts);

    } while (guess != secret);

    return 0;
}