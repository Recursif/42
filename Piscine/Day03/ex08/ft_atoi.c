#include <stdio.h>
#include <stdlib.h>

int ft_atoi(char *str)
{
  int n;
  int nb;
  int neg;

  n = 0;
  neg = 1;
  while( str[n] == '\n' || str[n] == ' ' || str[n] == '\t')
    n++;
  if(str[n] == '-')
  {
    neg = -1;
    n++;
  }
  nb = 0;
  while(str[n] && str[n] >= '0' && str[n] <= '9')
  {
    nb = nb * 10 + str[n] - '0';
    n++;
  }
  return(neg*nb);
}

int main(int argc, char **argv)
{
  int a;

  a = ft_atoi(argv[1]);
  printf("%i\n", a);
  printf("%i\n", atoi(argv[1]));
  return(0);
}
