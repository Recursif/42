/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 16:58:28 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/11 18:00:37 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#define CHUNK 4096
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int		n;

	n = 0;
	while (str[n])
		ft_putchar(str[n++]);
}

int		main(int argc, char **argv)
{
	char	buf[CHUNK + 1];
	int		file;
	int		ret;

	if (argc == 1)
		ft_putstr("File name missing.\n");
	else if (argc == 2)
	{
		file = open(argv[1], O_RDONLY);
		if (file == -1)
			return (1);
		while ((ret = read(file, buf, CHUNK)) > 0)
		{
			write(1, buf, ret);
		}
		close(file);
	}
	else
		ft_putstr("Too many arguments.\n");
	return (0);
}
