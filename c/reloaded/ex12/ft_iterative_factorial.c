/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 17:15:01 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/10 16:03:11 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_iterative_factorial(int nb)
{
	int	counter;

	if (nb < 0 || nb >= 13)
		return (0);
	else if (nb == 0)
		return (1);
	else
	{
		counter = nb - 1;
		while (counter >= 2)
			nb *= counter--;
		return (nb);
	}
}
