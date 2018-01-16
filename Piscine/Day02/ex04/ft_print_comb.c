#include <unistd.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}

void ft_print_comb(void)
{
  int n;

  n = 11;
  while(n++ < 689)
  {
    if((n / 100 < (n % 100) / 10) && ((n % 100) / 10 < n % 10))
    {
      ft_putchar('0' + n / 100);
      ft_putchar('0' + (n % 100) / 10);
      ft_putchar('0' + n % 10);
      write(1,", ",2);
    }
  }
  write(1,"789\n",4);
}

void ft_print_comb_v2(void)
{
  int cent;
  int dix;
  int un;

  cent = -1;
  while(++cent <= 6)
  {
    dix = cent;
    while(++dix <= 8)
    {
      un = dix + 1;
      while(un <= 9)
      {
        ft_putchar('0' + cent);
        ft_putchar('0' + dix);
        ft_putchar('0' + un++);
        write(1,", ",2);
      }
    }
  }
  write(1,"789\n",4);
}

int main(void)
{
  ft_print_comb_v2();
  ft_print_comb();
  return(0);
}
