
#include <string.h>
#include "libft.h"

static void	ft_cpy_bd(unsigned char *dest, const unsigned char *src, size_t n)
{
	size_t i;

	i = n - 1;
	while (i > 0)
	{
		dest[i] = src[i];
		i--;
	}
	dest[0] = src[0];
}

void		*ft_memmove(void *dest, const void *src, size_t len)
{
	if (src < dest && src + len >= dest)
		ft_cpy_bd(dest, src, len);
	else
		ft_memcpy(dest, src, len);
	return (dest);
}
