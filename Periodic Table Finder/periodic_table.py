print("PERIODIC TABLE")
print(" ")

elements = [
    "HYDROGEN\n"
    "Atomic Mass: 1.0080 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: 1s^1\n"
    "Oxidation States: +1, -1\n"
    "Electronegativity (Pauling Scale): 2.2\n"
    "Atomic Radius (van der Waals): 120 pm\n"
    "Ionization Energy: 13.598 eV\n"
    "Electron Affinity: 0.754 eV\n"
    "Melting Point: 13.81 K\n"
    "Boiling Point: 20.28 K\n"
    "Density: 0.00008988 g/cm³\n"
    "Year Discovered: 1766"
    ,

    "HELIUM\n"
    "Atomic Mass: 4.00260 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: 1s^2\n"
    "Oxidation States: 0\n"
    "Atomic Radius (van der Waals): 140 pm\n"
    "Ionization Energy: 24.587 eV\n"
    "Melting Point: 0.95 K\n"
    "Boiling Point: 4.22 K\n"
    "Density: 0.0001785 g/cm³\n"
    "Year Discovered: 1868"

    ,

    "LITHIUM\n"
    "Atomic Mass: 7.0 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [He]2s1\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 0.98\n"
    "Atomic Radius (van der Waals): 182 pm\n"
    "Ionization Energy: 5.392 eV\n"
    "Electron Affinity: 0.618 eV\n"
    "Melting Point: 453.65 K\n"
    "Boiling Point: 1615 K\n"
    "Density: 0.534 g/cm³\n"
    "Year Discovered: 1817\n"

    ,

    "BERYLLIUM\n"
    "Atomic Mass: 9.012183 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [He]2s2\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 1.57\n"
    "Atomic Radius (van der Waals): 153 pm\n"
    "Ionization Energy: 9.323 eV\n"
    "Melting Point: 1560 K\n"
    "Boiling Point: 2744 K\n"
    "Density: 1.85 g/cm³\n"
    "Year Discovered: 1798\n"

    ,

    "BORON\n"
    "Atomic Mass: 10.81 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [He]2s22p1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 2.04\n"
    "Atomic Radius (van der Waals): 192 pm\n"
    "Ionization Energy: 8.298 eV\n"
    "Electron Affinity: 0.277 eV\n"
    "Melting Point: 2348 K\n"
    "Boiling Point: 4273 K\n"
    "Density: 2.37 g/cm³\n"
    "Year Discovered: 1808\n"

    ,

    "CARBON\n"
    "Atomic Mass: 12.011 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [He]2s22p2\n"
    "Oxidation States: +4, +2, -4\n"
    "Electronegativity (Pauling Scale): 2.55\n"
    "Atomic Radius (van der Waals): 170 pm\n"
    "Ionization Energy: 11.260 eV\n"
    "Electron Affinity: 1.263 eV\n"
    "Melting Point: 3823 K\n"
    "Boiling Point: 4098 K\n"
    "Density: 2.2670 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "NITROGEN\n"
    "Atomic Mass: 14.007 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [He]2s22p3\n"
    "Oxidation States: +5, +4, +3, +2, +1, -1, -2, -3\n"
    "Electronegativity (Pauling Scale): 3.04\n"
    "Atomic Radius (van der Waals): 155 pm\n"
    "Ionization Energy: 14.534 eV\n"
    "Melting Point: 63.15 K\n"
    "Boiling Point: 77.36 K\n"
    "Density: 0.0012506 g/cm³\n"
    "Year Discovered: 1772\n"

    ,

    "OXYGEN\n"
    "Atomic Mass: 15.999 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [He]2s22p4\n"
    "Oxidation States: -2\n"
    "Electronegativity (Pauling Scale): 3.44\n"
    "Atomic Radius (van der Waals): 152 pm\n"
    "Ionization Energy: 13.618 eV\n"
    "Electron Affinity: 1.461 eV\n"
    "Melting Point: 54.36 K\n"
    "Boiling Point: 90.2 K\n"
    "Density: 0.001429 g/cm³\n"
    "Year Discovered: 1774\n"

    ,

    "FLOURINE\n"
    "Atomic Mass: 18.99840316 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [He]2s22p5\n"
    "Oxidation States: -1\n"
    "Electronegativity (Pauling Scale): 3.98\n"
    "Atomic Radius (van der Waals): 135 pm\n"
    "Ionization Energy: 17.423 eV\n"
    "Electron Affinity: 3.339 eV\n"
    "Melting Point: 53.53 K\n"
    "Boiling Point: 85.03 K\n"
    "Density: 0.001696 g/cm³\n"
    "Year Discovered: 1670\n"

    ,

    "NEON\n"
    "Atomic Mass: 20.180 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [He]2s22p6\n"
    "Oxidation States: 0\n"
    "Atomic Radius (van der Waals): 154 pm\n"
    "Ionization Energy: 21.565 eV\n"
    "Melting Point: 24.56 K\n"
    "Boiling Point: 27.07 K\n"
    "Density: 0.0008999 g/cm³\n"
    "Year Discovered: 1898\n"

    ,

    "SODIUM\n"
    "Atomic Mass: 22.9897693 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s1\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 0.93\n"
    "Atomic Radius (van der Waals): 227 pm\n"
    "Ionization Energy: 5.139 eV\n"
    "Electron Affinity: 0.548 eV\n"
    "Melting Point: 370.95 K\n"
    "Boiling Point: 1156 K\n"
    "Density: 0.97 g/cm³\n"
    "Year Discovered: 1807\n"

    ,

    "MAGNESIUM\n"
    "Atomic Mass: 24.305 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s2\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 1.31\n"
    "Atomic Radius (van der Waals): 173 pm\n"
    "Ionization Energy: 7.646 eV\n"
    "Melting Point: 923 K\n"
    "Boiling Point: 1363 K\n"
    "Density: 1.74 g/cm³\n"
    "Year Discovered: 1808\n"

    ,

    "ALUMINUM\n"
    "Atomic Mass: 26.981538 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s23p1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.61\n"
    "Atomic Radius (van der Waals): 184 pm\n"
    "Ionization Energy: 5.986 eV\n"
    "Electron Affinity: 0.441 eV\n"
    "Melting Point: 933.437 K\n"
    "Boiling Point: 2792 K\n"
    "Density: 2.70 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "SILICON\n"
    "Atomic Mass: 28.085 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s23p2\n"
    "Oxidation States: +4, +2, -4\n"
    "Electronegativity (Pauling Scale): 1.9\n"
    "Atomic Radius (van der Waals): 210 pm\n"
    "Ionization Energy: 8.152 eV\n"
    "Electron Affinity: 1.385 eV\n"
    "Melting Point: 1687 K\n"
    "Boiling Point: 3538 K\n"
    "Density: 2.3296 g/cm³\n"
    "Year Discovered: 1854\n"

    ,

    "PHOSPHORUS\n"
    "Atomic Mass: 30.97376200 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s23p3\n"
    "Oxidation States: +5, +3, -3\n"
    "Electronegativity (Pauling Scale): 2.19\n"
    "Atomic Radius (van der Waals): 180 pm\n"
    "Ionization Energy: 10.487 eV\n"
    "Electron Affinity: 0.746 eV\n"
    "Melting Point: 317.3 K\n"
    "Boiling Point: 553.65 K\n"
    "Density: 1.82 g/cm³\n"
    "Year Discovered: 1669\n"

    ,

    "SULFUR\n"
    "Atomic Mass: 32.07 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ne]3s23p4\n"
    "Oxidation States: +6, +4, -2\n"
    "Electronegativity (Pauling Scale): 2.58\n"
    "Atomic Radius (van der Waals): 180 pm\n"
    "Ionization Energy: 10.360 eV\n"
    "Electron Affinity: 2.077 eV\n"
    "Melting Point: 388.36 K\n"
    "Boiling Point: 717.75 K\n"
    "Density: 2.067 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "CHLORINE\n"
    "Atomic Mass: 35.45 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [Ne]3s23p5\n"
    "Oxidation States: +7, +5, +1, -1\n"
    "Electronegativity (Pauling Scale): 3.16\n"
    "Atomic Radius (van der Waals): 175 pm\n"
    "Ionization Energy: 12.968 eV\n"
    "Electron Affinity: 3.617 eV\n"
    "Melting Point: 171.65 K\n"
    "Boiling Point: 239.11 K\n"
    "Density: 0.003214 g/cm³\n"
    "Year Discovered: 1774\n"

    ,

    "ARGON\n"
    "Atomic Mass: 39.9 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [Ne]3s23p6\n"
    "Oxidation States: 0\n"
    "Atomic Radius (van der Waals): 188 pm\n"
    "Ionization Energy: 15.760 eV\n"
    "Melting Point: 83.8 K\n"
    "Boiling Point: 87.3 K\n"
    "Density: 0.0017837 g/cm³\n"
    "Year Discovered: 1894\n"

    ,

    "POTASSIUM\n"
    "Atomic Mass: 39.0983 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s1\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 0.82\n"
    "Atomic Radius (van der Waals): 275 pm\n"
    "Ionization Energy: 4.341 eV\n"
    "Electron Affinity: 0.501 eV\n"
    "Melting Point: 336.53 K\n"
    "Boiling Point: 1032 K\n"
    "Density: 0.89 g/cm³\n"
    "Year Discovered: 1807\n"

    ,

    "CALCIUM\n"
    "Atomic Mass: 40.08 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s2\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 1\n"
    "Atomic Radius (van der Waals): 231 pm\n"
    "Ionization Energy: 6.113 eV\n"
    "Melting Point: 1115 K\n"
    "Boiling Point: 1757 K\n"
    "Density: 1.54 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "SCANDIUM\n"
    "Atomic Mass: 44.95591 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.36\n"
    "Atomic Radius (van der Waals): 211 pm\n"
    "Ionization Energy: 6.561 eV\n"
    "Electron Affinity: 0.188 eV\n"
    "Melting Point: 1814 K\n"
    "Boiling Point: 3109 K\n"
    "Density: 2.99 g/cm³\n"
    "Year Discovered: 1879\n"

    ,

    "TITANIUM\n"
    "Atomic Mass: 47.867 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d2\n"
    "Oxidation States: +4, +3, +2\n"
    "Electronegativity (Pauling Scale): 1.54\n"
    "Atomic Radius (van der Waals): 187 pm\n"
    "Ionization Energy: 6.828 eV\n"
    "Electron Affinity: 0.079 eV\n"
    "Melting Point: 1941 K\n"
    "Boiling Point: 3560 K\n"
    "Density: 4.5 g/cm³\n"
    "Year Discovered: 1791\n"

    ,

    "VANADAIUM\n"
    "Atomic Mass: 50.9415 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d3\n"
    "Oxidation States: +5, +4, +3, +2\n"
    "Electronegativity (Pauling Scale): 1.63\n"
    "Atomic Radius (van der Waals): 179 pm\n"
    "Ionization Energy: 6.746 eV\n"
    "Electron Affinity: 0.525 eV\n"
    "Melting Point: 2183 K\n"
    "Boiling Point: 3680 K\n"
    "Density: 6.0 g/cm³\n"
    "Year Discovered: 1801\n"

    ,

    "CHROMIUM\n"
    "Atomic Mass: 51.996 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]3d54s1\n"
    "Oxidation States: +6, +3, +2\n"
    "Electronegativity (Pauling Scale): 1.66\n"
    "Atomic Radius (van der Waals): 189 pm\n"
    "Ionization Energy: 6.767 eV\n"
    "Electron Affinity: 0.666 eV\n"
    "Melting Point: 2180 K\n"
    "Boiling Point: 2944 K\n"
    "Density: 7.15 g/cm³\n"
    "Year Discovered: 1797\n"

    ,

    "MANGANESE\n"
    "Atomic Mass: 54.93804 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d5\n"
    "Oxidation States: +7, +4, +3, +2\n"
    "Electronegativity (Pauling Scale): 1.55\n"
    "Atomic Radius (van der Waals): 197 pm\n"
    "Ionization Energy: 7.434 eV\n"
    "Melting Point: 1519 K\n"
    "Boiling Point: 2334 K\n"
    "Density: 7.3 g/cm³\n"
    "Year Discovered: 1774\n"

    ,

    "IRON\n"
    "Atomic Mass: 55.84 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d6\n"
    "Oxidation States: +3, +2\n"
    "Electronegativity (Pauling Scale): 1.83\n"
    "Atomic Radius (van der Waals): 194 pm\n"
    "Ionization Energy: 7.902 eV\n"
    "Electron Affinity: 0.163 eV\n"
    "Melting Point: 1811 K\n"
    "Boiling Point: 3134 K\n"
    "Density: 7.874 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "COBALT\n"
    "Atomic Mass: 58.93319 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d7\n"
    "Oxidation States: +3, +2\n"
    "Electronegativity (Pauling Scale): 1.88\n"
    "Atomic Radius (van der Waals): 192 pm\n"
    "Ionization Energy: 7.881 eV\n"
    "Electron Affinity: 0.661 eV\n"
    "Melting Point: 1768 K\n"
    "Boiling Point: 3200 K\n"
    "Density: 8.86 g/cm³\n"
    "Year Discovered: 1735\n"

    ,

    "NICKEL\n"
    "Atomic Mass: 58.693 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d8\n"
    "Oxidation States: +3, +2\n"
    "Electronegativity (Pauling Scale): 1.91\n"
    "Atomic Radius (van der Waals): 163 pm\n"
    "Ionization Energy: 7.640 eV\n"
    "Electron Affinity: 1.156 eV\n"
    "Melting Point: 1728 K\n"
    "Boiling Point: 3186 K\n"
    "Density: 8.912 g/cm³\n"
    "Year Discovered: 1751\n"

    ,

    "COPPER\n"
    "Atomic Mass: 63.55 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s13d10\n"
    "Oxidation States: +2, +1\n"
    "Electronegativity (Pauling Scale): 1.9\n"
    "Atomic Radius (van der Waals): 140 pm\n"
    "Ionization Energy: 7.726 eV\n"
    "Electron Affinity: 1.228 eV\n"
    "Melting Point: 1357.77 K\n"
    "Boiling Point: 2835 K\n"
    "Density: 8.933 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "ZINC\n"
    "Atomic Mass: 65.4 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d10\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 1.65\n"
    "Atomic Radius (van der Waals): 139 pm\n"
    "Ionization Energy: 9.394 eV\n"
    "Melting Point: 692.68 K\n"
    "Boiling Point: 1180 K\n"
    "Density: 7.134 g/cm³\n"
    "Year Discovered: 1746\n"
    
    ,

    "GALLIUM\n"
    "Atomic Mass: 69.723 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d104p1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.81\n"
    "Atomic Radius (van der Waals): 187 pm\n"
    "Ionization Energy: 5.999 eV\n"
    "Electron Affinity: 0.3 eV\n"
    "Melting Point: 302.91 K\n"
    "Boiling Point: 2477 K\n"
    "Density: 5.91 g/cm³\n"
    "Year Discovered: 1875\n"
    
    ,

    "GERMANIUM\n"
    "Atomic Mass: 72.63 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d104p2\n"
    "Oxidation States: +4, +2\n"
    "Electronegativity (Pauling Scale): 2.01\n"
    "Atomic Radius (van der Waals): 211 pm\n"
    "Ionization Energy: 7.900 eV\n"
    "Electron Affinity: 1.35 eV\n"
    "Melting Point: 1211.4 K\n"
    "Boiling Point: 3106 K\n"
    "Density: 5.323 g/cm³\n"
    "Year Discovered: 1886\n"
    
    ,

    "ARSENIC\n"
    "Atomic Mass: 74.92159 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d104p3\n"
    "Oxidation States: +5, +3, -3\n"
    "Electronegativity (Pauling Scale): 2.18\n"
    "Atomic Radius (van der Waals): 185 pm\n"
    "Ionization Energy: 9.815 eV\n"
    "Electron Affinity: 0.81 eV\n"
    "Melting Point: 1090 K\n"
    "Boiling Point: 887 K\n"
    "Density: 5.776 g/cm³\n"
    "Year Discovered: Ancient\n"
    
    ,

    "SELENIUM\n"
    "Atomic Mass: 78.97 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Ar]4s23d104p4\n"
    "Oxidation States: +6, +4, -2\n"
    "Electronegativity (Pauling Scale): 2.55\n"
    "Atomic Radius (van der Waals): 190 pm\n"
    "Ionization Energy: 9.752 eV\n"
    "Electron Affinity: 2.021 eV\n"
    "Melting Point: 493.65 K\n"
    "Boiling Point: 958 K\n"
    "Density: 4.809 g/cm³\n"
    "Year Discovered: 1817\n"
    
    ,

    "BROMINE\n"
    "Atomic Mass: 79.90 u\n"
    "Standard State: Liquid\n"
    "Electron Configuration: [Ar]4s23d104p5\n"
    "Oxidation States: +5, +1, -1\n"
    "Electronegativity (Pauling Scale): 2.96\n"
    "Atomic Radius (van der Waals): 183 pm\n"
    "Ionization Energy: 11.814 eV\n"
    "Electron Affinity: 3.365 eV\n"
    "Melting Point: 265.95 K\n"
    "Boiling Point: 331.95 K\n"
    "Density: 3.11 g/cm³\n"
    "Year Discovered: 1826\n"
    
    ,

    "KRYPTON\n"
    "Atomic Mass: 83.80 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [Ar]4s23d104p6\n"
    "Oxidation States: 0\n"
    "Electronegativity (Pauling Scale): 3\n"
    "Atomic Radius (van der Waals): 202 pm\n"
    "Ionization Energy: 14.000 eV\n"
    "Melting Point: 115.79 K\n"
    "Boiling Point: 119.93 K\n"
    "Density: 0.003733 g/cm³\n"
    "Year Discovered: 1898\n"
    
    ,

    "RUBIDIUM\n"
    "Atomic Mass: 85.468 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s1\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 0.82\n"
    "Atomic Radius (van der Waals): 303 pm\n"
    "Ionization Energy: 4.177 eV\n"
    "Electron Affinity: 0.468 eV\n"
    "Melting Point: 312.46 K\n"
    "Boiling Point: 961 K\n"
    "Density: 1.53 g/cm³\n"
    "Year Discovered: 1861\n"
    
    ,

    "STRONTIUM\n"
    "Atomic Mass: 87.62 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s2\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 0.95\n"
    "Atomic Radius (van der Waals): 249 pm\n"
    "Ionization Energy: 5.695 eV\n"
    "Melting Point: 1050 K\n"
    "Boiling Point: 1655 K\n"
    "Density: 2.64 g/cm³\n"
    "Year Discovered: 1790\n"
    
    ,

    "YTTRIUM\n"
    "Atomic Mass: 88.90584 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.22\n"
    "Atomic Radius (van der Waals): 219 pm\n"
    "Ionization Energy: 6.217 eV\n"
    "Electron Affinity: 0.307 eV\n"
    "Melting Point: 1795 K\n"
    "Boiling Point: 3618 K\n"
    "Density: 4.47 g/cm³\n"
    "Year Discovered: 1794\n"
    
    ,

    "ZIRCONIUM\n"
    "Atomic Mass: 91.22 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d2\n"
    "Oxidation States: +4\n"
    "Electronegativity (Pauling Scale): 1.33\n"
    "Atomic Radius (van der Waals): 186 pm\n"
    "Ionization Energy: 6.634 eV\n"
    "Electron Affinity: 0.426 eV\n"
    "Melting Point: 2128 K\n"
    "Boiling Point: 4682 K\n"
    "Density: 6.52 g/cm³\n"
    "Year Discovered: 1789\n"
    
    ,

    "NIOBIUM\n"
    "Atomic Mass: 92.90637 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s14d4\n"
    "Oxidation States: +5, +3\n"
    "Electronegativity (Pauling Scale): 1.6\n"
    "Atomic Radius (van der Waals): 207 pm\n"
    "Ionization Energy: 6.759 eV\n"
    "Electron Affinity: 0.893 eV\n"
    "Melting Point: 2750 K\n"
    "Boiling Point: 5017 K\n"
    "Density: 8.57 g/cm³\n"
    "Year Discovered: 1801\n"
    
    ,

    "MOLYBDENUM\n"
    "Atomic Mass: 95.95 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s14d5\n"
    "Oxidation States: +6\n"
    "Electronegativity (Pauling Scale): 2.16\n"
    "Atomic Radius (van der Waals): 209 pm\n"
    "Ionization Energy: 7.092 eV\n"
    "Electron Affinity: 0.746 eV\n"
    "Melting Point: 2896 K\n"
    "Boiling Point: 4912 K\n"
    "Density: 10.2 g/cm³\n"
    "Year Discovered: 1778\n"
    
    ,

    "TECHNETIUM\n"
    "Atomic Mass: 96.90636 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d5\n"
    "Oxidation States: +7, +6, +4\n"
    "Electronegativity (Pauling Scale): 1.9\n"
    "Atomic Radius (van der Waals): 209 pm\n"
    "Ionization Energy: 7.28 eV\n"
    "Electron Affinity: 0.55 eV\n"
    "Melting Point: 2430 K\n"
    "Boiling Point: 4538 K\n"
    "Density: 11 g/cm³\n"
    "Year Discovered: 1937\n"

    ,

    "RUTHENIUM\n"
    "Atomic Mass: 101.1 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s14d7\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 2.2\n"
    "Atomic Radius (van der Waals): 207 pm\n"
    "Ionization Energy: 7.361 eV\n"
    "Electron Affinity: 1.05 eV\n"
    "Melting Point:	2607 K\n"
    "Boiling Point: 4423 K\n"
    "Density: 12.1 g/cm³\n"
    "Year Discovered: 1827\n"

    ,

    "RHODIUM\n"
    "Atomic Mass: 102.9055 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s14d8\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 2.28\n"
    "Atomic Radius (van der Waals): 195 pm\n"
    "Ionization Energy: 7.459 eV\n"
    "Electron Affinity: 1.137 eV\n"
    "Melting Point:	2237 K\n"
    "Boiling Point: 3968 K\n"
    "Density: 12.4 g/cm³\n"
    "Year Discovered: 1803\n"

    ,

    "PALLADIUM\n"
    "Atomic Mass: 106.42 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]4d10\n"
    "Oxidation States: +3, +2\n"
    "Electronegativity (Pauling Scale): 2.2\n"
    "Atomic Radius (van der Waals): 202 pm\n"
    "Ionization Energy: 8.337 eV\n"
    "Electron Affinity: 0.557 eV\n"
    "Melting Point:	1828.05 K\n"
    "Boiling Point: 3236 K\n"
    "Density: 12.0 g/cm³\n"
    "Year Discovered: 1803\n"

    ,

    "SILVER\n"
    "Atomic Mass: 107.868 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s14d10\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 1.93\n"
    "Atomic Radius (van der Waals): 172 pm\n"
    "Ionization Energy: 7.576 eV\n"
    "Electron Affinity: 1.302 eV\n"
    "Melting Point:	1234.93 K\n"
    "Boiling Point: 2435 K\n"
    "Density: 10.501 g/cm³\n"
    "Year Discovered: Ancient\n"
    ,

    "CADMIUM\n"
    "Atomic Mass: 112.41 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d10\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 1.69\n"
    "Atomic Radius (van der Waals): 158 pm\n"
    "Ionization Energy: 8.994 eV\n"
    "Melting Point:	594.22 K\n"
    "Boiling Point: 1040 K\n"
    "Density: 8.69 g/cm³\n"
    "Year Discovered: 1817\n"

    ,

    "INDIUM\n"
    "Atomic Mass: 114.818 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d105p1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.78\n"
    "Atomic Radius (van der Waals): 193 pm\n"
    "Ionization Energy: 5.786 eV\n"
    "Electron Affinity: 0.3 eV\n"
    "Melting Point:	429.75 K\n"
    "Boiling Point: 2345 K\n"
    "Density: 7.31 g/cm³\n"
    "Year Discovered: 1863\n"

    ,

    "TIN\n"
    "Atomic Mass: 118.71 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d105p2\n"
    "Oxidation States: +4, +2\n"
    "Electronegativity (Pauling Scale): 1.96\n"
    "Atomic Radius (van der Waals): 217 pm\n"
    "Ionization Energy: 7.344 eV\n"
    "Electron Affinity: 1.2 eV\n"
    "Melting Point:	505.08 K\n"
    "Boiling Point: 2875 K\n"
    "Density: 7.287 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "ANTIMONY\n"
    "Atomic Mass: 121.760 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d105p3\n"
    "Oxidation States: +5, +3, -3\n"
    "Electronegativity (Pauling Scale): 2.05\n"
    "Atomic Radius (van der Waals): 206 pm\n"
    "Ionization Energy: 8.64 eV\n"
    "Electron Affinity: 1.07 eV\n"
    "Melting Point:	903.78 K\n"
    "Boiling Point: 1860 K\n"
    "Density: 6.685 g/cm³\n"
    "Year Discovered: Ancient\n"

    ,

    "TELLURIUM\n"
    "Atomic Mass: 127.6 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d105p4\n"
    "Oxidation States: +6, +4, -2\n"
    "Electronegativity (Pauling Scale): 2.1\n"
    "Atomic Radius (van der Waals): 206 pm\n"
    "Ionization Energy: 9.010 eV\n"
    "Electron Affinity: 1.971 eV\n"
    "Melting Point:	722.66 K\n"
    "Boiling Point: 1261 K\n"
    "Density: 6.232 g/cm³\n"
    "Year Discovered: 1782\n"

    ,

    "IODINE\n"
    "Atomic Mass: 126.9045 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Kr]5s24d105p5\n"
    "Oxidation States: +7, +5, +1, -1\n"
    "Electronegativity (Pauling Scale): 2.66\n"
    "Atomic Radius (van der Waals): 198 pm\n"
    "Ionization Energy: 10.451 eV\n"
    "Electron Affinity: 3.059 eV\n"
    "Melting Point:	386.85 K\n"
    "Boiling Point: 457.55 K\n"
    "Density: 4.93 g/cm³\n"
    "Year Discovered: 1811\n"

    ,

    "XENON\n"
    "Atomic Mass: 131.29 u\n"
    "Standard State: Gas\n"
    "Electron Configuration: [Kr]5s24d105p6\n"
    "Oxidation States: 0\n"
    "Electronegativity (Pauling Scale): 2.6\n"
    "Atomic Radius (van der Waals): 216 pm\n"
    "Ionization Energy: 12.130 eV\n"
    "Melting Point:	161.36 K\n"
    "Boiling Point: 165.03 K\n"
    "Density: 0.005887 g/cm³\n"
    "Year Discovered: 1898\n"

    ,

    "CESIUM\n"
    "Atomic Mass: 132.9054520 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Xe]6s1\n"
    "Oxidation States: +1\n"
    "Electronegativity (Pauling Scale): 0.79\n"
    "Atomic Radius (van der Waals): 343 pm\n"
    "Ionization Energy: 3.894 eV\n"
    "Electron Affinity: 0.472 eV\n"
    "Melting Point:	301.59 K\n"
    "Boiling Point: 944 K\n"
    "Density: 1.93 g/cm³\n"
    "Year Discovered: 1860\n"

    ,

    "BARIUM\n"
    "Atomic Mass: 137.33 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Xe]6s2\n"
    "Oxidation States: +2\n"
    "Electronegativity (Pauling Scale): 0.89\n"
    "Atomic Radius (van der Waals): 268 pm\n"
    "Ionization Energy: 5.212 eV\n"
    "Melting Point:	1000 K\n"
    "Boiling Point: 2170 K\n"
    "Density: 3.62 g/cm³\n"
    "Year Discovered: 1808\n"

    ,

    "LANTHANUM\n"
    "Atomic Mass: 138.9055 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Xe]6s25d1\n"
    "Oxidation States: +3\n"
    "Electronegativity (Pauling Scale): 1.1\n"
    "Atomic Radius (van der Waals): 240 pm\n"
    "Ionization Energy: 5.577 eV\n"
    "Electron Affinity: 0.5 eV\n"
    "Melting Point:	1191 K\n"
    "Boiling Point: 3737 K\n"
    "Density: 6.15 g/cm³\n"
    "Year Discovered: 1839\n"

    ,

    "CERIUM\n"
    "Atomic Mass: 140.116 u\n"
    "Standard State: Solid\n"
    "Electron Configuration: [Xe]6s24f15d1\n"
    "Oxidation States: +4, +3\n"
    "Electronegativity (Pauling Scale): 1.12\n"
    "Atomic Radius (van der Waals): 235 pm\n"
    "Ionization Energy: 5.539 eV\n"
    "Electron Affinity: 0.5 eV\n"
    "Melting Point:	1071 K\n"
    "Boiling Point: 3697 K\n"
    "Density: 6.770 g/cm³\n"
    "Year Discovered: 1803\n"

    ,

    "PRASEODYMIUM\n"
"Atomic Mass: 140.91 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f3 6s2\n"
"Oxidation States: +3, +4\n"
"Electronegativity (Pauling Scale): 1.13\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.464 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1204 K\n"
"Boiling Point: 3793 K\n"
"Density: 6.77 g/cm^3\n"
"Year Discovered: 1885\n"

,

"NEODYMIUM\n"
"Atomic Mass: 144.24 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f4 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.14\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.525 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1294 K\n"
"Boiling Point: 3347 K\n"
"Density: 7.00 g/cm^3\n"
"Year Discovered: 1885\n"

,


"PROMETHIUM\n"
"Atomic Mass: 145 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f5 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.13\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.55 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1315 K\n"
"Boiling Point: 3273 K\n"
"Density: N/A\n"
"Year Discovered: 1945\n"

,


"SAMARIUM\n"
"Atomic Mass: 150.36 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f6 6s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.17\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.643 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1345 K\n"
"Boiling Point: 2067 K\n"
"Density: 7.52 g/cm^3\n"
"Year Discovered: 1879\n"

,


"EUROPIUM\n"
"Atomic Mass: 151.96 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f7 6s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.67 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1099 K\n"
"Boiling Point: 1802 K\n"
"Density: 5.24 g/cm^3\n"
"Year Discovered: 1901\n"

,


"GADOLINIUM\n"
"Atomic Mass: 157.25 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f7 5d1 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.15 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1586 K\n"
"Boiling Point: 3546 K\n"
"Density: 7.90 g/cm^3\n"
"Year Discovered: 1880\n"

,


"TERBIUM\n"
"Atomic Mass: 158.93 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f9 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.863 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1629 K\n"
"Boiling Point: 3503 K\n"
"Density: 8.23 g/cm^3\n"
"Year Discovered: 1843\n"

,


"DYSPROSIUM\n"
"Atomic Mass: 162.50 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f10 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.22\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.939 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1680 K\n"
"Boiling Point: 2840 K\n"
"Density: 8.55 g/cm^3\n"
"Year Discovered: 1886\n"

,


"HOLMIUM\n"
"Atomic Mass: 164.93 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f11 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.23\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.021 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1747 K\n"
"Boiling Point: 2973 K\n"
"Density: 8.80 g/cm^3\n"
"Year Discovered: 1878\n"

,


"ERBIUM\n"
"Atomic Mass: 167.26 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f12 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.24\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.108 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1802 K\n"
"Boiling Point: 3141 K\n"
"Density: 9.07 g/cm^3\n"
"Year Discovered: 1842\n"

,

"THULIUM\n"
"Atomic Mass: 168.93 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f13 6s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.25\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.184 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1818 K\n"
"Boiling Point: 2223 K\n"
"Density: 9.32 g/cm^3\n"
"Year Discovered: 1879\n"

,


"YTTERBIUM\n"
"Atomic Mass: 173.05 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 6s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.1\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.254 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1097 K\n"
"Boiling Point: 1469 K\n"
"Density: 6.97 g/cm^3\n"
"Year Discovered: 1878\n"

,


"LUTETIUM\n"
"Atomic Mass: 174.97 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d1 6s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.27\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.425 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1925 K\n"
"Boiling Point: 3675 K\n"
"Density: 9.84 g/cm^3\n"
"Year Discovered: 1907\n"

,


"HAFNIUM\n"
"Atomic Mass: 178.49 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d2 6s2\n"
"Oxidation States: +2, +3, +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.825 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 2506 K\n"
"Boiling Point: 4876 K\n"
"Density: 13.31 g/cm^3\n"
"Year Discovered: 1923\n"

,


"TANTALUM\n"
"Atomic Mass: 180.95 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d3 6s2\n"
"Oxidation States: -1, +1, +3, +4, +5\n"
"Electronegativity (Pauling Scale): 1.5\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 7.549 eV\n"
"Electron Affinity: 0.322 eV\n"
"Melting Point: 3290 K\n"
"Boiling Point: 5731 K\n"
"Density: 16.65 g/cm^3\n"
"Year Discovered: 1802\n"

,


"TUNGSTEN\n"
"Atomic Mass: 183.84 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d4 6s2\n"
"Oxidation States: -2, -1, +1, +2, +3, +4, +5, +6\n"
"Electronegativity (Pauling Scale): 2.36\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 7.864 eV\n"
"Electron Affinity: 0.815 eV\n"
"Melting Point: 3695 K\n"
"Boiling Point: 5828 K\n"
"Density: 19.25 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"RHENIUM\n"
"Atomic Mass: 186.21 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d5 6s2\n"
"Oxidation States: -3, -1, +1, +2, +3, +4, +5, +6, +7\n"
"Electronegativity (Pauling Scale): 1.9\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 7.833 eV\n"
"Electron Affinity: 0.15 eV\n"
"Melting Point: 3459 K\n"
"Boiling Point: 5869 K\n"
"Density: 21.02 g/cm^3\n"
"Year Discovered: 1925\n"

,

"OSMIUM\n"
"Atomic Mass: 190.23 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d6 6s2\n"
"Oxidation States: -2, -1, +1, +2, +3, +4, +5, +6, +7, +8\n"
"Electronegativity (Pauling Scale): 2.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 8.438 eV\n"
"Electron Affinity: 1.077 eV\n"
"Melting Point: 3306 K\n"
"Boiling Point: 5285 K\n"
"Density: 22.59 g/cm^3\n"
"Year Discovered: 1803\n"

,

"IRIDIUM\n"
"Atomic Mass: 192.22 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d7 6s2\n"
"Oxidation States: -3, -1, +1, +2, +3, +4, +5, +6\n"
"Electronegativity (Pauling Scale): 2.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 8.967 eV\n"
"Electron Affinity: 1.564 eV\n"
"Melting Point: 2719 K\n"
"Boiling Point: 4701 K\n"
"Density: 22.56 g/cm^3\n"
"Year Discovered: 1803\n"

,

"PLATINUM\n"
"Atomic Mass: 195.08 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d9 6s1\n"
"Oxidation States: +2, +4\n"
"Electronegativity (Pauling Scale): 2.28\n"
"Atomic Radius (van der Waals): 175 pm\n"
"Ionization Energy: 8.958 eV\n"
"Electron Affinity: 2.128 eV\n"
"Melting Point: 2041.4 K\n"
"Boiling Point: 4098 K\n"
"Density: 21.45 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"GOLD\n"
"Atomic Mass: 196.97 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s1\n"
"Oxidation States: -1, +1, +3, +5\n"
"Electronegativity (Pauling Scale): 2.54\n"
"Atomic Radius (van der Waals): 166 pm\n"
"Ionization Energy: 9.225 eV\n"
"Electron Affinity: 2.308 eV\n"
"Melting Point: 1337.33 K\n"
"Boiling Point: 3129 K\n"
"Density: 19.32 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"MERCURY\n"
"Atomic Mass: 200.59 u\n"
"Standard State: Liquid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2\n"
"Oxidation States: +1, +2\n"
"Electronegativity (Pauling Scale): 2.00\n"
"Atomic Radius (van der Waals): 155 pm\n"
"Ionization Energy: 10.437 eV\n"
"Electron Affinity: 0 eV\n"
"Melting Point: 234.32 K\n"
"Boiling Point: 629.88 K\n"
"Density: 13.55 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"THALLIUM\n"
"Atomic Mass: 204.38 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p1\n"
"Oxidation States: +1, +3\n"
"Electronegativity (Pauling Scale): 1.62\n"
"Atomic Radius (van der Waals): 196 pm\n"
"Ionization Energy: 6.108 eV\n"
"Electron Affinity: 0.2 eV\n"
"Melting Point: 577 K\n"
"Boiling Point: 1746 K\n"
"Density: 11.85 g/cm^3\n"
"Year Discovered: 1861\n"

,

"LEAD\n"
"Atomic Mass: 207.2 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p2\n"
"Oxidation States: -4, -2, +2, +4\n"
"Electronegativity (Pauling Scale): 2.33\n"
"Atomic Radius (van der Waals): 202 pm\n"
"Ionization Energy: 7.416 eV\n"
"Electron Affinity: 0.364 eV\n"
"Melting Point: 600.61 K\n"
"Boiling Point: 2022 K\n"
"Density: 11.34 g/cm^3\n"
"Year Discovered: Ancient\n"


,

"BISMUTH\n"
"Atomic Mass: 208.98 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p3\n"
"Oxidation States: -3, +3, +5\n"
"Electronegativity (Pauling Scale): 2.02\n"
"Atomic Radius (van der Waals): 207 pm\n"
"Ionization Energy: 7.285 eV\n"
"Electron Affinity: 0.942 eV\n"
"Melting Point: 544.4 K\n"
"Boiling Point: 1837 K\n"
"Density: 9.78 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"POLONIUM\n"
"Atomic Mass: 209 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p4\n"
"Oxidation States: +2, +4, +6\n"
"Electronegativity (Pauling Scale): 2.0\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 8.417 eV\n"
"Electron Affinity: 1.9 eV\n"
"Melting Point: 527 K\n"
"Boiling Point: 1235 K\n"
"Density: 9.2 g/cm^3\n"
"Year Discovered: 1898\n"

,

"ASTATINE\n"
"Atomic Mass: 210 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p5\n"
"Oxidation States: -1, +1, +3, +5, +7\n"
"Electronegativity (Pauling Scale): 2.2\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 9.3 eV\n"
"Electron Affinity: 2.8 eV\n"
"Melting Point: 575 K\n"
"Boiling Point: 610 K\n"
"Density: N/A\n"
"Year Discovered: 1940\n"

,

"RADON\n"
"Atomic Mass: 222 u\n"
"Standard State: Gas\n"
"Electron Configuration: [Xe]4f14 5d10 6s2 6p6\n"
"Oxidation States: +2\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): 220 pm\n"
"Ionization Energy: 10.748 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 202 K\n"
"Boiling Point: 211.5 K\n"
"Density: 0.00973 g/cm^3\n"
"Year Discovered: 1900\n"

,

"FRANCIUM\n"
"Atomic Mass: 223 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]7s1\n"
"Oxidation States: +1\n"
"Electronegativity (Pauling Scale): 0.7\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 4.072 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 300 K\n"
"Boiling Point: 950 K\n"
"Density: N/A\n"
"Year Discovered: 1939\n"

,

"RADIUM\n"
"Atomic Mass: 226 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]7s2\n"
"Oxidation States: +2\n"
"Electronegativity (Pauling Scale): 0.9\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.279 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 973 K\n"
"Boiling Point: 2010 K\n"
"Density: 5 g/cm^3\n"
"Year Discovered: 1898\n"

,

"ACTINIUM\n"
"Atomic Mass: 227 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]6d1 7s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.1\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.17 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1323 K\n"
"Boiling Point: 3471 K\n"
"Density: 10.07 g/cm^3\n"
"Year Discovered: 1899\n"

,

"THORIUM\n"
"Atomic Mass: 232.04 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]6d2 7s2\n"
"Oxidation States: +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.08 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 2023 K\n"
"Boiling Point: 5093 K\n"
"Density: 11.72 g/cm^3\n"
"Year Discovered: 1829\n"

,

"PROTACTINIUM\n"
"Atomic Mass: 231.04 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f2 6d1 7s2\n"
"Oxidation States: +5\n"
"Electronegativity (Pauling Scale): 1.5\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.89 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1841 K\n"
"Boiling Point: 4300 K\n"
"Density: 15.37 g/cm^3\n"
"Year Discovered: 1913\n"

,

"URANIUM\n"
"Atomic Mass: 238.03 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f3 6d1 7s2\n"
"Oxidation States: +3, +4, +5, +6\n"
"Electronegativity (Pauling Scale): 1.38\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.19 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1405.3 K\n"
"Boiling Point: 4404 K\n"
"Density: 19.05 g/cm^3\n"
"Year Discovered: Ancient\n"

,

"NEPTUNIUM\n"
"Atomic Mass: 237 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f4 6d1 7s2\n"
"Oxidation States: +3, +4, +5, +6, +7\n"
"Electronegativity (Pauling Scale): 1.36\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.27 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 917 K\n"
"Boiling Point: 4175 K\n"
"Density: 20.45 g/cm^3\n"
"Year Discovered: 1940\n"

,

"PLUTONIUM\n"
"Atomic Mass: 244 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f6 7s2\n"
"Oxidation States: +3, +4, +5, +6, +7\n"
"Electronegativity (Pauling Scale): 1.28\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.03 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 913 K\n"
"Boiling Point: 3505 K\n"
"Density: 19.86 g/cm^3\n"
"Year Discovered: 1940\n"

,

"AMERICIUM\n"
"Atomic Mass: 243 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f7 7s2\n"
"Oxidation States: +2, +3, +4, +5, +6\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.97 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1449 K\n"
"Boiling Point: 2880 K\n"
"Density: 13.67 g/cm^3\n"
"Year Discovered: 1944\n"

,

"CURIUM\n"
"Atomic Mass: 247 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f7 6d1 7s2\n"
"Oxidation States: +3, +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 5.99 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1613 K\n"
"Boiling Point: 3383 K\n"
"Density: 13.51 g/cm^3\n"
"Year Discovered: 1944\n"

,

"BERKELIUM\n"
"Atomic Mass: 247 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f9 7s2\n"
"Oxidation States: +3, +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.23 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1259 K\n"
"Boiling Point: N/A\n"
"Density: 14.79 g/cm^3\n"
"Year Discovered: 1949\n"

,

"CALIFORNIUM\n"
"Atomic Mass: 251 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f10 7s2\n"
"Oxidation States: +2, +3, +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.3 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1173 K\n"
"Boiling Point: N/A\n"
"Density: 15.1 g/cm^3\n"
"Year Discovered: 1950\n"

,

"EINSTEINIUM\n"
"Atomic Mass: 252 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f11 7s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.42 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1133 K\n"
"Boiling Point: N/A\n"
"Density: 8.84 g/cm^3\n"
"Year Discovered: 1952\n"

,

"FERMIUM\n"
"Atomic Mass: 257 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f12 7s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.5 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1800 K\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1952\n"

,

"MENDELEVIUM\n"
"Atomic Mass: 258 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f13 7s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.58 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1100 K\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1955\n"

,

"NOBELIUM\n"
"Atomic Mass: 259 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f14 7s2\n"
"Oxidation States: +2, +3\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6.65 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1100 K\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1957\n"

,

"LAWRENCIUM\n"
"Atomic Mass: 266 u\n"
"Standard State: Solid\n"
"Electron Configuration: [Rn]5f14 6d1 7s2\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 4.9 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: 1900 K\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1961\n"

,

"RUTHERFORDIUM\n"
"Atomic Mass: 267 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d2 7s2\n"
"Oxidation States: +4\n"
"Electronegativity (Pauling Scale): 1.3\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: 6 eV\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1969\n"

,

"DUBNIUM\n"
"Atomic Mass: 268 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d3 7s2\n"
"Oxidation States: +5, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1969\n"

,

"SEABORGIUM\n"
"Atomic Mass: 271 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d4 7s2\n"
"Oxidation States: +6, +5, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1974\n"

,

"BOHRIUM\n"
"Atomic Mass: 270 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d5 7s2\n"
"Oxidation States: +7, +6, +5, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1976\n"

,

"HASSIUM\n"
"Atomic Mass: 269 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d6 7s2\n"
"Oxidation States: +8, +6, +5, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1984\n"

,

"MEITNERIUM\n"
"Atomic Mass: 278 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d7 7s2\n"
"Oxidation States: +9, +8, +6, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1982\n"

,

"DARMSTADTIUM\n"
"Atomic Mass: 281 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d9 7s1\n"
"Oxidation States: +8, +6, +4, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1994\n"

,

"ROENTGENIUM\n"
"Atomic Mass: 282 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s1\n"
"Oxidation States: +7, +5, +3, +1\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1994\n"

,

"COPERNICIUM\n"
"Atomic Mass: 285 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2\n"
"Oxidation States: +2, +4\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1996\n"

,

"NIHONIUM\n"
"Atomic Mass: 286 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p1\n"
"Oxidation States: +1, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 2004\n"

,

"FLEROVIUM\n"
"Atomic Mass: 289 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p2\n"
"Oxidation States: +2\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 1999\n"

,

"MOSCOVIUM\n"
"Atomic Mass: 290 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p3\n"
"Oxidation States: +1, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 2003\n"

,

"LIVERMORIUM\n"
"Atomic Mass: 293 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p4\n"
"Oxidation States: +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 2000\n"

,

"TENNESSINE\n"
"Atomic Mass: 294 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p5\n"
"Oxidation States: +1, +3\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 2010\n"

,

"OGANESSON\n"
"Atomic Mass: 294 u\n"
"Standard State: Synthetic\n"
"Electron Configuration: [Rn]5f14 6d10 7s2 7p6\n"
"Oxidation States: +2, +4, +6, +8\n"
"Electronegativity (Pauling Scale): N/A\n"
"Atomic Radius (van der Waals): N/A\n"
"Ionization Energy: N/A\n"
"Electron Affinity: N/A\n"
"Melting Point: N/A\n"
"Boiling Point: N/A\n"
"Density: N/A\n"
"Year Discovered: 2002\n"

]

