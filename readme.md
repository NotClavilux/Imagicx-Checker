
# Imagicx Checker

[![GitHub Star](https://img.shields.io/github/stars/NotClavilux/Imagicx-Checker.svg?style=social)](https://github.com/NotClavilux/Imagicx-Checker/stargazers)

Imagicx Checker is a Python script that generates random image URLs from a German image hosting site called imagicx. It then checks if these URLs contain valid images.

## Usage

1. Clone the repository.

   ```bash
   git clone https://github.com/NotClavilux/Imagicx-Checker.git
   ```

2. Change to your project directory.

   ```bash
   cd Imagicx-Checker
   ```

3. Install required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Create a file called proxies.txt containing a list of proxies, one per line.

5. Run the script.

   ```bash
   python imagicx_checker.py
   ```

This script generates a random URL, checks its validity using a proxy, and saves the valid URL to a file called hit.txt.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers of imagicx for providing a platform to test such tools.

If you find this tool useful, please consider starring it on [GitHub](https://github.com/NotClavilux/Imagicx-Checker).
