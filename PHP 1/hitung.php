<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator Luas dan Keliling Bangun Datar</title>
</head>
<body>
    <h1>Kalkulator Luas dan Keliling Bangun Datar</h1>
    <form method="post" action="hitung.php">
        Pilih Bangun Datar:
        <select name="bangunDatar">
            <option value="persegi">Persegi</option>
            <option value="persegipanjang">Persegi Panjang</option>
            <option value="segitiga">Segitiga</option>
            <option value="lingkaran">Lingkaran</option>
        </select>
        <br>
        Nilai 1: <input type="text" name="input1" placeholder="Masukkan Nilai 1">
        Nilai 2: <input type="text" name="input2" placeholder="Masukkan Nilai 2">
        <input type="submit" name="hitung" value="Hitung">
    </form>
</body>
</html>
<?php
// Include kelas-kelas PHP
require_once('BangunDatar.php');
require_once('Persegi.php');
require_once('PersegiPanjang.php');
require_once('Segitiga.php');
require_once('Lingkaran.php');

if (isset($_POST['hitung'])) {
    $selectedShape = $_POST['bangunDatar'];
    $luas = 0;
    $keliling = 0;

    // Membuat objek berdasarkan pilihan pengguna
    if ($selectedShape == "persegi") {
        $persegi = new Persegi($_POST['input1']);
        $luas = $persegi->hitungLuas();
        $keliling = $persegi->hitungKeliling();
    } elseif ($selectedShape == "persegipanjang") {
        $persegipanjang = new PersegiPanjang($_POST['input1'], $_POST['input2']);
        $luas = $persegipanjang->hitungLuas();
        $keliling = $persegipanjang->hitungKeliling();
    } elseif ($selectedShape == "segitiga") {
        $segitiga = new Segitiga($_POST['input1'], $_POST['input2']);
        $luas = $segitiga->hitungLuas();
        $keliling = $segitiga->hitungKeliling();
    } elseif ($selectedShape == "lingkaran") {
        $lingkaran = new Lingkaran($_POST['input1']);
        $luas = $lingkaran->hitungLuas();
        $keliling = $lingkaran->hitungKeliling();
    }

    echo "Luas " . $selectedShape . " adalah: " . $luas . "<br>";
    echo "Keliling " . $selectedShape . " adalah: " . $keliling;
}
?>