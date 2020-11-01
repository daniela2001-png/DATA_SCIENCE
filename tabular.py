import pandas as pd
import matplotlib.pyplot as plt

# N numero en millones de usuarios
# t tiempo estimaciones semestrales

tabula = [
    {
        't':1996,
        'N':44,
    },

    {
        't': 1998,
        'N': 69,
    },
    {
        't': 2000,
        'N': 109,
    },

    {
        't': 2002,
        'N': 141,
    },

    {
        't': 2004,
        'N': 182,
    },

    {
        't':2006,
        'N':232,
    }
]

df = pd.DataFrame(tabula)
print(df)
fig, ax = plt.subplots()
ax.plot(df['N'], df['t'], marker='v', linestyle='--')

plt.xlabel('tiempo estimaciones semestrales')
plt.ylabel('número en millones de usuarios')
plt.title('el número N (en millones) de usuarios de telefonía celular en EU. (Se dan estimaciones semestrales.)')
plt.show()