#include <stdio.h>

int main() {
    int num, sum = 0, i;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    for (i = 1; i <= num; ++i) {
        sum += i;
    }

    printf("Sum = %d\n", sum);
    return 0;
}
