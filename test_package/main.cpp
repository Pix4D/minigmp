#include <iostream>
#include <mini-gmp.h>

int main()
{
    mpz_t val;
    mpz_init(val);
    
    std::cout << "minigmp was integrated successfully." << std::endl;
    return 0;
}
