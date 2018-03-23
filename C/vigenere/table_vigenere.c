#include <unistd.h>

void	ft_putchar(char c)
{
	write (1, &c, 1);
}

void	ft_putstr(char *s)
{
	while (*s)
		ft_putchar(*s++);
}

void	ft_table_vigenere()
{
	char	c;
	int		i;

	ft_putstr("   . A . B . C . D . E . F . G . H . I . J . K . L . M . N . O . P . Q . R . S . T . U . V . W . X . Y . Z \n");
	ft_putstr("                                                                                \n");
	c = 'A';
	while (c <= 'Z')
	{
		i = 0;

		ft_putchar(' ');
		ft_putchar(c);
		while (i <= 25)
		{
			ft_putstr(" . "); 
			ft_putchar('A' + (c + i) % 26);
			i++;
		}
		ft_putchar('\n');
		ft_putstr("                                                                                \n");
		c++;
	}
}

int		main()
{
	ft_table_vigenere();
	ft_putchar('\n');
	return (0);
}
