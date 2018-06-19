# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/03 14:50:00 by jdumorti          #+#    #+#              #
#    Updated: 2018/06/03 15:05:35 by jdumorti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = fillit
CC = gcc
CFLAGS = -Wall -Wextra -Werror
INCLUDES = .
SRCS = main.c reader.c solver.c utils.c fillit.c
LIB_DIR = ./libft
LIB_NAME = ft
OBJS = $(SRCS:.c=.o)

all: library $(NAME)

library:
	make -C ./libft

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -L$(LIB_DIR) -l$(LIB_NAME) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -I$(INCLUDES) -c $?

clean:
	rm -f $(NAME)
	rm -f ./libft/libft.a

re: fclean all
