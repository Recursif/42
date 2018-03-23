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

void	ft_vigenre(char *s, char *key)
{
	int		i;
	int		j;

	i = 0;
	j = 0;
	if (!(*key))
		return ;
	while (s[i])
	{
		if (ft_isalphamin(s[i]))
		{
			ft_putchar('a' + (s[i] + key[j] - 2 * 'a') % 26);
			j++;
		}
		else if (ft_isalphamaj(s[i]))
		{
			ft_putchar('A' + (s[i] + key[j] - 2 * 'A') % 26);
			j++;
		}
		else
			ft_putchar(s[i]);
		if (key[j] == '\0')
			j = 0;
		i++;
	}
}

int		main(int argc, char** argv)
{
	if (argc == 3)
		ft_vigenre(argv[1], argv[2]);
	ft_putchar('\n');
	return (0);
}
