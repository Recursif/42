/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/06/03 15:07:15 by jdumorti          #+#    #+#             */
/*   Updated: 2018/06/03 16:23:48 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include "includes.h"

static int	return_error(void)
{
	ft_putendl("error");
	return (1);
}

int			main(int argc, char **argv)
{
	int				fd;
	unsigned int	**tab;
	unsigned int	*grid;
	size_t			nb_tetri;

	if (argc != 2)
	{
		ft_putendl("usage: ./fillit source_file");
		return (1);
	}
	if ((fd = open(argv[1], O_RDONLY)) == -1)
		return (return_error());
	if (!(tab = (unsigned int **)malloc(sizeof(unsigned int *) * 27)))
		return (return_error());
	if (!(nb_tetri = reader(&tab, fd)))
		return (return_error());
	ft_print_final_grid(&tab, nb_tetri, solve(&tab, &grid, nb_tetri));
	destroy_tab(tab, nb_tetri + 1);
	free(grid);
	close(fd);
	return (0);
}
