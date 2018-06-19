/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   includes.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/06/03 15:12:19 by jdumorti          #+#    #+#             */
/*   Updated: 2018/06/03 15:35:26 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef INCLUDES_H
# define INCLUDES_H

# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>
# include "tetriminos.h"
# include "./libft/libft.h"
# define BUFF_SIZE 20

int			created_grid(unsigned int **grid, size_t size);
void		ft_print_final_grid(unsigned int ***tab,
			size_t nb_tetri, size_t size);
size_t		reader(unsigned int ***tab, unsigned int fd);
int			solve(unsigned int ***tab, unsigned int **grid,
			size_t nb_tetri);
void		destroy_tab(unsigned int **str_tab, size_t size_t size);
int			condition(unsigned int tetri,
			unsigned int **grid, size_t len, size_t pos);
void		putit(unsigned int tetri, unsigned int **grid,
			size_t len, size_t pos):
void		iter_grid(unsigned int tetri,
			unsigned int **grid, size_t len, size_t pos, int kiki);

#endif
