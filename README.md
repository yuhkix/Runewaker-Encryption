## Installation

To get started, you'll need to install the required dependencies. You'll need the latest version of Python and the libraries `pyperclip` and `pyinstaller`. You can install them using the following commands:

```bash
pip install pyperclip
pip install pyinstaller
```

## Compilation

To compile the project into a standalone executable, you have two options:

1. **Run `compile.bat`:** This batch file will handle the compilation for you.
   
2. **Manual Compilation:** You can also run the following command in your terminal (where `main.py` is located). The `--icon` parameter is optional:

   ```bash
   pyinstaller --onefile main.py --icon=rw.ico --name Runewaker
   ```

## Usage

After compilation, you will find the executable in the `dist` folder. You can run it directly from there.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is always welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
