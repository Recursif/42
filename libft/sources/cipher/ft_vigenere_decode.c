/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_vigenere_decode.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:48:34 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 14:49:13 by jdumorti         ###   ########.fr       */
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
			ft_putchar('A' + (ft_toupper(s[i]) - ft_toupper(key[j]) + 26) % 26);
			j++;
		}
		else
			ft_putchar(s[i]);
		if (key[j] == '\0')
			j = 0;
		i++;
	}
}
