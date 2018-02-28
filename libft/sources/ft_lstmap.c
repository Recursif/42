/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/02/28 15:34:11 by jdumorti          #+#    #+#             */
/*   Updated: 2018/02/28 15:34:13 by jdumorti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "libft.h"

t_list	*ft_lstmap(t_list *lst, t_list *(*f)(t_list *elem))
{
	t_list	*res;
	t_list	*prev;
	t_list	*curr;

	if (!lst || !f)
		return (NULL);
	res = (*f)(lst);
	if (!res)
		return (NULL);
	prev = res;
	lst = lst->next;
	while (lst)
	{
		curr = (*f)(lst);
		if (!curr)
			return (NULL);
		prev->next = curr;
		prev = curr;
		lst = lst->next;
	}
	return (res);
}
