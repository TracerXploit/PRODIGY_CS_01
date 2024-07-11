# Caesar Cipher

This project is part of my internship at Prodigy InfoTech. It implements the Caesar Cipher algorithm in Python to perform encryption and decryption of messages.

## Features

- Encrypt a message using the Caesar Cipher algorithm
- Decrypt a message using the Caesar Cipher algorithm
- User can specify the shift value for encryption and decryption

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/mihirsathvar56/caesar-cipher.git
    cd caesar-cipher
    ```
2. Run the Python script `caesar_cipher.py`:
    ```bash
    python caesar_cipher.py
    ```
3. Follow the on-screen instructions to either encrypt or decrypt a message.

### Example

```bash
$ python caesar_cipher.py
Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'q' to quit: e
Enter your message: Hello, World!
Enter shift value: 3
Encrypted message: Khoor, Zruog!

Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'q' to quit: d
Enter your message: Khoor, Zruog!
Enter shift value: 3
Decrypted message: Hello, World!
```

## How it works

The Caesar Cipher algorithm shifts each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The same shift value is used for both encryption and decryption, but in the opposite direction for decryption.

## Output Examples

## Encrypting a Message

Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'q' to quit: e
Enter your message: OpenAI is awesome!
Enter shift value: 5
Encrypted message: TsjsFN nx fbjtrj!

## Decrypting a Message

Do you want to (e)ncrypt or (d)ecrypt a message? Enter 'q' to quit: d
Enter your message: TsjsFN nx fbjtrj!
Enter shift value: 5
Decrypted message: OpenAI is awesome!

## Contributing

If you have suggestions for improvements or find any bugs, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
