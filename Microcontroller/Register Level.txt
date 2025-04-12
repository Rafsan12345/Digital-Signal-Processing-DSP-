#include <iostream>
#include <bitset>

#define REFS1 7
#define REFS0 6 
#define REFS2 4 
#define ADLAR 5
#define MUX3 3 
#define MUX2 2 
#define MUX1 1 
#define MUX0 0 

using namespace std;
char PORTA = 0b00000000;

int main() {
    
    // Set the  bit to 1 and 0
    //PORTA |= (1 << REFS1) ; //| (1 << 4) ;
    // PORTA = ~ PORTA; // NOT 
    //PORTA &= ~(1<<0);
    //PORTA = PORTA & (1<<3);
    //PORTA &= ~(1<<3);
    // Display the binary representation
    //PORTA = 0xFF;
    //PORTA &= ~(1<<2); // bit reset 
    //PORTA  ^= (1<<3); // toggle 
    
    cout << "Binary Representation: " << bitset<8>(PORTA) << endl;

    return 0;
}
