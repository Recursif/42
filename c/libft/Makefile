NAME=libft.a
AR=ar
ARFLAGS=rcs
CC=gcc
CFLAGS=-Wall -Wextra -Werror
INCLUDES=-I includes/
SOURCES= sources/

CONVERT =convert/
IS = is/
MEM = mem/
STR = str/
LST = lst/
PUT = put/
GET = get/

LIBCSRC= $(addprefix $(SOURCES), \
	\
	$(addprefix $(CONVERT), \
	ft_atoi.c ft_itoa.c \
	ft_tolower.c ft_toupper.c) \
	\
	$(addprefix $(IS), \
	ft_isalnum.c ft_isalpha.c \
	ft_isascii.c ft_isdigit.c \
	ft_isblank.c ft_isnumber.c \
	ft_islower.c ft_isupper.c \
	ft_isspace.c ft_isprint.c) \
	\
	$(addprefix $(MEM), \
	ft_bzero.c ft_memset.c \
	ft_memcpy.c ft_memccpy.c \
	ft_memmove.c ft_memchr.c \
	ft_memcmp.c ft_memalloc.c \
	ft_memdel.c) \
	\
	$(addprefix $(STR), \
	ft_strlen.c \
	ft_strdup.c ft_strndup.c\
	ft_strcpy.c	ft_strncpy.c \
	ft_strcat.c ft_strncat.c \
	ft_strlcat.c \
	ft_strchr.c ft_strrchr.c \
	ft_strstr.c ft_strnstr.c \
	ft_strcmp.c ft_strncmp.c \
	ft_strclr.c ft_strdel.c \
	ft_striter.c ft_striteri.c \
	ft_strnew.c \
	ft_strmap.c ft_strmapi.c \
	ft_strequ.c ft_strnequ.c \
	ft_strsub.c ft_strjoin.c \
	ft_strtrim.c ft_strtrimc.c \
	ft_strsplit.c) \
	\
	$(addprefix $(LST), \
	ft_lstnew.c ft_lstadd.c \
	ft_lstiter.c ft_lstmap.c \
	ft_lstdel.c ft_lstdelone.c\
	ft_lstpop.c) \
	\
	$(addprefix $(PUT), \
	ft_putchar_fd.c ft_putchar.c \
	ft_putstr_fd.c ft_putstr.c \
	ft_putnbr_fd.c ft_putnbr.c \
	ft_putendl_fd.c ft_putendl.c))

SRC= $(LIBCSRC)
OBJ= $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(AR) $(ARFLAGS) $(NAME) $(OBJ)

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -o $@ -c $<

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean
	$(MAKE) $(NAME)

.PHONY: all clean fclean re
