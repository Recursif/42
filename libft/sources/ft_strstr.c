/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:26:12 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 17:26:14 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <string.h>

char	*ft_strstr(const char *haystack, const char *needle)
{
	size_t	i;
	size_t	j;
	size_t	k;

	i = 0;
	while (haystack[i])
	{
		if (haystack[i] == needle[0])
		{
			j = i;
			k = 0;
			while (needle[k] && needle[k] == haystack[j])
			{
				j++;
				k++;
			}
			if (!needle[k])
				return ((char *)haystack + i);
		}
		i++;
	}
	return ((!*needle) ? (char *)haystack : NULL);
}
