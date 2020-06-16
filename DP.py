# Dynamic Programming
import time
start_time = time.time()
def DynamicProgram(W, wObjek, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Buat Tabel K[baris][kolom] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wObjek[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wObjek[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# value (profit), berat Objek, dan kapasitas pesawat 
brt = [100, 90, 75, 80]                             # objek dalam kg orang/barang
val = [140, 250, 120, 200]                          # profit diambil ketika kelas/harga setiap objek berbeda
kapasitas = 300                                     # Kapasitas Pesawat

n = len(val)
hasil = DynamicProgram(kapasitas, brt, val, n)

#Output 
print("Dynamic Programming")
print("Dengan Problem -Optimation Problem Dalam Kasus Muatan Pesawat-")
print("Profit berdasarkan Dynamic Programming = " + str(hasil)) 
print("Running time = %s sec" % (time.time() - start_time))
