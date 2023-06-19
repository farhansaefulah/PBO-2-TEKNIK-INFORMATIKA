<?php
//Simpanlah dengan nama file : Petugas.php
require_once 'database.php';
class Petugas 
{
    private $db;
    private $table = 'petugas';
    public $nipp = "";
    public $nama = "";
    public $jabatan = "";
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
    public function get_by_nipp(int $nipp)
    {
        $query = "SELECT * FROM $this->table WHERE nipp = $nipp";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nipp`,`nama`,`jabatan`,`notelp`,`alamat`) VALUES ('$this->nipp','$this->nama','$this->jabatan','$this->notelp','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nipp = '$this->nipp', nama = '$this->nama', jabatan = '$this->jabatan', notelp = '$this->notelp', alamat = '$this->alamat' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nipp($nipp): int
    {
        $query = "UPDATE $this->table SET nipp = '$this->nipp', nama = '$this->nama', jabatan = '$this->jabatan', notelp = '$this->notelp', alamat = '$this->alamat' 
        WHERE nipp = $nipp";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nipp($nipp): int
    {
        $query = "DELETE FROM $this->table WHERE nipp = $nipp";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>