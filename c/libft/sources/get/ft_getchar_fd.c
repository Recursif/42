

#include <unistd.h>

int		ft_getchar_fd(int fd)
{
	char	c;

	if (1 != read(fd, &c, 1))
		return (-1);
	return ((int) c);
}
