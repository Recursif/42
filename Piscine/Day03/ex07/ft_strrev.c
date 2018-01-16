

int ft_strlen(char *str)
{
  int n;

  n = 0;
  while(*str)
  {
    n++;
    str++;
  }
  return(n);
}

char *ft_strrev(char *str)
{
  char *dest;
  int len;
  int  n;

  *dest = *str;
  len = ft_strlen(*str);
  n = O;
  while(str[n])
  {
    dest[len - n] = str[n];
    n++;
  }
  dest[n] = str[n];
  return(*dest);
}
