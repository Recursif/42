/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 15:36:18 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 15:36:22 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <string.h>

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char *p;
	unsigned char target;

	p = (unsigned char *)s;
	target = (unsigned char)c;
	while (n)
	{
		if (*p == target)
			return (p);
		p++;
		n--;
	}
	return (NULL);
}
