
import json
import random
from pathlib import Path


CITIES = {
    "Munich": [
        "Schwabing",
        "Maxvorstadt",
        "Sendling",
        "Haidhausen",
        "Moosach",
    ],
    "Berlin": [
        "Neukölln",
        "Kreuzberg",
        "Prenzlauer Berg",
        "Charlottenburg",
        "Friedrichshain",
    ],
    "Hamburg": [
        "Eimsbüttel",
        "Altona",
        "Winterhude",
        "St. Pauli",
        "Barmbek",
    ],
    "Leipzig": [
        "Südvorstadt",
        "Connewitz",
        "Plagwitz",
        "Gohlis",
        "Zentrum",
    ],
}


HEATING_TYPES = [
    "gas",
    "district heating",
    "heat pump",
]


def generate_apartment(apartment_id: int) -> dict:
    city = random.choice(list(CITIES.keys()))
    district = random.choice(CITIES[city])

    size_m2 = random.randint(35, 140)
    rooms = random.choice([1, 2, 2, 3, 3, 4, 5])

    # Very simple synthetic rent calculation
    rent_per_m2 = random.randint(10, 28)
    cold_rent = size_m2 * rent_per_m2

    year_built = random.randint(1950, 2024)

    balcony = random.random() < 0.65
    parking = random.random() < 0.35

    heating = random.choice(HEATING_TYPES)

    return {
        "id": f"APT-{apartment_id:04d}",
        "city": city,
        "district": district,
        "size_m2": size_m2,
        "rooms": rooms,
        "cold_rent": cold_rent,
        "year_built": year_built,
        "balcony": balcony,
        "parking": parking,
        "heating": heating,
    }


def main():
    random.seed(42)

    apartments = [
        generate_apartment(i)
        for i in range(1, 101)
    ]

    output_path = Path("data/raw/apartments.json")

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            apartments,
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(f"Generated {len(apartments)} apartments.")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
