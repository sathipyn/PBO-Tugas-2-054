<?php
// Class Anak: Persegi Panjang
class PersegiPanjang extends BangunDatar {
    protected $panjang;
    
    public function __construct($panjang, $lebar) {
        $this->panjang = $panjang;
        parent::__construct($lebar);
    }

    public function hitungLuas() {
        return $this->panjang * $this->sisi;
    }

    public function hitungKeliling() {
        return 2 * ($this->panjang + $this->sisi);
    }
}
?>
