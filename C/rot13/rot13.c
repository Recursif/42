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

void	ft_rot13(char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if (ft_isalphamin(s[i]))
			ft_putchar('a' + (s[i] - 'a' + 13) % 26);
		else if (ft_isalphamaj(s[i]))
			ft_putchar('A' + (s[i] - 'A' + 13) % 26);
		else
			ft_putchar(s[i]);
		i++;
	}
}

int		main(int argc, char** argv)
{
	if (argc == 2)
		ft_rot13(argv[1]);
	ft_putchar('\n');
	return (0);
}
