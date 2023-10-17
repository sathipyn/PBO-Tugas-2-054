<?php
// Class Anak: Lingkaran
class Lingkaran extends BangunDatar {
    public function hitungLuas() {
        return 3.14 * $this->sisi * $this->sisi;
    }

    public function hitungKeliling() {
        return 2 * 3.14 * $this->sisi;
    }
}
?>
