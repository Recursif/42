/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 14:38:24 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/10 16:23:56 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strdup(char *src)
{
	char	*dest;
	int		n;

	n = 0;
	while (src[n])
		n++;
	if ((dest = (char *)malloc(sizeof(char) * (n + 1))) == NULL)
		return (NULL);
	n = 0;
	while (src[n])
	{
		dest[n] = src[n];
		n++;
	}
	dest[n] = src[n];
	return (dest);
}
