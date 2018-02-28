/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:25:07 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 17:25:09 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <string.h>
#include "libft.h"

static void	ft_concatenate(char *dst, const char *src, size_t dlen, size_t left)
{
	size_t i;

	i = 0;
	while (left != 1 && src[i])
	{
		dst[dlen + i] = src[i];
		left--;
		i++;
	}
	dst[dlen + i] = '\0';
}

size_t		ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t i;
	size_t dlen;
	size_t slen;
	size_t left;

	i = 0;
	left = size;
	while (left && dst[i])
	{
		i++;
		left--;
	}
	dlen = i;
	slen = ft_strlen(src);
	left = size - dlen;
	if (left == 0)
		return (dlen + slen);
	ft_concatenate(dst, src, dlen, left);
	return (dlen + slen);
}
