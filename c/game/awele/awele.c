#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void	ft_putchar(char c)
{
	write (1, &c, 1);
}

void	ft_putstr(char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		ft_putchar(s[i]);
		i++;
	}
}

char ft_getchar()
{
	char	c;

	read (0, &c, 1);
	return (c);
}

int		ft_istopcell(char c)
{
	return (c >= 'a' && c <= 'f');
}

int		ft_isbotcell(char c)
{
	return (c >= 'A' && c <= 'F');
}

int		ft_isinstr(char c, char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int		ft_find_index_instr(char c, char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

int		ft_is_enemy_is_starving(int	**tab, int	n, int m, int enemy)
{
	int		i;
	int		sum;

	if (enemy >= n || enemy < 0)
		return (-1);
	sum = 0;
	i = 0;
	while (i < m)
	{
		sum += tab[enemy][i];
		i++;
	}
	return (sum == 0);
}	

char*	ft_test_possible_actions(int **tab, int n, int m, int j)
{
	int		i;
	char	*actions = "abcdefgq";

	i = 0;
	while (i < m)
	{
		
		if (ft_test_case(tab, n, m, j, i))
			actions[i] = ' ';
		i++;
	}
	return (actions);
}

char	ft_choice_action(char *actions)
{
	char	c;

	c = ft_getchar();
	ft_putchar('\n');
	while (!ft_isinstr(c, actions) || c == ' ')
	{
		c = ft_getchar();
		ft_putchar('\n');
	}
	return (c);
}

int**	ft_take_seed(int **tab, int n, int m, int j, int y, int x, int * sum)
{
	int		i;

	if (j == 0 && y == 1)
	{
		i = x;
		while (i >= 0 && (tab[y][i] == 2 || tab[y][i] == 3))
		{
			*sum += tab[y][i];
			tab[y][i] = 0;
			i--;
		}
	}
	else if (j == 1 && y == 0)
	{
		i = x;
		while (i < m && (tab[y][i] == 2 || tab[y][i] == 3))
		{
			*sum += tab[y][i];
			tab[y][i] = 0;
			i++;
		}
	}
	return (tab);
}


int**	ft_plant_seeds(int **tab, int n, int m, int * x, int *  y)
{
	int		seeds;

	seeds = tab[x][y];
	while (seeds > 0)
	{
		if (y == 1 && x < m - 1)
			x++;
		else if(y == 1 && x == m - 1)
			y--;
		else if (y == 0 && x > 0)
			x--;
		else if (y == 0 && x == 0)
			y++;
		else
			return NULL;
		tab[x][y]++;
	}
	return(tab);
}


int**	ft_tab_init(int	n, int m, int nb)
{
	int		i;
	int		j;
	int		**tab;

	tab = (int**)malloc(sizeof(int*) * m);
	i = 0;
	while (i < m)
	{
		tab[i] = (int*)malloc(sizeof(int) * n);
		i++;
	}
	while (i < m)
	{
		j = 0;
		while (j < n)
		{
			tab[i][j] = nb;
			j++;
		}
		i++;
	}
	return (tab);
}


void	ft_

void	ft_awele()
{
	int		state_of_game;
	int		winner = 0;
	int		scorej1 = 0;
	int		scorej2 = 0;
	int		*score;
	char	*actions;
	int		player = 1;
	int		n = 2;
	int		m = 6;
	int		**tab;

	tab = ft_tab_init(n, m, 4);
	state_of_game = 1;
	while (state_of_game)
	{
		action = ft_test_possible_actions(tab, n, m, player);
		ft_draw_game(tab, actions, player);
		tab = ft_play_turn(tab, 2, 6, player);
		player = (player) ? 0 : 1;
	}
	ft_print_winner(winner);
}


int		main(void)
{
	ft_awele();
	ft_putchar('\n');
	return (0);
}
