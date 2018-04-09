/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_pow.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 16:59:51 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 17:30:23 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

unsigned long long	ft_pow(unsigned long long n, unsigned long long pow)
{
	if (pow >= 1)
		return (n * ft_pow(n, pow - 1));
	else if (pow == 0)
		return (1);
	else
		return (0);
}

int		main(int ac, char **av)
{
	unsigned long long	i;

	i = ft_pow(2, 58);
	printf("%llu", i);
	return (0);
}
