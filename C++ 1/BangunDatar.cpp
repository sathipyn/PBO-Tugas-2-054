#include <iostream>

using namespace std;

class BangunDatar {
public:
  virtual void hitungLuas() { cout << "Luas Bangun Datar Induk" << endl; }

  virtual void hitungKeliling() {
    cout << "Keliling Bangun Datar Induk" << endl;
  }
};

class Persegi : public BangunDatar {
public:
  void hitungLuas() override {
    double sisi;
    cout << "Masukkan panjang sisi persegi: ";
    cin >> sisi;
    double luas = sisi * sisi;
    cout << "Luas persegi: " << luas << endl;
  }

  void hitungKeliling() override {
    double sisi;
    cout << "Masukkan panjang sisi persegi: ";
    cin >> sisi;
    double keliling = 4 * sisi;
    cout << "Keliling persegi: " << keliling << endl;
  }
};

class PersegiPanjang : public BangunDatar {
public:
  void hitungLuas() override {
    double panjang, lebar;
    cout << "Masukkan panjang dan lebar persegi panjang (beri spasi): ";
    cin >> panjang >> lebar;
    double luas = panjang * lebar;
    cout << "Luas persegi panjang: " << luas << endl;
  }

  void hitungKeliling() override {
    double panjang, lebar;
    cout << "Masukkan panjang dan lebar persegi panjang (beri spasi): ";
    cin >> panjang >> lebar;
    double keliling = 2 * (panjang + lebar);
    cout << "Keliling persegi panjang: " << keliling << endl;
  }
};

class Segitiga : public BangunDatar {
public:
  void hitungLuas() override {
    double alas, tinggi;
    cout << "Masukkan panjang alas dan tinggi segitiga (beri spasi) : ";
    cin >> alas >> tinggi;
    double luas = 0.5 * alas * tinggi;
    cout << "Luas segitiga: " << luas << endl;
  }

  void hitungKeliling() override {
    double sisi1, sisi2, sisi3;
    cout << "Masukkan panjang sisi-sisi segitiga (beri spasi) :  ";
    cin >> sisi1 >> sisi2 >> sisi3;
    double keliling = sisi1 + sisi2 + sisi3;
    cout << "Keliling segitiga: " << keliling << endl;
  }
};

class Lingkaran : public BangunDatar {
public:
  void hitungLuas() override {
    double jariJari;
    cout << "Masukkan jari-jari lingkaran: ";
    cin >> jariJari;
    double luas = 3.14 * jariJari * jariJari;
    cout << "Luas lingkaran: " << luas << endl;
  }

  void hitungKeliling() override {
    double jariJari;
    cout << "Masukkan jari-jari lingkaran: ";
    cin >> jariJari;
    double keliling = 2 * 3.14 * jariJari;
    cout << "Keliling lingkaran: " << keliling << endl;
  }
};

int main() {
  BangunDatar *bangunDatar;

  cout << "Pilih bangun datar (1. Persegi, 2. Persegi Panjang, 3. Segitiga, 4. "
          "Lingkaran): ";
  int pilihan;
  cin >> pilihan;

  switch (pilihan) {
  case 1:
    bangunDatar = new Persegi();
    break;
  case 2:
    bangunDatar = new PersegiPanjang();
    break;
  case 3:
    bangunDatar = new Segitiga();
    break;
  case 4:
    bangunDatar = new Lingkaran();
    break;
  default:
    cout << "Pilihan tidak valid." << endl;
    return 1;
  }

  bangunDatar->hitungLuas();
  bangunDatar->hitungKeliling();

  delete bangunDatar;

  return 0;
}
