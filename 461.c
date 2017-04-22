int hammingDistance(int x, int y)
{
  int result = 0;
  int x_remainder = 0, y_remainder =0;
  while(x != 0 || y != 0)
    {
      x_remainder = x % 2;
      y_remainder = y % 2;
      if(x_remainder != y_remainder)
        ++result;
      x = x/2;
      y = y/2;
    }
  return result;
}
