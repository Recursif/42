/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_vigenere.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:47:53 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 14:48:26 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_vigenere(char *s, char *key)
{
	int		i;
	int		j;

	i = 0;
	j = 0;
	if (!(*key))
		return ;
	while (s[i])
	{
		if (ft_isalpha_up(ft_toupper(s[i])))
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
