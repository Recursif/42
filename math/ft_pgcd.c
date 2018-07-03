
#include <stdio.h>





int ft_pgcd(int a, int b)
{
    if (a % b == 0)
    {
        return (b);
    }
    else {
        return ft_pgcd(b, a % b);
    }
}

int main(void)
{
    int a = 1071;
    int b = 1029;

    printf("%d\n", ft_pgcd(a, b));
    return (0);

}