-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Jun 2023 pada 14.13
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbperpustakaan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `anggota`
--

CREATE TABLE `anggota` (
  `id` int(11) NOT NULL,
  `niap` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` enum('L','P') NOT NULL DEFAULT 'L',
  `prodi` enum('TIF','IND','PET') NOT NULL DEFAULT 'TIF',
  `notelp` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `anggota`
--

INSERT INTO `anggota` (`id`, `niap`, `nama`, `jk`, `prodi`, `notelp`, `alamat`) VALUES
(17, 1001, 'Farhan Saefulah', 'L', 'TIF', '089111', 'Cirebon'),
(18, 1002, 'Rere', 'P', 'TIF', '628', 'Bandung'),
(19, 1003, 'Ferro', 'L', 'IND', '1234', 'Cirebon'),
(20, 1004, 'Frisil', 'P', 'PET', '56789', 'Cirebon'),
(23, 1006, 'Han Saefulah', 'L', 'IND', '123', 'Cirebon');

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `kodebuku` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `penulis` varchar(100) NOT NULL,
  `penerbit` varchar(100) NOT NULL,
  `tahunpenerbit` int(4) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`id`, `kodebuku`, `judul`, `penulis`, `penerbit`, `tahunpenerbit`, `stok`) VALUES
(4, 1, 'Belajar Bahasa Pemograman', 'Farhan Saefulah', 'Jaya Baya', 2022, 3),
(5, 2, 'Belajar Laravel', 'Farhan Saefulah', 'Han', 2023, 10);

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id_pinjam` int(11) NOT NULL,
  `kodepinjam` int(11) NOT NULL,
  `tglpinjam` varchar(50) NOT NULL,
  `tglhrskembali` varchar(50) NOT NULL,
  `kodebuku` varchar(11) NOT NULL,
  `niap` int(11) NOT NULL,
  `nipp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `peminjaman`
--

INSERT INTO `peminjaman` (`id_pinjam`, `kodepinjam`, `tglpinjam`, `tglhrskembali`, `kodebuku`, `niap`, `nipp`) VALUES
(4, 3, 'Senin, 26 Juni 2023', 'Rabu,28 Juni 2023', 'BC', 1003, 1001);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id` int(11) NOT NULL,
  `kode` int(11) NOT NULL,
  `tglkembali` varchar(50) NOT NULL,
  `denda` int(11) NOT NULL,
  `kodebuku` varchar(11) NOT NULL,
  `niap` int(11) NOT NULL,
  `nipp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pengembalian`
--

INSERT INTO `pengembalian` (`id`, `kode`, `tglkembali`, `denda`, `kodebuku`, `niap`, `nipp`) VALUES
(1, 1, 'Kamis, 29 Juni 2023', 5000, 'PO', 1003, 1001);

-- --------------------------------------------------------

--
-- Struktur dari tabel `petugas`
--

CREATE TABLE `petugas` (
  `id` int(11) NOT NULL,
  `nipp` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `jabatan` enum('Kepala Perpus','Super Admin','Admin') NOT NULL DEFAULT 'Admin',
  `notelp` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `petugas`
--

INSERT INTO `petugas` (`id`, `nipp`, `nama`, `jabatan`, `notelp`, `alamat`) VALUES
(2, 1001, 'Farhan Saefulah', 'Kepala Perpus', '089', 'Cirebon');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `rolename` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `passwd`, `rolename`) VALUES
(1, 'petugas', '202cb962ac59075b964b07152d234b70', 'admin'),
(2, 'anggota', '202cb962ac59075b964b07152d234b70', 'dosen');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unik` (`niap`);

--
-- Indeks untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unik` (`kodebuku`);

--
-- Indeks untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`id_pinjam`),
  ADD UNIQUE KEY `unik` (`kodepinjam`),
  ADD KEY `id_buku` (`kodebuku`),
  ADD KEY `id_anggota` (`niap`),
  ADD KEY `id_petugas` (`nipp`),
  ADD KEY `id_buku_2` (`kodebuku`);

--
-- Indeks untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unik` (`kode`),
  ADD KEY `id_buku` (`kodebuku`),
  ADD KEY `id_anggota` (`niap`),
  ADD KEY `id_petugas` (`nipp`);

--
-- Indeks untuk tabel `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unik` (`nipp`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idx` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `id_pinjam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `petugas`
--
ALTER TABLE `petugas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
