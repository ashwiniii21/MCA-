#include <stdio.h>
#include <ctype.h>   // for tolower()

int main() {
    char ch, lowerCh;

    printf("Enter a character: ");
    scanf(" %c", &ch);   

    lowerCh = tolower(ch);  

    switch (lowerCh) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            printf("%c is a Vowel\n", ch);
            break;
        default:
            // Only treat it as consonant if it's actually a letter
            if (isalpha(ch))
                printf("%c is a Consonant\n", ch);
            else
                printf("%c is not an alphabet\n", ch);
    }

    return 0;
}
