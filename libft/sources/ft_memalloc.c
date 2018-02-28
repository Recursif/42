
#include <stdlib.h>

void	*ft_memalloc(size_t size)
{
	unsigned char	*p;
	size_t			i;

	if (size == 0)
		return (NULL);
	p = (unsigned char *)malloc(sizeof(char) * size);
	if (!p)
		return (NULL);
	i = 0;
	while (i < size)
		p[i++] = 0;
	return ((void *)p);
}
