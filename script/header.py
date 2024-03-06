def generate_prototypes(data):
    with open('../lib/signals/signals.h', 'w') as f:
        f.write("#ifndef SIGNALS_H\n#define SIGNALS_H\n\n")
        f.write("#include <stdint.h>\n\n")  # Include the necessary library
        for signal in data['signals']:
            f.write(f"/**\n * @brief This function is used to set {signal['comment']}\n *\n")
            f.write(f" * @param {signal['type']} value {signal['comment']} to set\n")
            if 'range' in signal:
                f.write(f" * @return True if {signal['comment']} is in the range of {signal['range']} otherwise false\n */\n")
            elif 'values' in signal:
                f.write(f" * @return True if {signal['comment']} is one of the {data['defines'][signal['values']]} values otherwise false\n */\n")
            f.write(f"uint8_t signals_set_{signal['name']}({signal['type']} value);\n\n")
            f.write(f"/**\n * @brief This function is used to get {signal['comment']}\n */\n")
            f.write(f"bool signals_get_{signal['name']}();\n\n")
        f.write("\n#endif // SIGNALS_H\n")