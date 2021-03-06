/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:26:00 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 18:09:03 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;
	size_t	lentmp;

	if (*little == '\0')
		return ((char *)big);
	i = 0;
	while (big[i] && len)
	{
		if (big[i] == little[0])
		{
			j = i;
			lentmp = len;
			while (little[j - i] && little[j - i] == big[j] && lentmp)
			{
				j++;
				lentmp--;
			}
			if (!little[j - i])
				return ((char *)big + i);
		}
		len--;
		i++;
	}
	return (NULL);
}
