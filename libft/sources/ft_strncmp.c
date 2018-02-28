/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 17:25:38 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 17:25:40 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <string.h>

int		ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned char *us1;
	unsigned char *us2;

	us1 = (unsigned char *)s1;
	us2 = (unsigned char *)s2;
	while (*us1 && *us1 == *us2 && n)
	{
		us1++;
		us2++;
		n--;
	}
	return ((n == 0) ? 0 : *us1 - *us2);
}
