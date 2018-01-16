#include <unistd.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}

void ft_print_comb2(void)
{
  int n;
  int p;

  p = -1;
  while(p++ < 97)
  {
    n = p;
    while(n++ < 99)
    {
      ft_putchar('0' + p / 10);
      ft_putchar('0' + p % 10);
      ft_putchar(' ');
      ft_putchar('0' + n / 10);
      ft_putchar('0' + n % 10);
      write(1,", ",2);
    }
  }
  write(1,"98 99\n",6);
}

int main(void)
{
  ft_print_comb2();
  return(0);
}
