<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kodebuku = "";
    public $judul = "";
    public $penulis = "";
    public $penerbit = "";
    public $tahunpenerbit = "";
    public $stok = "";
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
    public function get_by_kodebuku(int $kodebuku)
    {
        $query = "SELECT * FROM $this->table WHERE kodebuku = $kodebuku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodebuku`,`judul`,`penulis`,`penerbit`,`tahunpenerbit`,`stok`) VALUES ('$this->kodebuku','$this->judul','$this->penulis','$this->penerbit','$this->tahunpenerbit','$this->stok')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', penulis = '$this->penulis', penerbit = '$this->penerbit', tahunpenerbit = '$this->tahunpenerbit', stok = '$this->stok' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodebuku($kodebuku): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', penulis = '$this->penulis', penerbit = '$this->penerbit', tahunpenerbit = '$this->tahunpenerbit', stok = '$this->stok' 
        WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodebuku($kodebuku): int
    {
        $query = "DELETE FROM $this->table WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>