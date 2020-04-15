#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
	int fd = -1;
	char buf[512] = {0};

	if(argc <= 1) {
		printf("%s <file>\n", argv[0] == NULL ? "./challenge" : argv[0]);
		exit(1);
	}

	if(access(argv[1], R_OK)) {
		perror("failed access check");
		exit(1);
	}

	fd = open(argv[1], O_RDONLY);
	if(fd == -1) {
		perror("failed file open");
		exit(1);
	}

	read(fd, &buf, sizeof(buf)-1);
	printf("%s\n", buf);

	close(fd);
	return 0;
}
