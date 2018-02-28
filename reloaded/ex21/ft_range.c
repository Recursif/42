/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 14:48:16 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/10 16:40:30 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		*ft_range(int min, int max)
{
	int		n;
	int		*array;

	if (min >= max)
		return (NULL);
	if ((array = (int *)malloc(sizeof(int) * (max - min))) == NULL)
		return (NULL);
	n = 0;
	while (min + n < max)
	{
		array[n] = min + n;
		n++;
	}
	return (array);
}
