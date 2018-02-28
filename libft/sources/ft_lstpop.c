/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstpop.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 15:34:21 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 15:34:23 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "libft.h"
#include <stdlib.h>
#include <string.h>

void	*ft_lstpop(t_list **alst, size_t *content_size)
{
	void	*res;
	t_list	*next;

	if (!alst || !*alst)
		return (NULL);
	res = (*alst)->content;
	if (content_size)
		*content_size = (*alst)->content_size;
	next = (*alst)->next;
	free(*alst);
	*alst = next;
	return (res);
}
