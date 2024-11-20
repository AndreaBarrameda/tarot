import random
import warnings
from ai import ai  # Assuming there's an 'ai' module available for interaction


import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)



# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# Define Major and Minor Arcana
major_arcana = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

minor_arcana_suits = {
    "Cups": ["Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups",
             "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
             "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups"],
    "Wands": ["Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands",
              "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands",
              "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands"],
    "Swords": ["Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords",
               "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
               "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords"],
    "Pentacles": ["Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles",
                  "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles",
                  "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"]
}

# Full deck of cards
deck = major_arcana + [card for suit in minor_arcana_suits.values() for card in suit]

# Function to shuffle and draw cards, with a chance of reversed cards
def draw_cards(num_cards):
    random.shuffle(deck)
    drawn_cards = []
    for _ in range(num_cards):
        card = random.choice(deck)
        is_reversed = random.choice([True, False])  # 50% chance to be reversed
        drawn_cards.append(f"{card} (reversed)" if is_reversed else card)
    return drawn_cards

# AI-powered tarot interpretation
def interpret_with_ai(cards, area_of_focus):
    system_prompt = (
        "Your clients are curious Gen Z seekers who crave mystical insight that feels authentic, accessible, and emotionally resonant. Speak to their emotional states and recent life events while remaining attuned to the cosmic undercurrents and astrology that may shape their questions. Your interpretations should empower, guide, and illuminate their next steps, balancing realism with a hint of the mystical unknown.When answering their questions, focus on: Clear, memorable insights that connect the cards to each other. A direct, logical answer tied explicitly to their question, with actionable advice.A glimpse into the future rooted in the spread's themes, offering clarity on timing or outcomes while including a touch of shadow work, self-growth, or alignment with their higher self.Make the experience quick and engaging, perfect for TikTok or snackable wisdom seekers, while leaving them with a sense of magic and self-awareness. Above all, make them feel seen, understood, and empowered to take their next step")
    #     "You are a tarot-reading witch—a mystical sage, a modern-day oracle attuned to synchronicities, cosmic influences, and the wisdom of Carl Jung. Interpret the cards with insight that is grounded yet magical, concise yet deep, speaking in a tone that’s intuitive, direct, and mysteriously relatable. Your aim is to be authentic, human, and wise, attuned to your client’s emotional states, astrology, and any recent life events that may color their questions. Your clients are mostly Gen Z, seekers who want mystical insight in a format that’s quick, snackable, and TikTok-friendly. Connect the cards to each other to tell a cohesive story that feels uniquely personal to them. Be insightful, accessible, and slightly mysterious—making them feel truly seen and guiding them toward self-awareness. Each interpretation should include: Concise, memorable insights grounded in mysticism and psychology. Short advice relevant to their situation, if they ask a specific question make sure to answer their question specifically also and with logic. A glimpse into the future drawn from the spread’s themes, make it direct and literal to their question with a note on growth, shadow work, or personal alignment."
    # )
    
    user_input = f"Interpret these cards: {str(cards)} focusing on the user's request: {area_of_focus}"

    # Assuming the ai function interacts with the AI model and returns a result
    interpretations = ai(system_prompt, user_input)['result']
    return str(f'\n{interpretations}')

# Interactive tarot reading session
def tarot_reading():
    print("\n🌌 Welcome to your Interactive Tarot Reading 🌌")
    print("🌟------------------------------------🌟")

    print("Please focus on your question or intention for the reading.")

    question = input("\nWhat would you like to ask the tarot cards? ")
    print("🌟------------------------------------🌟")
    print("\nYou asked:", f"'{question}'")
    try:
        num_cards = int(input("How many cards would you like to draw? (1-5): "))
        if num_cards not in range(1, 6):
            print("Drawing 3 cards as default since the input was out of range.")
            num_cards = 3
    except ValueError:
        print("Invalid input, drawing 3 cards by default.")
        num_cards = 3

    print("\n🃏 Shuffling and drawing your cards... 🃏\n")
    drawn_cards = draw_cards(num_cards)

    print("Your drawn cards are:")
    for card in drawn_cards:
        print(f"- {card}")

    # Get AI-based interpretation
    print("\n✨ Interpretations of your cards ✨")
    interpretations = interpret_with_ai(drawn_cards, question)
    print(interpretations)

    print("\nThank you for exploring the tarot. Reflect on your question and the guidance received.")
    print("Remember, the cards reveal possibilities, but you shape your own destiny. 🌠")

# Run the tarot reading session
tarot_reading()
