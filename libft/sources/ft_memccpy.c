
#include <string.h>

void	*ft_memccpy(void *dest, const void *src, int c, size_t n)
{
	unsigned char		*p1;
	const unsigned char	*p2;

	p1 = dest;
	p2 = src;
	while (n)
	{
		*p1 = *p2;
		if (*p2 == (unsigned char)c)
			return (p1 + 1);
		p1++;
		p2++;
		n--;
	}
	return (NULL);
}
