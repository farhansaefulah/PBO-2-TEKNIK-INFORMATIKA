<?php
require_once 'database.php';
require_once 'Petugas.php';
$db = new MySQLDatabase();
$petugas = new Petugas($db);
$id=0;
$nipp=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nipp'])){
            $nipp = $_GET['nipp'];
        }
        if($id>0){    
            $result = $petugas->get_by_id($id);
        }elseif($nipp>0){
            $result = $petugas->get_by_nipp($nipp);
        } else {
            $result = $petugas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new petugas
        $petugas->nipp = $_POST['nipp'];
        $petugas->nama = $_POST['nama'];
        $petugas->jabatan = $_POST['jabatan'];
        $petugas->notelp = $_POST['notelp'];
        $petugas->alamat = $_POST['alamat'];
       
        $petugas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas not created.';
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
        if(isset($_GET['nipp'])){
            $nipp = $_GET['nipp'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $petugas->nipp = $_PUT['nipp'];
        $petugas->nama = $_PUT['nama'];
        $petugas->jabatan = $_PUT['jabatan'];
        $petugas->notelp = $_PUT['notelp'];
        $petugas->alamat = $_PUT['alamat'];
        if($id>0){    
            $petugas->update($id);
        }elseif($nipp<>""){
            $petugas->update_by_nipp($nipp);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nipp'])){
            $nipp = $_GET['nipp'];
        }
        if($id>0){    
            $petugas->delete($id);
        }elseif($nipp>0){
            $petugas->delete_by_nipp($nipp);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas delete failed.';
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