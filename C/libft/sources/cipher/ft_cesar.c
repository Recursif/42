

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

