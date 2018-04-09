/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_toupper.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 15:45:03 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 15:45:21 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_str_toupper(char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		s[i] = ft_toupper(s[i]);
		i++;
	}
	return (s);
}
