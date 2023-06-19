<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$kodepinjam=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodepinjam'])){
            $kodepinjam = $_GET['kodepinjam'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($kodepinjam>0){
            $result = $peminjaman->get_by_kodepinjam($kodepinjam);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->kodepinjam = $_POST['kodepinjam'];
        $peminjaman->tglpinjam = $_POST['tglpinjam'];
        $peminjaman->tglhrskembali = $_POST['tglhrskembali'];
        $peminjaman->kodebuku = $_POST['kodebuku'];
        $peminjaman->niap = $_POST['niap'];
        $peminjaman->nipp = $_POST['nipp'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodepinjam'])){
            $kodepinjam = $_GET['kodepinjam'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->kodepinjam = $_PUT['kodepinjam'];
        $peminjaman->tglpinjam = $_PUT['tglpinjam'];
        $peminjaman->tglhrskembali = $_PUT['tglhrskembali'];
        $peminjaman->kodebuku = $_PUT['kodebuku'];
        $peminjaman->niap = $_PUT['niap'];
        $peminjaman->nipp = $_PUT['nipp'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($kodepinjam<>""){
            $peminjaman->update_by_kodepinjam($kodepinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodepinjam'])){
            $kodepinjam = $_GET['kodepinjam'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($kodepinjam>0){
            $peminjaman->delete_by_kodepinjam($kodepinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>