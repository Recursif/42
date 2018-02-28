
#include <string.h>

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	const unsigned char	*p1;
	unsigned char		*p2;

	p1 = src;
	p2 = dest;
	while (n)
	{
		*p++ = *p++;
		n--;
	}
	return (dest);
}
