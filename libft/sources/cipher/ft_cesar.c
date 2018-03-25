/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_cesar.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 14:50:45 by jdumorti          #+#    #+#             */
/*   Updated: 2018/03/25 14:50:49 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_cesar(char *s, int n)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if (ft_isalpha_low(s[i]))
			ft_putchar('a' + (s[i] - 'a' + n) % 26);
		else if (ft_isalpha_up(s[i]))
			ft_putchar('A' + (s[i] - 'A' + n) % 26);
		else
			ft_putchar(s[i]);
		i++;
	}
}

