/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:24:59 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 17:25:03 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <stdlib.h>
#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	unsigned int	len;
	unsigned int	i;
	char			*res;

	if (!s1 || !s2)
		return (NULL);
	len = ft_strlen(s1);
	len += ft_strlen(s2);
	res = (char *)malloc(sizeof(char) * (len + 1));
	if (!res)
		return (NULL);
	i = 0;
	while (*s1)
		res[i++] = *s1++;
	while (*s2)
		res[i++] = *s2++;
	res[i] = '\0';
	return (res);
}
