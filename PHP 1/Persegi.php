<?php
// Class Anak: Persegi
class Persegi extends BangunDatar {
    public function hitungLuas() {
        return $this->sisi * $this->sisi;
    }

    public function hitungKeliling() {
        return 4 * $this->sisi;
    }
}
?>