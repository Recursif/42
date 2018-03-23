#include "libft.h"

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
		if (ft_isalpha_up(ft_toupper(s[i]))
		{
			ft_putchar('A' + (ft_toupper(s[i]) - ft_toupper(key[j]) - 2 * 'A' + 26) % 26);
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
