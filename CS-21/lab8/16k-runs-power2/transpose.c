#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

const char *OUTPUT_PATH = "output.ppm";

void transpose_basic(uint8_t *data, uint32_t width, uint32_t height) {
  uint8_t *temp = calloc(width * height * 3, 1);

  for (int r = 0; r < height; r++) {
    for (int c = 0; c < width; c++) {
      for (int rgb = 0; rgb <= 2; rgb++) {
        temp[c * height * 3 + r * 3 + rgb] = data[r * width * 3 + c * 3 + rgb];
      }
    }
  }

  memcpy(data, temp, width * height * 3);
  free(temp);
}

void transpose_improved(uint8_t *data, uint32_t width, uint32_t height, int blocksize) {
  uint8_t *temp = calloc(width * height * 3, 1);
  for (int b_r = 0; b_r < height; b_r += blocksize){
    for (int b_c = 0; b_c < width; b_c += blocksize){


      for (int r = b_r; r < b_r + blocksize && r < height; r++) {
        for (int c = b_c; c < b_c + blocksize && c < width; c++) {
          for (int rgb = 0; rgb <= 2; rgb++) {
            temp[c * height * 3 + r * 3 + rgb] = data[r * width * 3 + c * 3 + rgb];
          }
        }
      }
    }
  }
  memcpy(data, temp, width * height * 3);
  free(temp);
}               

void skip_comment_lines(FILE *fp) {
  int ch;

  while ((ch = fgetc(fp)) == '#') {
    fscanf(fp, " %*[^\n]\n");
  }

  ungetc(ch, fp);
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    fprintf(stderr, "Usage: ./transpose <filename> <0 or 1>\n");
    return -1;
  }

  char *input_path = argv[1];
  int blocksize = atoi(argv[2]);

  FILE *in = fopen(input_path, "rb");
  if (in == NULL) {
    printf("Error reading %s\n", input_path);
    return -1;
  }

  char magic[3];
  fread(&magic, 1, sizeof(magic), in);

  if (strncmp(magic, "P6\n", 3) != 0) {
    fprintf(stderr, "Magic bytes not found in %s\n", input_path);
    return -1;
  }

  skip_comment_lines(in);

  uint32_t width, height;
  fscanf(in, " %u %u", &width, &height);

  skip_comment_lines(in);

  uint32_t max_value;
  fscanf(in, " %u%*c", &max_value);

  printf("%u x %u image with max value %u\n", width, height, max_value);

  uint32_t data_size = width * height * 3;
  uint8_t *data = malloc(data_size);

  uint32_t tmp;
  if ((tmp = fread(data, 1, data_size, in)) != data_size) {
    fprintf(stderr, "Error reading image data (%u expected, %u actual)\n", data_size, tmp);
    free(data);
    fclose(in);
    return -1;
  }
  fclose(in);

  if (blocksize == 0) {
    transpose_basic(data, width, height);
  } else {
    transpose_improved(data, width, height, blocksize);
  }

  FILE *out = fopen(OUTPUT_PATH, "wb");
  if (out == NULL) {
    fprintf(stderr, "Error opening %s for writing\n", OUTPUT_PATH);
    free(data);
    return -1;
  }

  fprintf(out, "P6\n%u %u\n%u\n", height, width, max_value);
  fwrite(data, 1, data_size, out);

  fclose(out);
  free(data);
}