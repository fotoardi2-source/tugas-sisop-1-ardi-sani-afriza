1.percobaan 1 : 200000
   percobaan 2 : 200002
   percobaan 3 : 200002
   percobaan 4 : 200001
   petcobaan 5 : 200000
2.Inkonsistensi terjadi karena Race Condition. Operasi counter += 1 bersifat tidak atomik, yang artinya terdiri dari tiga langkah di tingkat CPU
3.Lost Update: Pembaruan yang dilakukan oleh Thread 1 hilang karena Thread 2 menuliskan nilai yang ia hitung berdasarkan data "basi" (nilai 100).
​Non-Atomic: Operasi += di Python sebenarnya melibatkan beberapa instruksi bytecode (LOAD_GLOBAL, BINARY_ADD, STORE_GLOBAL). Interleaving bisa terjadi di sela-sela instruksi tersebut.