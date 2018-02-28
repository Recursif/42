/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:25:18 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 17:25:21 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "libft.h"
#include <stdlib.h>

char	*ft_strmap(char const *s, char (*f)(char))
{
	unsigned int	i;
	char			*res;

	if (!s || !f)
		return (NULL);
	i = ft_strlen(s);
	res = (char *)malloc(sizeof(char) * (i + 1));
	if (!res)
		return (NULL);
	i = 0;
	while (*s)
		res[i++] = (*f)(*s++);
	res[i] = '\0';
	return (res);
}
