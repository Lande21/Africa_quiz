#Author:Rolande Umuhoza
#Github : Lande21
#Date : July, 28, 2024
import random

# List of African countries and their capitals
countries_and_capitals = {
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Ghana": "Accra",
    "Ethiopia": "Addis Ababa",
    "Morocco": "Rabat",
    "Senegal": "Dakar",
    "Rwanda": "Kigali",
    "Burundi": "Gitega",
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto-Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Cameroon": "Yaounde",
    "Cape Verde": "Praia",
    "Chad": "NDjamena",
    "Comoros": "Moroni",
    "Congo": "Brazzaville",
    "Djibouti": "Djibouti",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Mauritius",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Swaziland": "Mbabane",
    "Tanzania": "Dodoma",
    "Togo": "Lome",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare",
    
    # Add more countries and capitals as needed
}

def get_random_country_and_capital():
    country = random.choice(list(countries_and_capitals.keys()))
    capital = countries_and_capitals[country]
    return country, capital

def get_multiple_choice_options(correct_capital):
    options = [correct_capital]
    while len(options) < 4:
        random_capital = random.choice(list(countries_and_capitals.values()))
        if random_capital not in options:
            options.append(random_capital)
    random.shuffle(options)
    return options

def main():
    print("Welcome to the African Countries Capital Quiz!")
    print("You will be given the name of an African country and four options for its capital.")
    print("Try to choose the correct capital. Good luck!\n")

    score = 0
    number_of_questions = 5

    for _ in range(number_of_questions):
        country, correct_capital = get_random_country_and_capital()
        options = get_multiple_choice_options(correct_capital)

        print(f"What is the capital of {country}?")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        try:
            user_choice = int(input("Enter the number of your choice: "))
            if options[user_choice - 1] == correct_capital:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_capital}.\n")
        except (ValueError, IndexError):
            print(f"Invalid input. The correct answer is {correct_capital}.\n")

    print(f"Game over! Your final score is {score} out of {number_of_questions}.")

if __name__ == "__main__":
    main()
