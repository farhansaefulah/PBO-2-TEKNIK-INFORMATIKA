<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $niap = "";
    public $nama = "";
    public $jk = "";
    public $prodi = "";
    public $notelp = "";
    public $alamat = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_niap(int $niap)
    {
        $query = "SELECT * FROM $this->table WHERE niap = $niap";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`niap`,`nama`,`jk`,`prodi`,`notelp`,`alamat`) VALUES ('$this->niap','$this->nama','$this->jk','$this->prodi','$this->notelp','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET niap = '$this->niap', nama = '$this->nama', jk = '$this->jk', prodi = '$this->prodi', notelp = '$this->notelp', alamat = '$this->alamat' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_niap($niap): int
    {
        $query = "UPDATE $this->table SET niap = '$this->niap', nama = '$this->nama', jk = '$this->jk', prodi = '$this->prodi', notelp = '$this->notelp', alamat = '$this->alamat' 
        WHERE niap = $niap";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_niap($niap): int
    {
        $query = "DELETE FROM $this->table WHERE niap = $niap";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>