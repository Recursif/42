
#include "libft.h"
#include <stdlib.h>

char	*ft_strmap(char const *s, char (*f)(char))
{
	unsigned int	i;
	char			*res;

	if (!s || !f)
		return (NULL);
	i = ft_strlen(s);
	res = (char *)malloc(sizeof(char) * (i + 1));
	if (!res)
		return (NULL);
	i = 0;
	while (*s)
		res[i++] = (*f)(*s++);
	res[i] = '\0';
	return (res);
}
