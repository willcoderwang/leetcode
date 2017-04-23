char* complexNumberMultiply(char* a, char* b)
{
  int a_real, a_vir, b_real, b_vir;
  char *result = (char *) malloc(1024 * sizeof(char));
  sscanf(a, "%d+%di", &a_real, &a_vir);
  sscanf(b, "%d+%di", &b_real, &b_vir);
  sprintf(result, "%d+%di", a_real *  b_real - a_vir * b_vir, a_real * b_vir + a_vir * b_real);
  return result;
}
