
#include <string.h>

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char *p;
	unsigned char target;

	p = (unsigned char *)s;
	target = (unsigned char)c;
	while (n)
	{
		if (*p == target)
			return (p);
		p++;
		n--;
	}
	return (NULL);
}
