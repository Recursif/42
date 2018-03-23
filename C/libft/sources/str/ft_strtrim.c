/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:26:20 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 18:15:29 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_trimbegin(char const *s)
{
	size_t	i;

	i = 0;
	while (s[i] && ft_isspace(s[i]))
		i++;
	return (i);
}

static size_t	ft_trimend(char const *s)
{
	size_t	i;

	if (!*s)
		return (0);
	i = ft_strlen(s) - 1;
	while (i > 0 && ft_isspace(s[i]))
		i--;
	return (i);
}

char			*ft_strtrim(char const *s)
{
	size_t	begin;
	size_t	end;

	if (!s)
		return (NULL);
	begin = ft_trimbegin(s);
	end = ft_trimend(s);
	if (end < begin)
		return (ft_strdup(""));
	return (ft_strsub(s, begin, end - begin + 1));
}
