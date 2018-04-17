/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_vigenere_decode.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:48:34 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 16:53:29 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_vigenere_decode(char *s, char *key)
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
			s[i] = 'A' + (s[i] - ft_toupper(key[j]) + 26) % 26;
			j++;
		}
		if (key[j] == '\0')
			j = 0;
		i++;
	}
	return (s);
}
