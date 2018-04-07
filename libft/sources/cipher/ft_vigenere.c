/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_vigenere.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:47:53 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 15:49:43 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_vigenere(char *s, char *key)
{
	int		i;
	int		j;

	s = ft_str_toupper(s);
	i = 0;
	j = 0;
	if (!(*key) || !(*s))
		return (NULL);
	while (s[i])
	{
		if (ft_isalpha_up(s[i]))
		{
			s[i] = 'A' + (s[i] - ft_toupper(key[j]) - 2 * 'A' + 26) % 26;
			j++;
		}
		if (key[j] == '\0')
			j = 0;
		i++;
	}
	return (s);
}
