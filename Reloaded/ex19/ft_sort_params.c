/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 13:14:05 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/09 14:37:13 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

void	ft_putstr(char *str)
{
	int		n;

	n = 0;
	while (str[n])
		ft_putchar(str[n++]);
}

int		ft_strcmp(char *s1, char *s2)
{
	int		n;

	n = 0;
	while (s1[n] && s2[n] && s1[n] == s2[n])
		n++;
	return (s1[n] - s2[n]);
}

void	ft_swap(char **argv, int p)
{
	char	*str;

	str = argv[p];
	argv[p] = argv[p + 1];
	argv[p + 1] = str;
}

int		main(int argc, char **argv)
{
	int		n;

	n = 1;
	while (n < argc - 1)
	{
		if (ft_strcmp(argv[n], argv[n + 1]) > 0)
		{
			ft_swap(argv, n);
			n = 0;
		}
		n++;
	}
	n = 1;
	while (n < argc)
	{
		ft_putstr(argv[n]);
		ft_putchar('\n');
		n++;
	}
	return (0);
}
