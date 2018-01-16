#include <unistd.h>

void ft_putchar(char c)
{
  write(1,&c,1);
}

int ft_min(int n)
{
  int i;
  int nb;

  i = 0;
  nb = 0;
  while(++i < n)
  {
    nb = nb * 10 + i;
  }
  return(nb);
}

int ft_max(int n)
{
  int i;
  int nb;

  i = -1;
  nb = 0;
  while(i++ < n - 1)
  {
    nb = nb * 10 + 10 - n + i;
  }
  return(nb);
}

int ft_unit(int n)
{
  int i;
  int nb;

  i = 0;
  nb = 1;
  while(++i <= n)
  {
    nb = nb * 10;
  }
  return(nb);
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

void ft_print_combn(int n)
{
  int nb;
  int max;
  int unit;
  int div;
  int t;

  nb = ft_min(n) - 1;
  max = ft_max(n);
  unit = ft_unit(n);
  while(nb++ < max - unit / 10)
  {
    t = 1;
    div = unit;
    while(div > 10 && t == 1)
    {
      if((nb / (div / 10)) % 10 >= (nb / (div / 100)) % 10)
        t = 0;
      div /= 10;
    }
    if(t)
    {
      if(nb < unit / 10)
        ft_putchar('0');
      ft_putnbr(nb);
      write(1,", ",2);
    }
  }
  ft_putnbr(max);
}

void ft_print_tab(int n, int tab[10])
{
  int cpt;

  cpt = 1;
  while(cpt <= n)
  {
    ft_putchar('0' + tab[cpt++]);
  }

}

void ft_comb_rec(int n, int i, int tab[10])
{
  int p;

  p = tab[i - 1] + 1;
  while(p <= 9 - n + i)
  {
    tab[i] = p;
    if(i < n)
      ft_comb_rec(n, i + 1, tab);
    else
    {
      if(p != n - 1)
      {
        write(1,", ",2);
        ft_print_tab(n, tab);
      }
    }
    p++;
  }
}

void ft_tab_null(int *tab)
{
  while(*tab)
  {
    *tab = 0;
    tab++;
  }
}


void ft_print_combn_v2(int n)
{
  int tab[10];
  int t;

  t = -1;
  while(t < 9)
  {
    tab[t + 1]= t++;
  }
  ft_print_tab(n, tab);
  ft_tab_null(tab);
  tab[0] = -1;
  ft_comb_rec(n, 1, tab);
}

int main(void)
{
  ft_print_combn(4);
  write(1,"\n\n",2);
  ft_print_combn_v2(4);
  ft_putchar('\n');
  return(0);
}
