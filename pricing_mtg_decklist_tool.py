#Pulling Card Data from https://api.scryfall.com
import requests
from tqdm import tqdm
import re
import time

base_url = 'https://api.scryfall.com/cards'
total_card_prices = 0
file_path = r'C:\Users\Max\Documents\Development\Technical Development\Py-Development\sgt_john_benton_decklist.txt'
card_count = []
card_name = []
set_code = []
collector_number = []
foil_treatment = []
card_price_list = []
total_card_price_list = []
price_foil_usd = 0
price_usd = 0
text = ""
total_card_count = 0
cards_priced_count = 0


def main():
    slow_print("Decklist Loaded...")    

    with open(file_path, 'r') as deck_list:
        for card in deck_list:
            match = re.match(r'(\d+)\s+(.*?)\s+\((.*?)\)\s+(\d+)(?:\s*(\*Foil\*|\*F\*|\s*p)?)', card)   
            if match:
                card_count.append(int(match.group(1)))  
                card_name.append(match.group(2)) 
                set_code.append(match.group(3).lower())  
                collector_number.append(match.group(4)) 
                foil_treatment.append(match.group(5).strip() if match.group(5) else None) 
    total_card_count = len(card_name)
    slow_print("Retrieving Card Prices...")

    for card in range(len(card_name)):       
        url = base_url + '/' + set_code[card] + '/' + collector_number[card] + ''
        raw_data = requests.get(url).json()
        if 'prices' in raw_data:
            price_usd = raw_data['prices']['usd']
            price_foil_usd = raw_data['prices']['usd_foil']

            if(price_usd is None):
                if(price_foil_usd is None):
                    price_to_add = 0.0
            elif foil_treatment[card] == '*F*' or foil_treatment[card] == '*Foil*':
                price_to_add = price_foil_usd
            else:            
                price_to_add = price_usd
        card_price_list.append(price_to_add) 
        card_price = (float(price_to_add)*float(card_count[card])) 
        total_card_price_list.append(card_price) 
        global total_card_prices
        total_card_prices += card_price
        global cards_priced_count 
        cards_priced_count += 1
        progress_bar(cards_priced_count, total_card_count)     
    print_decklist()
        
def print_decklist():
    choice = input('Print Decklist? (Y/N): ')
    
    if choice.upper() == 'Y':
        for card in range(len(card_name)):
            print(f"{card_count[card]} {card_name[card]} ({set_code[card].upper()}) at ${float(card_price_list[card]):0.2f} equalling ${float(total_card_price_list[card]):0.2f}")
    print("")
    print(f"Total Deck Price: ${float(total_card_prices):.02f}")

def slow_print(text):
    for char in text:
        print(char, end = '', flush = True)   
        time.sleep(0.01)
    print()

def progress_bar(priced, total):
    percent = (priced / total) * 100
    if(percent < 100):
        print(f"\rCards Priced: {percent:.2f}%", end = '', flush = True) 
    else:
        print(f"\rCards Priced: {percent:.2f}%", flush = True) 


main()




