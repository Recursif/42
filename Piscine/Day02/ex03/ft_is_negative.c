#include <unistd.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}

void ft_is_negative(int n)
{
  (n >= 0) ? (ft_putchar('P')) : (ft_putchar('N'));
}

int main(void)
{
  ft_is_negative(6);
  return(0);
}
