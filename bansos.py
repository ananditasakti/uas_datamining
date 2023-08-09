import pandas as pd
import cmath

# Load the CSV data
data = pd.read_csv('data_bantuan.csv')

# Menampilkan beberapa baris pertama data
print(data.to_string(index=False))
print("\n")
print("=" * 60)
print("Total")
dt = data.shape[0]
print("Jumlah :",dt)

bs = pd.DataFrame(data)
bsy = bs[bs['Bantuan Sosial'] == 'Ya']
ya = bsy.shape[0]
print("YA :",ya)

bst = bs[bs['Bantuan Sosial'] == 'Tidak']
td = bst.shape[0]
print("TIDAK :",td)

# Nilai dari K2, L2, dan J2
K2 = ya
L2 = td
J2 = dt

# Menghitung logaritma basis 2 dari angka kompleks
log_K2_J2 = cmath.log(K2 / J2, 2)
log_L2_J2 = cmath.log(L2 / J2, 2)
# Menghitung hasil sesuai dengan rumus Excel yang diberikan
result = ((-K2 / J2) * log_K2_J2 + (-L2 / J2) * log_L2_J2).real
print("Entropy:", result)
print("=" * 60)
