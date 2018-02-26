/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 18:23:44 by jdumorti          #+#    #+#             */
/*   Updated: 2017/11/08 18:38:00 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_strcmp(char *s1, char *s2)
{
	int		n;

	n = 0;
	while (s1[n] && s2[n] && s1[n] == s2[n])
		n++;
	return (s1[n] - s2[n]);
}