import json

# Load category and credit card input data
def load_data(category_file_path, credit_card_file_path):
    with open(category_file_path, 'r', encoding='utf-8') as category_file:
        category_data = json.load(category_file)
    
    with open(credit_card_file_path, 'r', encoding='utf-8') as credit_card_file:
        credit_card_data = json.load(credit_card_file)
    
    return category_data, credit_card_data

# Combine credit card benefits with category data
def combine_credit_card_categories(category_data, credit_card_data):
    # Create a mapping of kinds to category_id
    kinds_to_category = {}
    for category, details in category_data.items():
        for kind in details['kinds']:
            kinds_to_category[kind] = category

    # print(kinds_to_category)
    # Combine credit card data with category information
    combined_credit_card_data = []
    for card in credit_card_data:
        # Copy card data without 'benefit' key
        card_combined_data = {key: value for key, value in card.items() if key != 'benefit'}
        # card_combined_data = card.copy()
        card_combined_data['categories'] = []

        for benefit in card['benefit']:
            if benefit in kinds_to_category:
                category_id = kinds_to_category[benefit]
                if category_id not in card_combined_data['categories']:
                    card_combined_data['categories'].append(category_id)
        
        # Remove duplicate category ids
        card_combined_data['categories'] = list(set(card_combined_data['categories']))
        
        combined_credit_card_data.append(card_combined_data)
    
    return combined_credit_card_data

# Save combined data to a JSON file
def save_combined_data(combined_data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(combined_data, output_file, ensure_ascii=False, indent=4)

# Main function to run the script
def main():
    category_file_path = 'category_input.json'
    credit_card_file_path = 'check_card_input.json'
    output_file_path = 'combined_check_card_data.json'

    category_data, credit_card_data = load_data(category_file_path, credit_card_file_path)
    combined_data = combine_credit_card_categories(category_data, credit_card_data)
    save_combined_data(combined_data, output_file_path)

if __name__ == '__main__':
    main()
