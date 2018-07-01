
#include <stdio.h>

unsigned int ft_unsigned_int_magnitude(unsigned int n)
{
    unsigned int     len;

    len = 10;
    while (n >= 10)
    {
        len *= 10;
        n /= 10;
    }
    return (len);
}

int ft_is_automorphic(unsigned int n)
{
    unsigned int     magnitude;
    
    magnitude = ft_unsigned_int_magnitude(n);
    return ((n * n) % magnitude == n);
}


int main(void)
{
    unsigned int     n = 0;
    unsigned int    nbOfAutomorphic = 0;

    while (nbOfAutomorphic <= 100)
    {
        if (ft_is_automorphic(n))
        {
            printf("%d\n", n);
            nbOfAutomorphic++;
        }
        n++;
    }
    
    
    return (0);
}