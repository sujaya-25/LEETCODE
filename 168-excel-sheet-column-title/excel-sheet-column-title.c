
#include <stdlib.h>

char* convertToTitle(int columnNumber) {
    char *s = malloc(20);
    int i = 0;

    while (columnNumber > 0) {
        columnNumber--;
        s[i] = 'A' + (columnNumber % 26);
        i++;
        columnNumber /= 26;
    }

    s[i] = '\0';

    for (int j = 0; j < i / 2; j++) {
        char temp = s[j];
        s[j] = s[i - 1 - j];
        s[i - 1 - j] = temp;
    }

    return s;
}
