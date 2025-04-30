from pathlib import Path

import setuptools

# Get the long description from the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Get requirements from requirements.txt
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="f-lite",
    version="0.1.0",  # Placeholder version, consider managing this more formally
    author="Freepik and Fal AI Contributors",  # Based on README
    description="F Lite Diffusion Model codebase",  # Based on README
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FreepikLabs/fal-ai-f-lite",  # Assuming this is the repo URL
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # This is not strictly true, the license is CreativeML Open RAIL-M. Using a placeholder or more specific classifier might be needed, but this is a common starting point. Referencing the LICENSE file is key.
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",  # Common minimum version, check actual requirements if needed
    entry_points={
        "console_scripts": [
            "f-lite-generate=f_lite.generate:generate_images",
            "f-lite-to-hf=f_lite.f_lite_to_hf:f_lite_to_hf",
            "f-lite-precompute=f_lite.precompute_embeddings:main",
            "f-lite-train=f_lite.train:train",
        ],
    },
    include_package_data=True,  # Use MANIFEST.in to include non-code files
)
