def generate_signal_func(data):
    with open('../lib/signals/signals.cpp', 'w') as f:
        f.write('#include "signals.h"\n#include "buffer.h"\n\n')
        f.write(f"static constexpr float PRECISION{{0.1f}}; \n")
        f.write(f"static uint8_t buffer[14]{{0}};\n\n")

        for signal in data['signals']:
           if 'type' in signal and 'float' in signal['type']:
            f.write(f"bool signals_set_{signal['name']}({signal['type']} value)\n{{\n")
            f.write(f" \tbool status{{false}};\n")
            f.write(f" \tif(value>= {signal['range'][0]} && value<={signal['range'][1]})\n\t{{\n")
            f.write(f" \t\tstatus = true; \n")
            f.write(f" \t\tbuffer_insert(buffer, {signal['start']}, {signal['length']}, value/ PRECISION); \n\t}}\n")
            f.write(f" \treturn status; \n}}\n\n")
            f.write(f"{signal['type']} signals_get_{signal['name']}(void)\n{{\n")
            f.write(f" \treturn PRECISION * (buffer_extract(buffer, {signal['start']}, {signal['length']}));\n}}\n\n")
        
           elif 'values' in signal and 'states' in signal['values']:
            f.write(f"bool signals_set_{signal['name']}({signal['type']} value)\n{{\n")
            f.write(f" \tbool status{{false}};\n")
            f.write(f" \tif(value<= ON)\n\t{{\n")
            f.write(f" \t\tstatus = true;\n")
            f.write(f" \t\tbuffer_insert(buffer, {signal['start']}, {signal['length']}, value);\n\t}}\n")
            f.write(f" \treturn status; \n}}\n\n")
            f.write(f"{signal['type']} signals_get_{signal['name']}(void)\n{{\n")
            f.write(f" \treturn (buffer_extract(buffer, {signal['start']}, {signal['length']} ));\n}}\n\n")

           elif 'values' in signal and 'status' in signal['values']:
            f.write(f"bool signals_set_{signal['name']}({signal['type']} value)\n{{\n")
            f.write(f" \tbool status{{false}};\n")
            f.write(f" \tif(value<= OKAY)\n\t{{\n")
            f.write(f" \t\tstatus = true;\n")
            f.write(f" \t\tbuffer_insert(buffer, {signal['start']}, {signal['length']}, value);\n\t}}\n")
            f.write(f" \treturn status; \n}}\n\n")
            f.write(f"{signal['type']} signals_get_{signal['name']}(void)\n{{\n")
            f.write(f" \treturn (buffer_extract(buffer, {signal['start']}, {signal['length']} ));\n}}\n\n")
           elif signal['range'][0]==0:

            f.write(f"bool signals_set_{signal['name']}({signal['type']} value)\n{{\n")
            f.write(f" \tbool status{{false}};\n")
            f.write(f" \tif(value<={signal['range'][1]})\n\t{{\n")
            f.write(f" \t\tstatus = true; \n")
            f.write(f" \t\tbuffer_insert(buffer, {signal['start']}, {signal['length']}, value); \n\t}}\n")
            f.write(f" \treturn status; \n}}\n\n")
            f.write(f"{signal['type']} signals_get_{signal['name']}(void)\n{{\n")
            f.write(f" \treturn (buffer_extract(buffer, {signal['start']}, {signal['length']}));\n}}\n\n")

           else:
            f.write(f"bool signals_set_{signal['name']}({signal['type']} value)\n{{\n")
            f.write(f" \tbool status{{false}};\n")
            f.write(f" \tif(value>= {signal['range'][0]} && value<={signal['range'][1]})\n\t{{\n")
            f.write(f" \t\tstatus = true; \n")
            f.write(f" \t\tbuffer_insert(buffer, {signal['start']}, {signal['length']}, value); \n\t}}\n")
            f.write(f" \treturn status; \n}}\n\n")
            f.write(f"{signal['type']} signals_get_{signal['name']}(void)\n{{\n")
            f.write(f" \treturn (buffer_extract(buffer, {signal['start']}, {signal['length']}));\n}}\n\n")


        