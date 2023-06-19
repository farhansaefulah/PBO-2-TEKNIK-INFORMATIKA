<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kodepinjam = "";
    public $tglpinjam = "";
    public $tglhrskembali = "";
    public $kodebuku = "";
    public $niap = "";
    public $nipp = "";
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
    public function get_by_kodepinjam(int $kodepinjam)
    {
        $query = "SELECT * FROM $this->table WHERE kodepinjam = $kodepinjam";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodepinjam`,`tglpinjam`,`tglhrskembali`,`kodebuku`,`niap`,`nipp`) VALUES ('$this->kodepinjam','$this->tglpinjam','$this->tglhrskembali','$this->kodebuku','$this->niap','$this->nipp')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodepinjam = '$this->kodepinjam', tglpinjam = '$this->tglpinjam', tglhrskembali = '$this->tglhrskembali', kodebuku = '$this->kodebuku', niap = '$this->niap', nipp = '$this->nipp' 
        WHERE id_pinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodepinjam($kodepinjam): int
    {
        $query = "UPDATE $this->table SET kodepinjam = '$this->kodepinjam', tglpinjam = '$this->tglpinjam', tglhrskembali = '$this->tglhrskembali', kodebuku = '$this->kodebuku', niap = '$this->niap', nipp = '$this->nipp' 
        WHERE kodepinjam = $kodepinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_pinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodepinjam($kodepinjam): int
    {
        $query = "DELETE FROM $this->table WHERE kodepinjam = $kodepinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>