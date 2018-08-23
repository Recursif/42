/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cesar.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:50:45 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 15:39:47 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_cesar(char *s, int n)
{
	int		i;
	char	*res;

	res = ft_strdup(s);
	i = 0;
	while (s[i])
	{
		if (ft_isalpha_low(s[i]))
			res[i] = 'a' + (s[i] - 'a' + n) % 26;
		else if (ft_isalpha_up(s[i]))
			res[i] = 'A' + (s[i] - 'A' + n) % 26;
		i++;
	}
	return (res);
}
