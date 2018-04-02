/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isspace.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 18:16:49 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 18:16:52 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_isspace(int c)
{
	return (c == ' '
			|| c == '\t'
			|| c == '\n'
			|| c == '\f'
			|| c == '\v'
			|| c == '\r');
}