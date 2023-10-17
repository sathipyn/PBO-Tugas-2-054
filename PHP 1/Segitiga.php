<?php
// Class Anak: Segitiga
class Segitiga extends BangunDatar {
    protected $tinggi;

    public function __construct($alas, $tinggi) {
        $this->tinggi = $tinggi;
        parent::__construct($alas);
    }

    public function hitungLuas() {
        return 0.5 * $this->sisi * $this->tinggi;
    }

    public function hitungKeliling() {
        $sisi3 = sqrt($this->sisi ** 2 + $this->tinggi ** 2);
        return $this->sisi + $this->tinggi + $sisi3;
    }
}
?>
