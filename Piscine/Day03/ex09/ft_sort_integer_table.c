#include <stdio.h>

void ft_swap(int *a, int *b)
{
  int x;

  x = *a;
  *a = *b;
  *b = x;
}

void ft_sort_integer_table(int *tab, int size)
{
  int n;
  int b;

  n = 1;
  while(n < size)
  {
    if(tab[n] < tab[n - 1])
    {
      b = tab[n];
      tab[n] = tab[n - 1];
      tab[n -1] = b;
      n = 0;
    }
    n++;
  }
}

int main(int argc, char **argv)
{
  int tab[5];

  tab[0] = 10;
  tab[1] = 2;
  tab[2] = 30;
  tab[3] = 31;
  tab[4] = 5;

  ft_sort_integer_table(tab, 5);
  printf("%i\n%i\n%i\n%i\n%i\n", tab[0], tab[1], tab[2], tab[3], tab[4]);
  return(0);
}
