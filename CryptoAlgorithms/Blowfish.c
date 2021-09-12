#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <alloc.h>
#include <ctype.h>
#include <dir.h>
#include <bios.h>
#include <Types.h>

typedef struct {
  unsigned long S[4][256],P[18];
} blf_ctx;

#define MAXKEYBYTES 56
#define little_endian 1
#define big_endian 1

void blowfishEncipher(blf_ctx *, unsigned long *xl, unsigned long *xr);
void blowfishDecipher(blf_ctx *, unsigned long *xl, unsigned long *xr);

#define N 16
#define noErr 0
#define DATAERROR -1
#define KEYBYTES 8

FILE* SubkeyFile;
unsigned long F(blf_ctx *bc, unsigned long x) {
  unsigned short a;
  unsigned short b;
  unsigned short c;
  unsigned short d;
  unsigned long y;
  d = x & 0x00FF;
  x >>= 8;
  c = x & 0x00FF;
  x >>= 8;

