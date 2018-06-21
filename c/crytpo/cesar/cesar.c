#include <unistd.h>

void	ft_putchar(char c)
{
	write (1, &c, 1);
}

int		ft_isalphamin(char c)
{
	return (c >= 'a' && c <= 'z');
}

int		ft_isalphamaj(char c)
{
	return (c >= 'A' && c <= 'Z');
}

int		ft_atoi(char *str)
{
	int	res;
	int	neg;

	res = 0;
	neg = 1;
	while ((*str > 8 && *str < 14) || *str == ' ')
				str++;
	neg = (*str == '-') ? -1 : 1;
	str = (neg == -1 || *str == '+') ? str + 1 : str;
	while (*str >= '0' && *str <= '9')
				res = res * 10 + (*str++ - '0');
	return (res * neg);	
}


void	ft_cesar(char *s, int n)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if (ft_isalphamin(s[i]))
			ft_putchar('a' + (s[i] - 'a' + n) % 26);
		else if (ft_isalphamaj(s[i]))
			ft_putchar('A' + (s[i] - 'A' + n) % 26);
		else
			ft_putchar(s[i]);
		i++;
	}
}

int		main(int argc, char** argv)
{
	if (argc == 3)
		ft_cesar(argv[1], ft_atoi(argv[2]));
	ft_putchar('\n');
	return (0);
}
