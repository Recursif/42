
#include <stdio.h>

unsigned int ft_unsigned_int_len(unsigned int n)
{
    unsigned int     len;

    len = 1;
    while (n >= 10)
    {
        len++;
        n /= 10;
    }
    return (len);
}

int ft_is_automorphic(unsigned int n)
{
    unsigned int     len;
    
    
    len = ft_unsigned_int_len(n) * 10;
    printf("%d\n", len);
    return ((n * n) % len == n);
}

int main(void)
{
    unsigned int     n = 5;


    printf("%d\n", ft_is_automorphic(n));
    n = 3;  
    printf("%d\n", ft_is_automorphic(n));
    
    return (0);
}