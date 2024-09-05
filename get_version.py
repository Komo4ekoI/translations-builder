import re


def get_version():
    with open('src/translation_builder/__init__.py', 'r') as f:
        content = f.read()
        version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


if __name__ == "__main__":
    print(get_version())
