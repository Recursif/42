/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_facto.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 16:54:22 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 16:56:28 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_facto(int n)
{
	if (i >= 1 && i <= 13)
		return (n * ft_facto(n - 1));
	else if (i == 0)
		return (1);
	else
		return (-1);
}
