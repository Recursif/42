#include <unistd.h>
#include <stdio.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}


void ft_ft(int *nbr)
{
  *nbr = 42;
}

int main(void)
{
  int *nbr;
  int a;

  a = 22;
  nbr = &a;

  ft_ft(nbr);
  printf("%i\n", a);
  return(0);
}