def print_element_properties(index):
    element = elements[index]
    for line in element.split('\n'):
        print(line)
    

while True:
    print(" ")
    print("Enter 'Q' to Exit")
    property = input("Enter Element Property: ").capitalize()
    print(" ")

    if property == "Q":
        print("Exiting...")
        print(" ")
        break
    elif property == "Hydrogen" or property == "H" or property == "1":
        print_element_properties(0)
    elif property == "Helium" or property == "He" or property == "2":
        print_element_properties(1)
    elif property == "Lithium" or property == "L" or property == "3":
        print_element_properties(2)
    elif property == "Beryllium" or property == "Be" or property == "4":
        print_element_properties(3)
    elif property == "Boron" or property == "B" or property == "5":
        print_element_properties(4)
    elif property == "Carbon" or property == "C" or property == "6":
        print_element_properties(5)
    elif property == "Nitrogen" or property == "N" or property == "7":
        print_element_properties(6)
    elif property == "Oxygen" or property == "O" or property == "8":
        print_element_properties(7)
    elif property == "Flourine" or property == "F" or property == "9":
        print_element_properties(8)
    elif property == "Neon" or property == "Ne" or property == "10":
        print_element_properties(9)
    elif property == "Sodium" or property == "Na" or property == "11":
        print_element_properties(10)
    elif property == "Magnesium" or property == "Mg" or property == "12":
        print_element_properties(11)
    elif property == "Aluminum" or property == "Al" or property == "13":
        print_element_properties(12)
    elif property == "Silicon" or property == "Si" or property == "14":
        print_element_properties(13)
    elif property == "Phosphorus" or property == "P" or property == "15":
        print_element_properties(14)
    elif property == "Sulfur" or property == "S" or property == "16":
        print_element_properties(15)
    elif property == "Chlorine" or property == "Cl" or property == "17":
        print_element_properties(16)
    elif property == "Argon" or property == "Ar" or property == "18":
        print_element_properties(17)
    elif property == "Potassium" or property == "K" or property == "19":
        print_element_properties(18)
    elif property == "Calcium" or property == "Ca" or property == "20":
        print_element_properties(19)
    elif property == "Scandium" or property == "Sc" or property == "21":
        print_element_properties(20)
    elif property == "Titanium" or property == "Ti" or property == "22":
        print_element_properties(21)
    elif property == "Vanadium" or property == "V" or property == "23":
        print_element_properties(22)
    elif property == "Chromium" or property == "Cr" or property == "24":
        print_element_properties(23)
    elif property == "Manganese" or property == "Mn" or property == "25":
        print_element_properties(24)
    elif property == "Iron" or property == "Fe" or property == "26":
        print_element_properties(25)
    elif property == "Cobalt" or property == "Co" or property == "27":
        print_element_properties(26)
    elif property == "Nickel" or property == "Ni" or property == "28":
        print_element_properties(27)
    elif property == "Copper" or property == "Cu" or property == "29":
        print_element_properties(28)
    elif property == "Zinc" or property == "Zn" or property == "30":
        print_element_properties(29)
    elif property == "Gallium" or property == "Ga" or property == "31":
        print_element_properties(30)
    elif property == "Germanium" or property == "Ge" or property == "32":
        print_element_properties(31)
    elif property == "Arsenic" or property == "As" or property == "33":
        print_element_properties(32)
    elif property == "Selenium" or property == "Se" or property == "34":
        print_element_properties(33)
    elif property == "Bromine" or property == "Br" or property == "35":
        print_element_properties(34)
    elif property == "Krypton" or property == "Kr" or property == "36":
        print_element_properties(35)
    elif property == "Rubidium" or property == "Rb" or property == "37":
        print_element_properties(36)
    elif property == "Strontium" or property == "Sr" or property == "38":
        print_element_properties(37)
    elif property == "Yttrium" or property == "Y" or property == "39":
        print_element_properties(38)
    elif property == "Zirconium" or property == "Zr" or property == "40":
        print_element_properties(39)
    elif property == "Niobium" or property == "Nb" or property == "41":
        print_element_properties(40)
    elif property == "Molybdenum" or property == "Mo" or property == "42":
        print_element_properties(41)
    elif property == "Technetium" or property == "Tc" or property == "43":
        print_element_properties(42)
    elif property == "Ruthenium" or property == "Ru" or property == "44":
        print_element_properties(43)
    elif property == "Rhodium" or property == "Rh" or property == "45":
        print_element_properties(44)
    elif property == "Palladium" or property == "Pd" or property == "46":
        print_element_properties(45)
    elif property == "Silver" or property == "Ag" or property == "47":
        print_element_properties(46)
    elif property == "Cadmium" or property == "Cd" or property == "48":
        print_element_properties(47)
    elif property == "Indium" or property == "In" or property == "49":
        print_element_properties(48)
    elif property == "Tin" or property == "Sn" or property == "50":
        print_element_properties(49)
    elif property == "Antimony" or property == "Sb" or property == "51":
        print_element_properties(50)
    elif property == "Tellurium" or property == "Te" or property == "52":
        print_element_properties(51)
    elif property == "Iodine" or property == "I" or property == "53":
        print_element_properties(52)
    elif property == "Xenon" or property == "Xe" or property == "54":
        print_element_properties(53)
    elif property == "Cesium" or property == "Cs" or property == "55":
        print_element_properties(54)
    elif property == "Barium" or property == "Ba" or property == "56":
        print_element_properties(55)
    elif property == "Lanthanum" or property == "La" or property == "57":
        print_element_properties(56)
    elif property == "Cerium" or property == "Ce" or property == "58":
        print_element_properties(57)
    elif property == "Praseodymium" or property == "Pr" or property == "59":
        print_element_properties(58)
    elif property == "Neodymium" or property == "Nd" or property == "60":
        print_element_properties(59)
    elif property == "Promethium" or property == "Pm" or property == "61":
        print_element_properties(60)
    elif property == "Samarium" or property == "Sm" or property == "62":
        print_element_properties(61)
    elif property == "Europium" or property == "Eu" or property == "63":
        print_element_properties(62)
    elif property == "Gadolinium" or property == "Gd" or property == "64":
        print_element_properties(63)
    elif property == "Terbium" or property == "Tb" or property == "65":
        print_element_properties(64)
    elif property == "Dysprosium" or property == "Dy" or property == "66":
        print_element_properties(65)
    elif property == "Holmium" or property == "Ho" or property == "67":
        print_element_properties(66)
    elif property == "Erbium" or property == "Er" or property == "68":
        print_element_properties(67)
    elif property == "Thulium" or property == "Tm" or property == "69":
        print_element_properties(68)
    elif property == "Ytterbium" or property == "Yb" or property == "70":
        print_element_properties(69)
    elif property == "Lutetium" or property == "Lu" or property == "71":
        print_element_properties(70)
    elif property == "Hafnium" or property == "Hf" or property == "72":
        print_element_properties(71)
    elif property == "Tantalum" or property == "Ta" or property == "73":
        print_element_properties(72)
    elif property == "Tungsten" or property == "W" or property == "74":
        print_element_properties(73)
    elif property == "Rhenium" or property == "Re" or property == "75":
        print_element_properties(74)
    elif property == "Osmium" or property == "Os" or property == "76":
        print_element_properties(75)
    elif property == "Iridium" or property == "Ir" or property == "77":
        print_element_properties(76)
    elif property == "Platinum" or property == "Pt" or property == "78":
        print_element_properties(77)
    elif property == "Gold" or property == "Au" or property == "79":
        print_element_properties(78)
    elif property == "Mercury" or property == "Hg" or property == "80":
        print_element_properties(79)
    elif property == "Thallium" or property == "Tl" or property == "81":
        print_element_properties(80)
    elif property == "Lead" or property == "Pb" or property == "82":
        print_element_properties(81)
    elif property == "Bismuth" or property == "Bi" or property == "83":
        print_element_properties(82)
    elif property == "Polonium" or property == "Po" or property == "84":
        print_element_properties(83)
    elif property == "Astatine" or property == "At" or property == "85":
        print_element_properties(84)
    elif property == "Radon" or property == "Rn" or property == "86":
        print_element_properties(85)
    elif property == "Francium" or property == "Fr" or property == "87":
        print_element_properties(86)
    elif property == "Radium" or property == "Ra" or property == "88":
        print_element_properties(87)
    elif property == "Actinium" or property == "Ac" or property == "89":
        print_element_properties(88)
    elif property == "Thorium" or property == "Th" or property == "90":
        print_element_properties(89)
    elif property == "Protactinium" or property == "Pa" or property == "91":
        print_element_properties(90)
    elif property == "Uranium" or property == "U" or property == "92":
        print_element_properties(91)
    elif property == "Neptunium" or property == "Np" or property == "93":
        print_element_properties(92)
    elif property == "Plutonium" or property == "Pu" or property == "94":
        print_element_properties(93)
    elif property == "Americium" or property == "Am" or property == "95":
        print_element_properties(94)
    elif property == "Curium" or property == "Cm" or property == "96":
        print_element_properties(95)
    elif property == "Berkelium" or property == "Bk" or property == "97":
        print_element_properties(96)
    elif property == "Californium" or property == "Cf" or property == "98":
        print_element_properties(97)
    elif property == "Einsteinium" or property == "Es" or property == "99":
        print_element_properties(98)
    elif property == "Fermium" or property == "Fm" or property == "100":
        print_element_properties(99)
    elif property == "Mendelevium" or property == "Md" or property == "101":
        print_element_properties(100)
    elif property == "Nobelium" or property == "No" or property == "102":
        print_element_properties(101)
    elif property == "Lawrencium" or property == "Lr" or property == "103":
        print_element_properties(102)
    elif property == "Rutherfordium" or property == "Rf" or property == "104":
        print_element_properties(103)
    elif property == "Dubnium" or property == "Db" or property == "105":
        print_element_properties(104)
    elif property == "Seaborgium" or property == "Sg" or property == "106":
        print_element_properties(105)
    elif property == "Bohrium" or property == "Bh" or property == "107":
        print_element_properties(106)
    elif property == "Hassium" or property == "Hs" or property == "108":
        print_element_properties(107)
    elif property == "Meitnerium" or property == "Mt" or property == "109":
        print_element_properties(108)
    elif property == "Darmstadtium" or property == "Ds" or property == "110":
        print_element_properties(109)
    elif property == "Roentgenium" or property == "Rg" or property == "111":
        print_element_properties(110)
    elif property == "Copernicium" or property == "Cn" or property == "112":
        print_element_properties(111)
    elif property == "Nihonium" or property == "Nh" or property == "113":
        print_element_properties(112)
    elif property == "Flerovium" or property == "Fl" or property == "114":
        print_element_properties(113)
    elif property == "Moscovium" or property == "Mc" or property == "115":
        print_element_properties(114)
    elif property == "Livermorium" or property == "Lv" or property == "116":
        print_element_properties(115)
    elif property == "Tennessine" or property == "Ts" or property == "117":
        print_element_properties(116)
    elif property == "Oganesson" or property == "Og" or property == "118":
        print_element_properties(117)
    else:
        print("Element not recognized.")



    