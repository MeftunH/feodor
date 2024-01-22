# FEODOR - XOROSHIRO128 AES-CTR GENERATOR LIBRARY

1. [x] Supports multi-ethnic generation.

## Installation
`pip install feodor`

## Usage
Here are listed some examples of feodor usage.

#### Python



``` .python
import random_name_generator as rng

# Generate 2 english male names
rng.generate(descent=rng.Descent.ENGLISH, sex=rng.Sex.MALE, limit=2)

# Generate 1 italian female name
rng.generate_one(rng.Descent.ITALIAN, sex=rng.Sex.FEMALE)

# generate male name with italian first name and english last name
rng.generate_one(
    descent=(rng.Descent.ITALIAN, rng.Descent.ENGLISH),
    sex=rng.Sex.MALE
)
```

#### CLI
`generate-random-names --descent Italian/English --sex unisex --limit 1`