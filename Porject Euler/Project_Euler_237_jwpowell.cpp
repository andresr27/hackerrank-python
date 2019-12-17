//#include <iostream.h>
//#include <array>

template <typename T, unsigned int N>
class SquareMatrix
{
public:
  SquareMatrix()
  {
    for (size_t i = 0; i < N*N; ++i)
      vals[i] = T{0};
  }

  SquareMatrix(std::initializer_list<std::initializer_list<T>> init)
  {
    size_t i = 0, j = 0;
    for (auto row: init) {
      j = 0;
      for (auto val: row) {
	vals[i * N + j] = val;
	++j;
      }
      ++i;
    }
  }

  SquareMatrix operator+(const SquareMatrix<T, N>& rhs)
  {
    SquareMatrix<T, N> sum;
    for (size_t i = 0; i < N; ++i)
      for (size_t j = 0; j < N; ++j)
	sum.vals[i * N + j] = vals[i * N + j] + rhs.vals[i * N + j];

    return sum;
  }

  SquareMatrix operator=(const SquareMatrix<T, N>& rhs)
  {
    for (size_t i = 0; i < N * N; ++i)
      vals[i] = rhs.vals[i];
    return *this;
  }

  SquareMatrix operator*(const SquareMatrix<T, N>& rhs)
  {
    SquareMatrix<T, N> prod;
    for (size_t i = 0; i < N; ++i)
      for (size_t j = 0; j < N; ++j)
	for (size_t k = 0; k < N; ++k)
	  prod.vals[i * N + j] += vals[i * N + k] * rhs.vals[k * N + j];

    return prod;
  }

  std::array<T, N> transform(std::array<T, N> vec)
  {
    // use the SquareMatrix as a linear transform
    // on the given array
    std::array<T, N> new_vec;
    for (size_t i = 0; i < N; ++i) {
      new_vec[i] = T{0};
      for (size_t j = 0; j < N; ++j)
	new_vec[i] += vals[i * N + j] * vec[j];
    }

    return new_vec;
  };

  SquareMatrix mod(T m)
  {
    for (size_t i = 0; i < N*N; ++i)
      vals[i] %= m;

    return *this;
  }

  void print()
  {
    for (size_t i = 0; i < N; ++i) {
      for (size_t j = 0; j < N; ++j)
	std::cout << vals[i * N + j] << " ";
      std::cout << "\n";
    }
  }

  T vals[N*N];
};


int main(int argc, char* argv[])
{
  SquareMatrix<long, 4> step = {{2,2,-2,1},
				{1,0,0,0},
				{0,1,0,0},
				{0,0,1,0}},
			mat = {{1,0,0,0},
			       {0,1,0,0},
			       {0,0,1,0},
			       {0,0,0,1}};

  long mod = 100000000L;
  for (long exp = 1000000000000L - 3L; exp > 0L; exp >>= 1) {
    if (exp & 1L)
      mat = (step * mat).mod(mod);
    step = (step * step).mod(mod);
  }

  auto vec = mat.transform(std::array<long, 4>{{4, 1, 1, 0}});
  std::cout << (vec[0] % mod) << std::endl;

  return 0;
}
