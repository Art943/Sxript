def generate_signals_txt(data):
    with open('../lib/signals/signals.txt', 'w') as file:
        file.write(f"{'Signal':<35} | {'Type':<10} | {'Range/Values':<20} | {'Description'}\n")
        file.write('-' * 100 + '\n')
        for signal in data['signals']:
            name = signal['name']
            type_ = signal['type']
            range_values = signal.get('range', signal.get('values'))
            if isinstance(range_values, str):  
                range_values = ', '.join(data['defines'][range_values])
            else:
                range_values = str(range_values)
            description = signal['comment']
            file.write(f"{name:<35} | {type_:<10} | {range_values:<20} | {description}\n")
