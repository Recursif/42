#include <unistd.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}

void ft_putnbr(int nb)
{
  if(nb >= 0)
  {
    if(nb >= 10)
    {
      ft_putnbr(nb / 10);
      ft_putchar('0' + nb % 10);
    }
    else
    {
      ft_putchar('0' + nb);
    }
  }
  else
  {
    if(nb == -2147483648)
    {
      write(1,"-2147483648",11);
    }
    else
    {
      ft_putchar('-');
      ft_putnbr(-nb);
    }
  }
}

int main(void)
{
  ft_putnbr(2147483647);
  return(0);
}
