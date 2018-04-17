/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 15:05:17 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 18:19:41 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	*ft_memalloc(size_t size)
{
	unsigned char	*p;
	size_t			i;

	if (size == 0)
		return (NULL);
	p = (unsigned char *)malloc(sizeof(char) * size);
	if (!p)
		return (NULL);
	i = 0;
	while (i < size)
		p[i++] = 0;
	return ((void *)p);
}
