#include "pico/stdlib.h" // include the standard libraries for interacting with the pico

int main() {
  //Do stuff here!   
    const uint LED_PIN = PICO_DEFAULT_LED_PIN; // Use the default LED pin
    gpio_init(LED_PIN);  // initialize the interface to the pin
    gpio_set_dir(LED_PIN, GPIO_OUT);  // set the direction of the pin to send
    while (true) {  // start and continue a loop until true is not true
        gpio_put(LED_PIN, 1);  // set the pin to on or high voltage to light the LED.
        sleep_ms(1000);  // wait for a second with the LED on.
        gpio_put(LED_PIN, 0);  // set the pin to off or 0 volts to turn off the LED.
        sleep_ms(1000); // wait for second with the LED off
    }
}
