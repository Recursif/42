/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 15:05:56 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 18:14:19 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	const unsigned char	*p1;
	unsigned char		*p2;

	p1 = src;
	p2 = dest;
	while (n)
	{
		*p2++ = *p1++;
		n--;
	}
	return (dest);
}
