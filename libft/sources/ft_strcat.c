
#include <string.h>
#include "libft.h"

char	*ft_strcat(char *dest, const char *src)
{
	size_t i;
	size_t len;

	len = ft_strlen(dest);
	i = 0;
	while (src[i])
	{
		dest[i + len] = src[i];
		i++;
	}
	dest[i + len] = '\0';
	return (dest);
}
