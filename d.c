void d(void *pSrc,int len)
{
    unsigned char *line;
    int i;
    int thisline;
    int offset;

    line = (unsigned char *)pSrc;
    offset = 0;
    if(line == 0 || len > 0xffff)
        return;

    long mod = (long)line % 16;
    if(mod != 0)
    {
        printf( "%012x   ", (unsigned char *)((long)line-mod) );
        for(i=0;i<16;i++)
        {
            if(i<mod)
                printf("   ");
            else
                printf("%02x ", line[i]);
        }
        for (i = 0; i < 16; i++)
        {
            if(i<mod)
                printf(" ");
            else
                printf("%c", (line[i] >= 0x20 && line[i] < 0x7f) ? line[i] : '.');
        }
        line = line - mod + 16;
        len = len - mod + 16;
        printf("\n");
    }

    while (offset < len)
    {
        printf("%012x   ", line);
        thisline = len - offset;

        if (thisline > 16)
        {
            thisline = 16;
        }

        for (i = 0; i < thisline; i++)
        {
            printf("%02x ", line[i]);
        }

        for (; i < 16; i++)
        {
            printf("   ");
        }

        for (i = 0; i < thisline; i++)
        {
            printf("%c", (line[i] >= 0x20 && line[i] < 0x7f) ? line[i] : '.');
        }

        printf("\n");
        offset += thisline;
        line += thisline;
    }
}
