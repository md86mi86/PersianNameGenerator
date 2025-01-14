
# PersianNameGenerator

`PersianNameGenerator` is a Python package designed to generate random Persian names, including both first names and last names. It is useful for generating sample data for applications, websites, or testing purposes.

## Installation

You can install the `PersianNameGenerator` package via `pip` from PyPI:

```bash
pip install PersianNameGenerator
```

## Usage

Once installed, you can use the package to generate random Persian names in your Python project.

### Importing the Package

To use the package, import the `PersianNameGenerators` class:

```python
from PersianNameGenerator import PersianNameGenerators
```

### Example Code

Here’s an example of how you can generate random Persian names:

```python
# Create an instance of the PersianNameGenerators class
name_generator = PersianNameGenerators()

# Generate a random first name
first_name = name_generator.getFirstName()
print(f"Random First Name: {first_name}")

# Generate a random last name
last_name = name_generator.getLastName()
print(f"Random Last Name: {last_name}")

# Generate a random full name (first + last)
full_name = name_generator.getFullName()
print(f"Random Full Name: {full_name}")
```

### Example Output:

```
Random First Name: آرش
Random Last Name: رضایی
Random Full Name: آرش رضایی
```

## Features

- Generates random Persian **first names**.
- Generates random Persian **last names**.
- Combines first and last names to create a **full name**.

## License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file in the repository.

## Contributing

If you would like to contribute to the development of `PersianNameGenerator`, feel free to fork the repository and submit a pull request. We welcome any suggestions or improvements.

## Acknowledgments

- The list of names used in this package is based on common Persian names and may not be exhaustive.
- Special thanks to the community for contributing ideas for name lists and improvements.

## GitHub Repository

You can find the repository for this project on GitHub: [github.com/md86mi86/PersianNameGenerator](https://github.com/md86mi86/PersianNameGenerator)
